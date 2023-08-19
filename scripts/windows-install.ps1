

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

# Function to add a directory to the system-wide PATH
# function Add-DirectoryToPath {
#     param (
#         [string]$DirectoryPath
#     )
    
#     # Check if the directory is already in the PATH
#     $existingPath = [System.Environment]::GetEnvironmentVariable("Path", [System.EnvironmentVariableTarget]::Machine)
    
#     if ($existingPath -notlike "*$DirectoryPath*") {
#         # Add the directory to the PATH
#         [System.Environment]::SetEnvironmentVariable("Path", "$existingPath;$DirectoryPath", [System.EnvironmentVariableTarget]::Machine)
#         Write-Host "Added $DirectoryPath to the system-wide PATH."
#     } else {
#         Write-Host "$DirectoryPath is already in the system-wide PATH."
#     }
# }

# function AddTo-Path{
# param(
#     [string]$Dir
# )

#     if( !(Test-Path $Dir) ){
#         Write-warning "Supplied directory was not found!"
#         return
#     }
#     $PATH = [Environment]::GetEnvironmentVariable("PATH", "Machine")
#     if( $PATH -notlike "*"+$Dir+"*" ){
#         [Environment]::SetEnvironmentVariable("PATH", "$PATH;$Dir", "Machine")
#     }
# }



# Define the directory containing your application
$AppName = "openai-client"
$Author = "anirban"
$AppDirectory = "C:\Program Files\${Author}\${AppName}"  # Change to your actual directory
$Uri = "https://github.com/anirbandey1/openai-client/releases/download/v1.0.0/openai-client.exe"
$Dest = "openai-client.exe"


# Check for administrative privileges
Test-AdminPrivileges

# Create AppDirectory
Create-FolderIfNotExists -FolderPath $AppDirectory

# Go to AppDirectory
Set-Location $AppDirectory
Write-Host "Currently in Directory : $(Get-Location)"

# Download
Invoke-WebRequest -Uri  $Uri -OutFile $Dest

# Add the directory to the system-wide PATH
# AddTo-Path -Dir $AppDirectory


Write-Host "Installed $AppName successfully"



