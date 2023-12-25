#!/bin/sh

show_help(){

	cat << EOF
linux.sh

Choose one of the available commands:
    gh
	build
	setup
	deps
	help | --help | -h
	
EOF


}


if [ $# -eq 0 ]; then
	show_help
	exit
fi


build_dir="build_binary"
_pkgname="openai-client"



install_dependencies() {
	echo "Install dependencies in Linux"

	sudo apt update
    sudo apt install -y libgl1 libsm6 libxext6 libegl1 '^libxcb.*-dev' libx11-xcb-dev libglu1-mesa-dev libxrender-dev libxi-dev libxkbcommon-dev libxkbcommon-x11-dev


}




setup_environment() {
#Install in virtualenv
python3 -m venv venv

if [ -f venv/bin/activate ]; then
    echo "Python virtualenv created properly"
else
    echo "Virtual environment not created properly"
    echo "Abort build"
    exit 1
fi

pwd

. venv/bin/activate

which python3
which pip3


python3 -m pip install --upgrade pip

pip3 install -r requirements.txt
# python3 -m pip install PySide6
# python3 -m pip install openai
# python3 -m pip install pyinstaller

}

build_pyinstaller_binary(){

    . venv/bin/activate
    pyinstaller -F --add-data "resources:resources" main.py

}

build_binary() {

    build_pyinstaller_binary


    echo ${build_dir}
	rm -rf ${build_dir}
	mkdir -pv "${build_dir}/${_pkgname}"
	mkdir -pv "${build_dir}/${_pkgname}/usr/bin"
	mkdir -pv "${build_dir}/${_pkgname}/usr/share/applications"
	mkdir -pv "${build_dir}/${_pkgname}/usr/share/icons/hicolor/scalable/apps"
	mkdir -pv "${build_dir}/${_pkgname}/usr/share/${_pkgname}"
	cp -rv "assets/DEBIAN" "${build_dir}/${_pkgname}"
	cp -rv "assets/${_pkgname}" "${build_dir}/${_pkgname}/usr/bin"
	cp -rv "assets/${_pkgname}.desktop" "${build_dir}/${_pkgname}/usr/share/applications"
	cp -rv "assets/${_pkgname}.svg" "${build_dir}/${_pkgname}/usr/share/icons/hicolor/scalable/apps"
	cp -rv "dist/main" "${build_dir}/${_pkgname}/usr/share/${_pkgname}"
	sh -c "cd ${build_dir} && dpkg-deb --build ${_pkgname}"

}


build_gh() {
    install_dependencies
    setup_environment
    build_binary

}

main() {

	case "$1" in 
		(build)
			shift
			build_binary "$@"
			;;
		(deps)
			shift
			install_dependencies "$@"
			;;
		(setup)
			shift
			setup_environment "$@"
			;;
		(gh)
			shift
			build_gh "$@"
			;;
		(help | --help | -h)
			show_help 
			exit 0 
			;;
		(*)
			printf >&2 "Error: invalid command\n"
			show_help
			exit 1
			;;

	esac
	

}

main "$@"
