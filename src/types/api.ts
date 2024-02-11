export enum API {
  checkPythonInstallation = "CHECK_PYTHON_INSTALLATION",
  installPipx = "INSTALL_PIPX",
  pipxEnsurepath = "PIPX_ENSUREPATH",
  installPoetry = "INSTALL_POETRY",
  installDependencies = "INSTALL_DEPENDENCIES",
  getPoetryVenvExecutable = "GET_POETRY_EXECUTABLE",
  spawnCaptain = "SPAWN_CAPTAIN",
  killCaptain = "KILL_CAPTAIN",
  openLogFolder = "OPEN_LOG_FOLDER",
  restartFlojoyStudio = "RESTART_STUDIO",
  setUnsavedChanges = "SET_UNSAVED_CHANGES",
  statusBarLogging = "STATUSBAR_LOGGING",
  setPythonInterpreter = "SET_PY_INTERPRETER",
  writeFileSync = "WRITE_FILE_SYNC",
  showSaveDialog = "SHOW_SAVE_DIALOG",
  browsePythonInterpreter = "BROWSE_PY_INTERPRETER",
  sendLogToStatusbar = "SEND_LOG_TO_STATUSBAR",
  listPythonPackages = "LIST_PYTHON_PACKAGES",
  pyvisaInfo = "PYVISA_INFO",
  ping = "PING",
  netstat = "NETSTAT",
  ifconfig = "IFCONFIG",
  downloadLogs = "DOWNLOAD_LOGS",
  checkForUpdates = "CHECK_FOR_UPDATES",
  restartCaptain = "RESTART_CAPTAIN",
  pickDirectory = "PICK_DIRECTORY",
  getCustomBlocksDir = "GET_CUSTOM_BLOCKS_DIR",
  cacheCustomBlocksDir = "CACHE_CUSTOM_BLOCKS_DIR",
  poetryShowTopLevel = "POETRY_SHOW_TOP_LEVEL",
  poetryGetGroupInfo = "POETRY_GET_GROUP_INFO",
  poetryInstallDepGroup = "POETRY_INSTALL_DEP_GROUP",
  poetryUninstallDepGroup = "POETRY_UNINSTALL_DEP_GROUP",
  openFilePicker = "OPEN_FILE_PICKER",
  openEditorWindow = "OPEN_EDITOR_WINDOW",
  loadFileFromFullPath = "LOAD_FILE_FROM_FULL_PATH",
  saveFileToFullPath = "SAVE_FILE_TO_FULL_PATH",
  setupExecutionTime = "SETUP_EXEC_TIME",
  isCI = "IS_CI",
  getAllLogs = "GET_ALL_LOGS",
  openLink = "OPEN_LINK",
  openTestPicker = "OPEN_TEST_PICKER",
  // Authentication
  getUserProfiles = "GET_USER_PROFILES",
  setUserProfile = "SET_USER_PROFILE",
  setUserProfilePassword = "SET_USER_PROFILE_PASSWORD",
  validatePassword = "VALIDATE_PASSWORD",
  createUserProfile = "CREATE_USER_PROFILE",
  deleteUserProfile = "DELETE_USER_PROFILE",
}
