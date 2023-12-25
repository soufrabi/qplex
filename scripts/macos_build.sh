#!/bin/sh

_pkgname="qplex"
build_dir="build_binary"

printf "Building for MacOS\n"

python -m venv .venv
. ./.venv/bin/activate
pip install -r requirements.txt
pyinstaller -F --add-data "resources:resources" main.py


mkdir -pv "${build_dir}"
mv dist/main "${build_dir}/${_pkgname}"
