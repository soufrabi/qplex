

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




# ref : https://gist.github.com/mkropat/c1226e0cc2ca941b23a9

function Add-EnvPath {
    param(
        [Parameter(Mandatory=$true)]
        [string] $Path,

        [ValidateSet('Machine', 'User', 'Session')]
        [string] $Container = 'Session'
    )

    if ($Container -ne 'Session') {
        $containerMapping = @{
            Machine = [EnvironmentVariableTarget]::Machine
            User = [EnvironmentVariableTarget]::User
        }
        $containerType = $containerMapping[$Container]

        $persistedPaths = [Environment]::GetEnvironmentVariable('Path', $containerType) -split ';'
        if ($persistedPaths -notcontains $Path) {
            $persistedPaths = $persistedPaths + $Path | where { $_ }
            [Environment]::SetEnvironmentVariable('Path', $persistedPaths -join ';', $containerType)
        }
    }

    $envPaths = $env:Path -split ';'
    if ($envPaths -notcontains $Path) {
        $envPaths = $envPaths + $Path | where { $_ }
        $env:Path = $envPaths -join ';'
    }
}

function Remove-EnvPath {
    param(
        [Parameter(Mandatory=$true)]
        [string] $Path,

        [ValidateSet('Machine', 'User', 'Session')]
        [string] $Container = 'Session'
    )

    if ($Container -ne 'Session') {
        $containerMapping = @{
            Machine = [EnvironmentVariableTarget]::Machine
            User = [EnvironmentVariableTarget]::User
        }
        $containerType = $containerMapping[$Container]

        $persistedPaths = [Environment]::GetEnvironmentVariable('Path', $containerType) -split ';'
        if ($persistedPaths -contains $Path) {
            $persistedPaths = $persistedPaths | where { $_ -and $_ -ne $Path }
            [Environment]::SetEnvironmentVariable('Path', $persistedPaths -join ';', $containerType)
        }
    }

    $envPaths = $env:Path -split ';'
    if ($envPaths -contains $Path) {
        $envPaths = $envPaths | where { $_ -and $_ -ne $Path }
        $env:Path = $envPaths -join ';'
    }
}

function Get-EnvPath {
    param(
        [Parameter(Mandatory=$true)]
        [ValidateSet('Machine', 'User')]
        [string] $Container
    )

    $containerMapping = @{
        Machine = [EnvironmentVariableTarget]::Machine
        User = [EnvironmentVariableTarget]::User
    }
    $containerType = $containerMapping[$Container]

    [Environment]::GetEnvironmentVariable('Path', $containerType) -split ';' |
        where { $_ }
}

# Export-ModuleMember -Function *



### Main
function Main {

# Define the directory containing your application
$AppName = "openai-client"
$ExeName = "openai-client.exe"
$Author = "anirban"
$AuthorDirectory = "C:\Program Files\${Author}"  # Change to your actual directory
$BinDirectory = "C:\Program Files\${Author}\Bin"  # Change to your actual directory
$AppDirectory = "C:\Program Files\${Author}\Apps\${AppName}"  # Change to your actual directory

$Uri = "https://github.com/anirbandey1/openai-client/releases/download/v1.0.0/openai-client.exe"
$Dest = "openai-client.exe"


# Check for administrative privileges
Test-AdminPrivileges


# Delete Existing App
Remove-Item -LiteralPath "$AppDirectory"  -Force -Recurse
Remove-Item -LiteralPath "$BinDirectory\$ExeName"  -Force 

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
Add-EnvPath $BinDirectory

New-Item -ItemType SymbolicLink -Path "$BinDirectory\$ExeName" -Target "$AppDirectory\$ExeName" 

Write-Host "Installed $AppName successfully"

}

Main


