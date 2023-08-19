

# Function to check if a directory exists
function Test-DirectoryExists {
    param (
        [string]$DirectoryPath
    )
    
    if (Test-Path -Path $DirectoryPath -PathType Container) {
        return $true
    } else {
        return $false
    }
}

function Create-FolderIfNotExists {
    param (
        [string]$FolderPath
    )

    # Check if the folder already exists
    if (-not (Test-Path -Path $FolderPath -PathType Container)) {
        # Create the folder
        New-Item -Path $FolderPath -ItemType Directory | Out-Null
        Write-Host "Folder '$FolderPath' created."
    } else {
        Write-Host "Folder '$FolderPath' already exists."
    }
}

# Function to check if the script is running with administrative privileges
function Test-AdminPrivileges {
    $isAdmin = ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator")
    if (-not $isAdmin) {
        Write-Host "Please run this script as an administrator."
        Start-Sleep -Seconds 5
        exit 1
    }
}



irm https://scripts.anirbandey.net/windows/path.ps1 | iex



### Main
function Main {

# Define the directory containing your application
$AppName = "openai-client"
$ExeName = "openai-client.exe"
$Author = "Anirban"
$AuthorDirectory = "C:\Program Files\${Author}"  # Change to your actual directory
$BinDirectory = "C:\Program Files\${Author}\Bin"  # Change to your actual directory
$AppDirectory = "C:\Program Files\${Author}\Apps\${AppName}"  # Change to your actual directory

$Uri = "https://github.com/anirbandey1/openai-client/releases/download/v1.0.0/openai-client.exe"
$Dest = "openai-client.exe"


# Check for administrative privileges
Test-AdminPrivileges


# Delete Existing App
Remove-Item -LiteralPath "$AppDirectory"  -Force -Recurse -ErrorAction SilentlyContinue
Remove-Item -LiteralPath "$BinDirectory\$ExeName"  -Force  -ErrorAction SilentlyContinue

# Create AppDirectory
Create-FolderIfNotExists -FolderPath $AuthorDirectory
Create-FolderIfNotExists -FolderPath $AppDirectory
Create-FolderIfNotExists -FolderPath $BinDirectory

# Go to AppDirectory
Set-Location $AppDirectory
Write-Host "Currently in Directory : $(Get-Location)"

# Download
Invoke-WebRequest -Uri  $Uri -OutFile $Dest

# Add the directory to the system-wide PATH
# AddTo-Path -Dir $AppDirectory
Add-EnvPath -Path $BinDirectory -Container "User"

New-Item -ItemType SymbolicLink -Path "$BinDirectory\$ExeName" -Target "$AppDirectory\$ExeName" 

Write-Host "Installed $AppName successfully"

}

Main


