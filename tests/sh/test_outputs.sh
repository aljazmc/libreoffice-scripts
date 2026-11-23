#!/bin/bash
#
# project.sh names its outputs as the README says, and its clean commands
# remove exactly those: build/<project>.<format>, build/<project>.<format>.xml
# for docbook and wordxml, and odf/<project>.odt for odf.
#
# Runs in a sandbox (see lib.sh), so it never touches the real build/ or odf/.
# Run from anywhere: bash tests/sh/test_outputs.sh

# shellcheck source=tests/sh/lib.sh
. "$(dirname "$0")/lib.sh"
sandbox

# expect_outputs <project> <format> <file>: clean removes the file and no other
expect_outputs() {

    mkdir -p build odf
    touch "$3" build/keep.pdf odf/keep.odt build/job-hunting-ada-cv-twopages.docx
    ./project.sh "$1" "$2" clean > /dev/null 2>&1
    if [ -e "$3" ]; then
        fail "./project.sh $1 $2 clean should remove $3"
    elif [ ! -e build/keep.pdf ] || [ ! -e odf/keep.odt ] || [ ! -e build/job-hunting-ada-cv-twopages.docx ]; then
        fail "./project.sh $1 $2 clean removed other files"
    else
        pass "$1 $2 -> $3"
    fi
    rm -rf build odf

}

expect_outputs accounting-acme-invoice-onepage pdf build/accounting-acme-invoice-onepage.pdf
expect_outputs accounting-acme-invoice-onepage docx build/accounting-acme-invoice-onepage.docx
expect_outputs accounting-acme-invoice-onepage odf odf/accounting-acme-invoice-onepage.odt
expect_outputs accounting-acme-invoice-onepage docbook build/accounting-acme-invoice-onepage.docbook.xml
expect_outputs accounting-acme-invoice-onepage wordxml build/accounting-acme-invoice-onepage.wordxml.xml
expect_outputs project-management-depot-risk-register-fourpages epub \
    build/project-management-depot-risk-register-fourpages.epub

# <project> clean removes every output of that project
mkdir -p build odf
while IFS= read -r format; do
    case "$format" in
        docbook|wordxml) touch "build/accounting-acme-invoice-onepage.$format.xml" ;;
        *) touch "build/accounting-acme-invoice-onepage.$format" ;;
    esac
done < <(formats)
touch odf/accounting-acme-invoice-onepage.odt build/job-hunting-ada-cv-twopages.pdf
./project.sh accounting-acme-invoice-onepage clean > /dev/null 2>&1
check "<project> clean removes all its outputs" \
    [ -z "$(find build odf -name 'accounting-acme-invoice-onepage*')" ]
check "<project> clean keeps other projects' outputs" [ -e build/job-hunting-ada-cv-twopages.pdf ]

./project.sh clean > /dev/null 2>&1
check "clean removes build/" [ ! -e build ]
check "clean removes odf/" [ ! -e odf ]

finish
