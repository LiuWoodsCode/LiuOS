import platform
import api
import socket
import random
import datetime
import logging
build_add = "07-21-23"
logging.info(f"Build date: {build_add}")
logging.info(f"API Version: {api.VerAPI}")
logging.info(f"LiuOS Version: {api.VerLiuOS}")

def set_fuckspez_remark():
    # Get the current date
    today = datetime.date.today()
    
    # Define the chances of each case
    chance_normal = 1 / 50
    chance_special = 1 / 7

    # Check if it's July 1st
    is_july_1st = today.month == 7 and today.day == 1

    # Check if it's a special day (July 1st)
    if is_july_1st:
        if random.random() < chance_special:
            variable = "RIP, Apollo for Reddit - "
        else:
            variable = None
    else:
        # Check for the normal case
        if random.random() < chance_normal:
            variable = "fuck u/spez - "
        else:
            variable = None

    if variable == None:
        variable = ""

    return variable

# Test the function
result = set_fuckspez_remark()

IsDebug = False
IsInternal = False
from termcolor import colored
def get_release_channel() :
    if IsInternal:
        return "Debug"
    else:
        return "Production"
hostname = socket.gethostname()
hostname_color = colored(f'Hello, World!', 'green', attrs=['reverse', 'blink'])
python = platform.python_version()
lowlevelos = platform.platform()
## English Language for LiuOS
CURRENT_LANG = "EngUS"
LANG_VER = 2.0
CURRENT_LONG_LANG = "English (US)"
# Authentication
# Do not translate - ASCII Art
LINE1 =  colored(f'██▓     ██▓ █    ██  ▒█████    ██████ ', 'blue')
LINE4 =  colored(f'▓██▒   ▒▓██▒ ██  ▓██▒▒██▒  ██▒▒██    ▒ ', 'cyan')
LINE2 = colored(f'▒██░   ▒▒██▒▓██  ▒██░▒██░  ██▒░ ▓██▄   \n', 'magenta')
LINE3 = colored(f'▒██░   ░░██░▓▓█  ░██░▒██   ██░  ▒   ██▒\n░██████░░██░▒▒█████▓ ░ ████▓▒░▒██████▒▒\n░ ▒░▓   ░▓  ░▒▓▒ ▒ ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░\n░ ░ ▒  ░ ▒ ░░░▒░ ░ ░   ░ ▒ ▒░ ░ ░▒  ░  \n  ░ ░  ░ ▒ ░ ░░░ ░ ░ ░ ░ ░ ▒  ░  ░  ░  \n    ░    ░     ░         ░ ░        ░', 'light_magenta')
# Ok, now continue.
OS_NAME_LOGIN = f"\n{LINE1}\n{LINE4}\n{LINE2}{LINE3}\n\n{result}{colored(f'LiuOS {api.VerLiuOS} by LiuWoodsCode', 'cyan')}\n"
CHANGE_CREDENTIAL_ALERT = "You have not set up user credentials. The default username is \"username\", and the password is \"password\".\nWhen you log in, run the \"changecred\" command to change the username and password."
ENTER_USERNAME_CREATION = "Enter a username, keep blank to use \"username\": "
ENTER_PASSWD_CREATION = "Enter a password: "
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
SHELL_INTRO = f"LiuOS {api.VerLiuOS}, running on kernel version Python {python}.\nType help or ? to list available commands.\n"
HELP_HEADER = f"LiuOS commands in this current build ({api.VerLiuOS}). Type \"help (command)\" for details about a command."
COMMAND_NOT_FOUND = "command not found"
# Commands 
# Change Credentials
CHANGECRED_ELEVATION_FAILED = "LiuOS cannot change your credentials without elevation."
# Version
OS_NAME_LOGO= f"\n{LINE1}\n{LINE4}\n{LINE2}{LINE3}"
VersionOutput = f"LiuOS {api.VerLiuOS}\nLiuOS API {api.VerAPI}\nLiuOS Language Pack {CURRENT_LANG} {LANG_VER}\nRelease Type: {get_release_channel()}\n-----------------------\nKernel (Python) version: {python}\nLow level OS: {lowlevelos}"
# WebGet
CHECK_LOG = "Request output saved to your log file."
# Shut Down
LOGGING_OUT = "Logging out..."
# Updates - For future use
UPDATECORE_RECOVERY = "recovery"
RECOVERY_MODE_WARN = "You are entering recovery mode. LiuWoodsCode is not responsible for any damage caused in Recovery Mode. Continue at your own risk."
UPDATING_MSG = "Updating LiuOS..."
RECOVERY_START = "Starting LiuOS Recovery..."
# Safety
CONFORM_RUN_FILE = colored(f'You are about to run a command file.\n This could contain Shell/CMD/PowerShell commands or Python code that could be dangerous.\n\nARE YOU SURE YOU WANT TO RUN THE COMMANDS IN THIS FILE?', 'red')
EXCEPTION_RUNLINE_TRY_AGAIN = "Would you like to try again without the crash handler? Answer with either y or n: "
SHUTDOWN_WARNING = "Do you really want to shut down? \n\nY = Yes\nN = No"
PASSWORD_CANNOT_PASSWORD = "Your password cannot be set to \"password\" as is included with the default configuration. Attempting to do so will make the login MOTD think that you have not set new credentials.\n\nYour password has been set to \"liuos\""
# Crash handler
PROG_HAS_CRASHED = "has crashed. Please consult the developer for more information. At least it isn't as bad as Shinji Aoba!"
OS_NAME_SPLASH= f"\n{LINE1}\n{LINE4}\n{LINE2}{LINE3}\n\n{SHELL_INTRO}"
