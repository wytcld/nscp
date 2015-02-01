
BREAKPAD_FOUND = "${BREAKPAD_FOUND}"
BREAKPAD_DUMPSYMS_EXE = "${BREAKPAD_DUMPSYMS_EXE}"
BUILD_TARGET_EXE_PATH = "${BUILD_TARGET_EXE_PATH}"
BUILD_PYTHON_FOLDER = "${BUILD_PYTHON_FOLDER}"
VERSION = "${VERSION_SERIES}.${VERSION_MAJOR}.${VERSION_MINOR}"
CMAKE_CL_64 = "${CMAKE_CL_64}"
ARCHIVE_FOLDER = "${ARCHIVE_FOLDER}"
VERSION_TXT = "${VERSION_TXT}"
VERSION_ARCH = "${VERSION_ARCH}"
TARGET_SITE = "${TARGET_SITE}"
CMAKE_SOURCE_DIR  = "${CMAKE_CURRENT_SOURCE_DIR}"
SCP_BINARY = 'c:\Progra~2\PuTTY\pscp.exe' # ${PSCP_EXE}
CREDENTIALS_FILE = "${BUILD_TARGET_EXE_PATH}/../credentials.txt"

#if CMAKE_CL_64 != "0": # Due to bug in x64 dump_symbols (or possible windows API)
#	BREAKPAD_FOUND = "FALSE"
