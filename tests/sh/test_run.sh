#!/bin/bash
#
# project.sh runs the right export script for each request, with the project
# in PROJECT and scripts/ on the PYTHONPATH, for one project or all of them
# (never the shared typesetters), and from any directory. It skips outputs
# that exist, reports a failed export with exit code 1, and stops when a
# program it needs is missing.
#
# Runs in a sandbox (see lib.sh) with a stand-in python3, so nothing is typeset.
# Run from anywhere: bash tests/sh/test_run.sh

# shellcheck source=tests/sh/lib.sh
. "$(dirname "$0")/lib.sh"
sandbox

# expect_calls <description> <expected calls.log> -- <project.sh arguments>
expect_calls() {

    local description=$1 expected=$2
    shift 3
    : > calls.log
    ./project.sh "$@" > output.log 2>&1
    if [ "$(cat calls.log)" = "$expected" ]; then
        pass "$description"
    else
        fail "$description: ./project.sh $* ran"$'\n'"$(cat calls.log)"$'\n'"expected"$'\n'"$expected"
    fi

}

expect_calls "one project, one format" \
    "PROJECT=job-hunting-ada-cv-twopages PYTHONPATH=scripts python3 scripts/exportpdf.py" \
    -- job-hunting-ada-cv-twopages pdf

expect_calls "odf runs saveodf.py" \
    "PROJECT=accounting-acme-invoice-onepage PYTHONPATH=scripts python3 scripts/saveodf.py" \
    -- accounting-acme-invoice-onepage odf

expect_calls "all runs every project, sorted, and not the typesetters" \
    "PROJECT=accounting-acme-invoice-onepage PYTHONPATH=scripts python3 scripts/exportdocx.py
PROJECT=job-hunting-ada-cv-twopages PYTHONPATH=scripts python3 scripts/exportdocx.py
PROJECT=project-management-depot-risk-register-fourpages PYTHONPATH=scripts python3 scripts/exportdocx.py" \
    -- all docx

: > calls.log
./project.sh typesetting pdf > output.log 2>&1
code=$?
check "the typesetters are not a project" [ "$code" -eq 1 ] && [ ! -s calls.log ]

: > calls.log
PYTHONPATH=/elsewhere ./project.sh job-hunting-ada-cv-twopages rtf > /dev/null 2>&1
check "an existing PYTHONPATH is kept after scripts/" \
    grep -qx "PROJECT=job-hunting-ada-cv-twopages PYTHONPATH=scripts:/elsewhere python3 scripts/exportrtf.py" calls.log

: > calls.log
(cd / && "$SANDBOX/project.sh" accounting-acme-invoice-onepage html > /dev/null 2>&1)
check "it runs from any directory" \
    grep -qx "PROJECT=accounting-acme-invoice-onepage PYTHONPATH=scripts python3 scripts/exporthtml.py" calls.log

: > calls.log
./project.sh accounting-acme-invoice-onepage all > /dev/null 2>&1
count=$(formats | wc -l)
check "<project> all runs every format and odf ($((count + 1)) runs)" \
    [ "$(wc -l < calls.log)" -eq $((count + 1)) ]
check "and each of them once" [ "$(sort -u calls.log | wc -l)" -eq $((count + 1)) ]

mkdir -p build
touch build/job-hunting-ada-cv-twopages.epub
expect_calls "an existing output is skipped" "" -- job-hunting-ada-cv-twopages epub
check "and says so" grep -q "Skipping build/job-hunting-ada-cv-twopages.epub" output.log
rm -rf build

PYTHON_EXIT=1 ./project.sh all pdf > output.log 2>&1
code=$?
check "a failed export exits with 1" [ "$code" -eq 1 ]
check "and names the project" grep -q "FAILED: exportpdf for job-hunting-ada-cv-twopages" output.log
check "and goes on with the other projects" [ "$(grep -c FAILED output.log)" -eq 3 ]

# only the stand-ins and the basic tools project.sh uses on the PATH
mkdir tools
for tool in bash find sort head paste dirname grep; do
    ln -s "$(command -v "$tool")" "tools/$tool"
done
for missing in soffice python3; do
    mv "bin/$missing" "bin/$missing.away"
    PATH="$SANDBOX/bin:$SANDBOX/tools" ./project.sh accounting-acme-invoice-onepage pdf > output.log 2>&1
    code=$?
    mv "bin/$missing.away" "bin/$missing"
    check "without $missing it exits with 1" [ "$code" -eq 1 ]
    check "and names $missing" grep -q "$missing is required" output.log
done

finish
