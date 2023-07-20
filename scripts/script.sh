#!/bin/sh

if [ ! "$#"  = 1 ] ; then
	echo "Please provide the action to be performed"
	exit 1
fi

action="$1"


if [ "${action}" = "setup" ]; then

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



elif [ "${action}" = "build" ]; then
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


else
    echo "Unknown action"
    
    
fi







