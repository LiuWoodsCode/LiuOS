import platform
import api
import socket
hostname = socket.gethostname()
python = platform.python_version()
lowlevelos = platform.platform()
## English Language for LiuOS
CURRENT_LANG = "EngUS"
LANG_VER = 1.5
CURRENT_LONG_LANG = "English (US)"
# Authentication
ENTER_USERNAME_LOGIN = "Enter your username: "
ENTER_PASSWD_LOGIN = "Enter your password: "
INCORRECT_LOGIN = "Incorrect credentials. Check your Caps Lock and locale settings and try again."
SUCCESSFUL_LOGIN = "Logging in..."
FAKE_SUCCESSFUL_LOGIN = "[FAKE LOGIN] Logging in..."
BRUTE_FORCE_CRASH = "Too many attempted passwords."
# Global strings that can be multi-purpose
SOURCE_FILE = "Source File"
DEST_FILE = "Destination File"
# Test strings used for GitHub Actions testing
SAMPLE_ABC = "EngUS - ABCDEFGHIJKLNOPQRSTUVWXYZabcdefghijklnopqustuvwxyz1234567890!@#$%^&*()-=[]\{}|;':,./<>?"
SAMPLE_STRING = "Henry Morris = Eteled"
# LiuOS Shell
SHELL_PROMPT = "LiuOS $ "
SHELL_INTRO = f"LiuOS Shell, running on kernel version Python {python}.\nType help or ? to list available commands.\n"
# Commands 
# Version
VersionOutput = f"LiuOS {api.VerLiuOS}\nLiuOS API {api.VerAPI}\nLiuOS Language Pack {CURRENT_LANG} {LANG_VER}\n---------------------\nKernel (Python) version: {python}\nLow level OS: {lowlevelos}"
# WebGet
CHECK_LOG = "Request output saved to your log file."
# Shut Down
LOGGING_OUT = "Logging out..."
