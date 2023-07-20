# Build script

git clone https://github.com/awesomeDev12/openai-client.git main_repo


sudo apt install python3-pip
pip install venvs


# Run this command if the above the command is not working
# Check version before installing (Its needed for debian systems)
#sudo apt install python3.10-venv


#Install in virtualenv
python3 -m venv .venvs/openai-client-venv

if [ -f .venvs/openai-client-venv/bin/activate ]; then
    echo "Good to go"
    echo "Python virtualenv created properly"
else
    echo "Virtual environment not created properly"
    read -p "Do you wish to manually install the dependencies(Y/N):" apt_install
    if [ "$apt_install" = "Y" ]
    then
        sudo apt install python3.10-venv
    else	    
        echo "Abort Install"
        exit 1
    fi
fi


# Final check
if [ -f .venvs/openai-client-venv/bin/activate ]; then
    echo "Good to go"
    echo "Python virtualenv created properly"
else
    echo "Virtual environment not created properly"
    echo "Abort Install"
    exit 1
fi


source .venvs/openai-client-venv/bin/activate
python3 -m pip install --upgrade pip
pip install --upgrade -r main_repo/requirements.txt
# python3 -m pip install PySide6
# python3 -m pip install openai
# python3 -m pip install pyinstaller
which python

pyinstaller main_repo/main.py


mkdir -p openai-client/opt
mkdir -p openai-client/opt/openai-client-bin


cp -r dist/main openai-client/opt/openai-client-bin/binaries

dpkg-deb --build openai-client

# deactivate virtualenv
# deactivate
