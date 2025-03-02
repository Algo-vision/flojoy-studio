
# Dev environement installation

1. ### Install Scoop For windows
```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression
```

2. ### Python 3.11 Installation 
Install Python 3.11 using Scoop.

In a new terminal run: 
```
scoop bucket add versions
scoop install versions/python311
```

3. ### Install PIPX

```
pip3 install pipx
pipx ensurepath
    
```
4. ### Install Poetry
```
pipx install poetry
```
5. ### Install GIT
```
scoop bucket add main
scoop install main/git
```
6. ### Install NodeJs and PNPM using FNM
Install FNM:
```
scoop install main/fnm
Add-Content -Path $PROFILE -Value "fnm env --use-on-cd | Out-String | Invoke-Expression"
```

Restart PowerShell and run:

```
fnm install 22
```

Now install PNPM package manager:

```
corepack enable pnpm
```

Run `pnmp` and select download.

7. ### Clone repo 
```
mkdir $env:USERPROFILE\repos
cd $env:USERPROFILE\repos
git clone https://github.com/Algo-vision/flojoy-studio.git

```

8. ### Install project poetry python environement:

```
cd $env:USERPROFILE\repos\flojoy-studio
# Install project dependencies but not the current project as python site-package, because we want to import it from the source in the repo when debugging.
poetry install --no-root
```

9. ### Install NodeJS dependencies

```
cd $env:USERPROFILE\repos\flojoy-studio

pnpm install
```
10. ### Install vscode

```
scoop bucket add extras
scoop install extras/vscode
```

Make Sure to install Python extension

11. Inside VSCode, select python interpreter to be th one poetry installed under the repo derectory in `.venv`

### Now you will be able to debug everything.

First, launch the debug configuration "FastAPI Debug" and after the backend service has started , launch "Debug Main Process" in order to launch the main Electron GUI process and debug it.
