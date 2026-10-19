#!/bin/bash

FORMATS=(
    apng bmp doc docbook docm docx dot dotx emf emz eps epub fodg fodt gif
    html jpg otg ott pdf png rtf svg svgz tif txt uot webp wmf wmz wordxml
    xhtml
)

require() {

    local bin
    if bin=$(command -v "$1"); then
        echo "$1 found at: $bin"
    else
        echo "$1 is required but was not found" >&2
        exit 1
    fi

}

run() {

    require python3
    require soffice

    find scripts -maxdepth 2 -mindepth 2 -type f -name "$1" -exec {} \;

}

save() {

    run "save*.py"

}

build() {

    run "*.py"

}

clean() {

    rm -rf build

}

export_format() {

    run "export$1.py"

}

usage() {

    local IFS="|"
    echo "You should use: $0 {save|build|clean|${FORMATS[*]}}" >&2
    exit 1

}

cd "$(dirname "$0")" || exit 1

case "$1" in
    save|build|clean) "$1" ;;
    *)
        for format in "${FORMATS[@]}"; do
            [ "$1" = "$format" ] && { export_format "$1"; exit; }
        done
        usage
        ;;
esac
