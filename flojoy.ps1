Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Bypass

# Run all services required by Flojoy Studio

$success_color = 'Green'
$warning_color = 'Yellow'
$error_color = 'Red'
$info_color = 'Cyan'
$general_color = 'Magenta'
$info_mark = '👉'
$check_mark = '✔'
$alert_mark = '⚠️'
$error_mark = '❌'

$is_command_successful = 0

function success_msg {
  param (
    $message
  )
  Write-Host "$check_mark $message " -ForegroundColor $success_color
  Write-Host ""
}

function info_msg {
  param (
    $message
  )
  Write-Host "$info_mark $message " -ForegroundColor $info_color
  Write-Host ""
}

function warning_msg {
  param (
    $message
  )
  Write-Host "$alert_mark $message " -ForegroundColor $warning_color
  Write-Host ""
}

function error_msg {
  param (
    $message
  )
  Write-Host "$error_mark $message " -ForegroundColor $error_color
  Write-Host ""
  Write-Host ""
}

Write-Host ""
Write-Host ""
Write-Host "      ============================================================"  -ForegroundColor $general_color
Write-Host "     ||                  Welcome to Flojoy!                      ||" -ForegroundColor $general_color
Write-Host "     ||                                                          ||" -ForegroundColor $general_color
Write-Host "     ||         For Installation, Follow the Link Below          ||" -ForegroundColor $general_color
Write-Host "     ||       https://docs.flojoy.io/getting-started/install/    ||" -ForegroundColor $general_color
Write-Host "     ||                                                          ||" -ForegroundColor $general_color
Write-Host "      ============================================================" -ForegroundColor $general_color
Write-Host ""

$djangoPort = 8000
$initNodePackages = $true
$initPythonPackages = $true

# creating system links

function createSystemLinks {
  $FILE = Join-Path $PWD PYTHON/WATCH/STATUS_CODES.yml
  if (Test-Path $FILE) {
    info_msg "$FILE exists."
    $is_command_successful += $?
  }
  else {
    cmd /c mklink $FILE STATUS_CODES.yml
    $is_command_successful += $?
  }

  $FILE = Join-Path $PWD src/STATUS_CODES.yml
  if (Test-Path $FILE) {
    info_msg "$FILE exists."
    $is_command_successful += $?
  }
  else {
    cmd /c mklink $FILE STATUS_CODES.yml
    $is_command_successful += $?
  }
}

# Gives Feedback if the command run is successful or failed, if failed it exits the execution.

function feedback {
  param (
    $is_successful,
    $message,
    $help_message
  )
  if ($is_successful -eq $true) {
    success_msg $message
  }
  else {
    error_msg $help_message
    exit
  }
}

# Help function

function helpFunction {
  Write-Host ""
  Write-Host "Usage: $0 -n -p"
  Write-Host " -n: To not install npm packages"
  Write-Host " -p: To not install python packages"
  return 1 # Exit script after printing help
}

# Assign command-line arguments to a variable
$arguments = $args

# Parse command-line arguments
$index = 0
while ($arguments) {
  $key = $arguments[$index]
  switch ($key) {
    "-n" {
      $initNodePackages = $false
      $index = $index + 1
      continue
    }
    "-p" {
      $initPythonPackages = $false
      $index = $index + 1
      continue
    }
    "-P" {
      $djangoPort = $arguments[$index + 1]
      $index = $index + 2
      continue
    }
    default {
      Write-Host "Unknown option: $key"
      helpFunction
      exit 1
    }
  }
  if ($index -eq $arguments.Length) {
    break
  }
}

$CWD = $PWD

function createFlojoyDirectoryWithYmlFile {
  $FOLDER = "$HOME/.flojoy"
  $FILE = "$HOME/.flojoy/flojoy.yaml"
  if (Test-Path $FOLDER) {
    if (Test-Path $FILE) {
      info_msg "$FILE exists."
      Set-Content $FILE "PATH: $CWD"
      feedback $? "Updated file path in flojoy.yaml file." "Couldn't update file path in flojoy.yaml file, check the permission or sign in as root user"
    }
    else {
      info_msg "file flojoy.yaml in directory $FOLDER does not exist."
      New-Item $FILE -ItemType File | Out-Null
      Set-Content $FILE "PATH: $CWD"
      feedback $? "Successfully created flojoy.yaml file in $FOLDER directory." "Couldn't create flojoy.yaml file in $FOLDER directory, check the permission or sign in as root user"
    }
  }
  else {
    info_msg "directory ~/.flojoy/flojoy.yaml does not exist."
    New-Item -ItemType Directory $FOLDER | Out-Null
    New-Item $FILE -ItemType File | Out-Null
    Set-Content $FILE "PATH: $CWD"
    feedback $? "Created new $FOLDER directory with flojoy.yaml file." "Failed to create file in the home directory, check the permission or sign in as root user"
  }

  $CREDENTIALS_FILE = "$FOLDER/credentials"
  if (-not (Test-Path $CREDENTIALS_FILE)) {
    warning_msg " Warning: Credentials are not set for your project! You can set credentials by creating a file named 'credentials' in the directory '~/.flojoy' and adding your credentials to the file."
  }
  else {
    $FRONTIER_API_KEY_PATTERN = "FRONTIER_API_KEY:"
    $FRONTIER_API_KEY = Select-String $CREDENTIALS_FILE -Pattern $FRONTIER_API_KEY_PATTERN -Quiet
    if (-not $FRONTIER_API_KEY) {
      warning_msg " Warning: Frontier API key not set for your project! To set Frontier API key, simply follow this pattern in the '~/.flojoy/credentials' file: FRONTIER_API_KEY:<your key>"
    }
  }
}

createFlojoyDirectoryWithYmlFile

# Update submodules
& git submodule update --init --recursive > $null
feedback $? 'Updated submodules successfully' 'Failed to update submodules, check if git is installed correctly and configured with your github account.'


# Check if Python, Pip, or npm is missing.
. ./check-dependencies.ps1

# Call the function to check for dependencies
$missing_dependencies = check_dependencies

# If there are missing dependencies, print the list of them
if ($missing_dependencies) {
  error_msg "$missing_dependencies"
  exit 1
}


# Install Python packages

if ($initPythonPackages) {
  info_msg "Flag -p is not provided, Python packages will be installed from requirements.txt file"
  Set-Location $CWD
  & pip show pipwin 2>$1 > $null
  $is_installed = $LastExitCode
  if ($is_installed -ne 0) {
    $install_cmd = 'python -m pip install pipwin'
    Invoke-Expression $install_cmd 2>$1 | Out-Null
  }
  & python -m pipwin install matplotlib==3.5.2
  $pip_cmd = "python -m pip install -r requirements.txt"
  Invoke-Expression $pip_cmd
  feedback $? 'Python packages installed successfully!' "Python package installation failed! check error details printed above."
}

# Install Node packages

if ($initNodePackages) {
  info_msg "Argument -n is not provided, Node packages will be installed from package.json"
  & npm install
  feedback $? 'Installed Node packages successfully.' 'Node packages installation failed! check error details printed above.'
}


# update ES6 status codes file

& python -c 'import yaml, json; f=open("src/STATUS_CODES.json", "w"); f.write(json.dumps(yaml.safe_load(open("STATUS_CODES.yml", encoding="utf-8").read()), indent=4)); f.close();'

feedback $? 'Updated ES6 status codes file.' 'Failed to update ES6 status codes file, check if all required Python packages are installed. You can run this script without -p argument to install required Python packages automatically'

# creating system links

createSystemLinks

feedback $? 'Created symlinks successfully!' 'Creating symlinks failed, check your PYTHON/WATCH or src folder, maybe one of them is missing'

# jsonify python functions

& python write_python_metadata.py

feedback $? 'Jsonified Python functions and written to JS-readable directory' 'Error occurred while Jsonifying Python functions. Check errors printed above!'

# Generate Manifest

& python generate_manifest.py

feedback $? 'Successfully generated manifest for Python nodes to frontend' 'Failed to generate manifest for Python nodes. Check errors printed above!'

info_msg 'Checking if Memurai is running...'
& memurai-cli.exe ping 2>$1 > $null
$is_running = $LastExitCode

if ($is_running -eq 0) {
  success_msg 'Memurai is up and running...'
}
else {
  info_msg "Memurai is not running, trying to start Memurai service..."
  & memurai.exe --service-start > $null
  feedback $? 'Started Memurai successfully...' 'Failed to start Memurai. Please try running following command to start Memurai: "memurai.exe --service-start"'
}



# Start the Django server
$dir = $CWD
$wt_path = "wt.exe"
$cmd = "python write_port_to_env.py $djangoPort && python manage.py runserver $djangoPort"
$tab_args = "-d `"$dir`" cmd /c $cmd"
Start-Process -FilePath $wt_path -ArgumentList $tab_args
feedback $? "Starting Django server on port $djangoPort in a new tab..." 'Failed while starting Django server, check error detail printed above!'

# Check for rq-win package
& pip show rq-win 2>$1 > $null
$is_installed = $LastExitCode
if ($is_installed -ne 0) {
  info_msg 'Installing rq-win package to run RQ Worker on Windows...'
  $install_cmd = 'pip install git+https://github.com/michaelbrooks/rq-win.git#egg=rq-win'
  Invoke-Expression $install_cmd 2>$1 | Out-Null
  if ($LastExitCode -eq 0) {
    feedback $true 'Installed rq-win package successfully!' ''
  }
  else {
    feedback $false '' 'Failed to install rq-win package try running following command to install it manually: "pip install git+https://github.com/michaelbrooks/rq-win.git#egg=rq-win"'
  }
}


# Get RQ Worker script path

$python_scripts_path = & python .\get_script_dir.py
feedback $? 'Script path found for Python...' "Couldn't find script path for Python site-packages. Make sure you installed all required Python packages or run this script without -p argument to install packages automatically."
$rq_path = Join-Path $python_scripts_path "rqworker.exe"
$rq_script = "$rq_path -w rq_win.WindowsWorker"


# Initializing FLOJOY-WATCH RQ Worker
$dir = $CWD
$wt_path = "wt.exe"
$cmd = "$rq_script flojoy-watch"
$tab_args = "-d `"$dir`" cmd /c $cmd"
Start-Process -FilePath $wt_path -ArgumentList $tab_args
feedback $? 'Starting RQ worker for flojoy-watch in a new tab...' 'Starting RQ worker for flojoy-watch failed, check if ttab is installed (npx ttab) or check if rq worker is installed in your python package'


# Initializing Flojoy RQ Worker for nodes
$dir = Join-Path $CWD 'PYTHON'
$wt_path = "wt.exe"
$cmd = "$rq_script flojoy"
$tab_args = "-d `"$dir`" cmd /c $cmd"
Start-Process -FilePath $wt_path -ArgumentList $tab_args
feedback $? 'Starting RQ worker for nodes in a new tab...' 'Starting RQ worker for nodes failed, check if ttab is installed (npx ttab) or check if rq worker is installed in your python package'



# Initializing React Server

$dir = $CWD
$wt_path = "wt.exe"
$tab_args = "-d `"$dir`" cmd /c npm start"
Start-Process -FilePath $wt_path -ArgumentList $tab_args
feedback $? 'Starting React server on port 3000 in a new tab...' 'Could not start React server, check is npm installed in your local machine or run the script without -n flag to install the node packages'