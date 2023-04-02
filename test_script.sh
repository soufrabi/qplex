# Test script
#
# 


#Install in virtualenv
python3 -m venv venv/bin/activate

if [ -f venv/bin/activate ]; then
    echo "Good to go"
    echo "Python virtualenv created properly"
else
    echo "Virtual environment not created properly"
    echo "Manually install python-pip or python3-pip"
    echo "Then, try again"
    echo "Abort test"
    exit 1
  
fi

source venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install PySide6
python3 -m pip install openai
# python3 -m pip install pyinstaller
which python

python3 src/main.py
