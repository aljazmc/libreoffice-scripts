#!/bin/bash
#
# The formats in project.sh, the exporters in scripts/ and the README agree:
# every format has an exporter that writes its own file, every exporter is
# listed, the README's Formats table names every format and its count of
# formats is right, and exactly the image and drawing formats go through
# LibreOffice Draw, as the README says.
#
# Run from anywhere: bash tests/sh/test_formats.sh

# shellcheck source=tests/sh/lib.sh
. "$(dirname "$0")/lib.sh"
cd "$ROOT" || exit 1

mapfile -t known < <(formats)

if [ "${#known[@]}" -lt 30 ]; then
    fail "read the FORMATS of project.sh, got ${#known[@]}: ${known[*]}"
fi

# the README's Images and Drawings rows: what Draw converts
drawn=" $(grep -E '^\| (Images|Drawings) \|' README.md | grep -oE '`[a-z]+`' | tr -d '`' | paste -sd' ') "

for format in "${known[@]}"; do
    script="scripts/export$format.py"
    if [ ! -f "$script" ]; then
        fail "$format has no $script"
        continue
    fi
    # docbook and wordxml are XML, written as <project>.<format>.xml
    extension=".$format"
    case "$format" in
        docbook|wordxml) extension=".$format.xml" ;;
    esac
    check "$script writes $extension" grep -qF "output + \"$extension\"" "$script"
    check "$script writes into build/" grep -qF 'load_project("build")' "$script"
    check "the README lists $format" grep -qE "^\|.*\`$format\`" README.md
    if [[ "$drawn" == *" $format "* ]]; then
        check "$script goes through Draw" grep -qF "export(drawing(document)" "$script"
    else
        check "$script goes through Writer" bash -c "! grep -qF 'drawing(' '$script'"
    fi
done

for script in scripts/export*.py; do
    format=${script#scripts/export}
    format=${format%.py}
    listed=no
    for name in "${known[@]}"; do
        [ "$name" = "$format" ] && listed=yes
    done
    check "$script is in the FORMATS of project.sh" [ "$listed" = yes ]
done

check "scripts/saveodf.py saves the ODT into odf/" grep -qF 'load_project("odf")' scripts/saveodf.py
check "the README lists odf" grep -qE '^\|.*`odf`' README.md

# every format and odf
outputs=$(( ${#known[@]} + 1 ))
check "the README counts $outputs output formats" grep -qF "**$outputs output formats**" README.md

finish
