
# Generate executable in windows
#
# Ensure that cwd is the root directory of the git repository

python -m venv venv
venv/scripts/activate

python -m pip install --upgrade pip
pip install --upgrade -r requirements.txt

pyinstaller -F main.py
