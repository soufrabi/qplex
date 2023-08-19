#!/bin/sh

show_help(){

	cat << EOF
linux.sh

Choose one of the available commands:
	build
	setup
	install-dependencies
	help | --help | -h
	
EOF


}


if [ $# -eq 0 ]; then
	show_help
	exit
fi





_install_dependencies() {
	echo "Install dependencies in Linux"

	sudo apt update && sudo apt install -y libgl1 ffmpeg libsm6 libxext6 libegl1 '^libxcb.*-dev' libx11-xcb-dev libglu1-mesa-dev libxrender-dev libxi-dev libxkbcommon-dev libxkbcommon-x11-dev


}




_setup() {
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

pip3 install --upgrade -r requirements.txt
# python3 -m pip install PySide6
# python3 -m pip install openai
# python3 -m pip install pyinstaller

}

_build() {

    . venv/bin/activate
    pyinstaller -F main.py

    build_dir="build_linux"
    _pkgname="openai-client"


    echo ${build_dir}
	rm -rf ${build_dir}
	mkdir -pv "${build_dir}/${_pkgname}"
	mkdir -pv "${build_dir}/${_pkgname}/usr"
	mkdir -pv "${build_dir}/${_pkgname}/opt/${_pkgname}"
	cp -rv "assets/DEBIAN" "${build_dir}/${_pkgname}"
	cp -rv "dist/main" "${build_dir}/${_pkgname}/opt/${_pkgname}"
	cp -rv "assets/usr/bin" "${build_dir}/${_pkgname}/usr"
	cp -rv "assets/usr/share" "${build_dir}/${_pkgname}/usr"
	cd ${build_dir} && dpkg-deb --build ${_pkgname}

}





main() {

	case "$1" in 
		(build)
			shift
			_build "$@"
			;;
		(install-dependencies)
			shift
			_install_dependencies "$@"
			;;
		(setup)
			shift
			_setup "$@"
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