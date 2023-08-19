

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

# Function to check if the script is running with administrative privileges
function Test-AdminPrivileges {
    $isAdmin = ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator")
    if (-not $isAdmin) {
        Write-Host "Please run this script as an administrator."
        exit
    }
}

# Function to add a directory to the system-wide PATH
function Add-DirectoryToPath {
    param (
        [string]$DirectoryPath
    )
    
    # Check if the directory is already in the PATH
    $existingPath = [System.Environment]::GetEnvironmentVariable("Path", [System.EnvironmentVariableTarget]::Machine)
    
    if ($existingPath -notlike "*$DirectoryPath*") {
        # Add the directory to the PATH
        [System.Environment]::SetEnvironmentVariable("Path", "$existingPath;$DirectoryPath", [System.EnvironmentVariableTarget]::Machine)
        Write-Host "Added $DirectoryPath to the system-wide PATH."
    } else {
        Write-Host "$DirectoryPath is already in the system-wide PATH."
    }
}



# Define the directory containing your application
$AppName = "openai-client"
$AppDirectory = "C:\Program Files\openai-client"  # Change to your actual directory
$Uri = "https://github.com/anirbandey1/openai-client/releases/download/v1.0.0/openai-client.exe"
$Dest = "openai-client.exe"


# Check for administrative privileges
Test-AdminPrivileges

# Download
Invoke-WebRequest -Uri  $Uri -OutFile $Dest


# Check if the directory already exists
if (-not (Test-Path -Path $DirectoryPath -PathType Container)) {
    # Create the directory
    New-Item -Path $DirectoryPath -ItemType Directory
    Write-Host "Created directory: $DirectoryPath"
} else {
    Write-Host "Directory $DirectoryPath already exists."
}

# Add the directory to the system-wide PATH
Add-DirectoryToPath -DirectoryPath $AppDirectory

$SourceFile = $Dest
$DestinationDirectory = $AppDirectory


Copy-Item -Path $SourceFile -Destination $DestinationDirectory -Force
Write-Host "Copied $SourceFile to $DestinationDirectory."


Write-Host "Installed $AppName successfully"



