
# Generate executable in windows
# Ensure that cwd is the root directory of the git repository

$build_dir = "build_binary"
$package_name = "qplex"
$executable_name = "qplex.exe"

function InstallDependencies {
    Write-Host "Install Dependencies"

}

function CreatePythonVirtualEnvironment {

python -m venv venv
venv/scripts/activate

python -m pip install --upgrade pip
pip install -r requirements.txt

pyinstaller -F --add-data "resources;resources" main.py


}

function BuildBinary {

New-Item -Path "$build_dir" -Type Directory

Move-Item -Path ".\dist\main.exe" -Destination "$build_dir\$executable_name"


}

function BuildMain {

InstallDependencies
CreatePythonVirtualEnvironment
BuildBinary
    

}

BuildMain


