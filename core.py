
# ██▓     ██▓ █    ██  ▒█████    ██████ 
# ▓██▒   ▒▓██▒ ██  ▓██▒▒██▒  ██▒▒██    ▒ 
# ▒██░   ▒▒██▒▓██  ▒██░▒██░  ██▒░ ▓██▄   
# ▒██░   ░░██░▓▓█  ░██░▒██   ██░  ▒   ██▒
# ░██████░░██░▒▒█████▓ ░ ████▓▒░▒██████▒▒
# ░ ▒░▓   ░▓  ░▒▓▒ ▒ ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░
# ░ ░ ▒  ░ ▒ ░░░▒░ ░ ░   ░ ▒ ▒░ ░ ░▒  ░  
#  ░ ░  ░ ▒ ░ ░░░ ░ ░ ░ ░ ░ ▒  ░  ░  ░  
#    ░    ░     ░         ░ ░        ░
#
# LiuOS Shell + Authentication
# 
# set some vars, I know this is bad Python practice.
IsFound = False
username = ""
currentdir = ""
ERROR_CODE = "UNKNOWN_ERROR"
should_crash = True
# Import
import http.client
import logging
import sys
import traceback
import os
try:
    FORMAT = '%(levelname)s | TIME - %(asctime)s | PROCESS - %(processName)s %(process)d | MSG - %(message)s'
    logging.basicConfig(filename='LiuOS.log', encoding='utf-8', level=logging.DEBUG, format=FORMAT)
except Exception as wpException:
    print(f"LiuOS cannot create/access the log file at {os.getcwd()}\\LiuOS.log.\n\nCheck to make sure you have write permissions to the folder you are in, that you have enough disk space, and make sure the directory you are in is mutable.\n\nIf the issue persists, your storage media could be full, write protected or failing.\n\nError from Python: {wpException.args}")
    sys.exit(1)
logging.debug("Imported traceback")
logging.debug("Imported sys")
logging.debug("Imported os")
logging.debug("Starting LiuOS")
import platform
try:
    import api
    logging.debug(f"Loaded LiuOS API {api.VerAPI}")
except:
    logging.fatal("Could not find/load the api module. Quitting!")
    print("LiuOS could not find the API library. Please make sure you have not deleted or renamed it and try again.")
    sys.exit(1)
import hashlib
logging.debug("Imported hashlib")
import getpass
logging.debug("Imported getpass")
try:
    import lang
    logging.debug(f"Loaded LiuOS {lang.CURRENT_LANG}")
except:
    logging.fatal("Could not find/load the lang module. Quitting!")
    print("LiuOS could not find the API library. Please make sure you have not deleted or renamed it and try again.")
    sys.exit(1)
try:
    import cred
    logging.debug("Imported cred.py")
except:
    logging.fatal("Could not find/load the cred module. Quitting.")
    print("LiuOS cannot load because you have a missing or damaged credential file. Run setup.py to fix the credential file.")

import cmd
logging.debug("Imported cmd")
import runpy
logging.debug("Imported runpy")
import time
logging.debug("Imported time")
try:
    from termcolor import colored
    logging.debug("Imported colored from termcolor")
except:
    print("The termcolor library could not be found. Please check that you have installed it.\n\nIf the library is not installed, please install it with \"python3 -m pip install termcolor\".")
    sys.exit(1)
# Some more vars
hostname_color = colored(f'{cred.loginname}@{lang.hostname}-LiuOS', 'light_green')
currentdir = os.getcwd()
dir_color = colored(f'{currentdir}', 'light_blue')

# Easter egg, now in your logs!
if lang.result != "":
    logging.info(lang.result)

# Our shell class
class LiuShell(cmd.Cmd):
    
    intro = lang.OS_NAME_SPLASH
    prompt = f"{hostname_color}:{dir_color}$ "
    file = None
    doc_header = lang.HELP_HEADER
    # a function to do nothing
    def emptyline(self):
        pass

    def default(self, line):
        print(f"{line}: {lang.COMMAND_NOT_FOUND}")
    # ----- LiuOS Shell commands -----
    def do_runcmd(self, arg):
        'Runs the host shell command specified. Ex: runcmd echo'
        logging.info("Running command using runcmd in shell")
        os.system(arg)
    def do_runline(self, arg):
        'Runs the Python line specified. Ex: runline print("hello")'
        logging.info("Running Python code using runline in shell")
        arghash = hashlib.sha1(arg.encode())
        argbyte = arghash.hexdigest()
        if arghash == "2fc7f1452374b6e341d67717f032abbe0da0f4a6":
            raise Exception("debug crash")
        else:
            try:
                res = exec(arg)
                print(str(res))
            except Exception as e:
                print(f"Error while trying to execute {arg}: {e}")
                conformationexec = input(lang.EXCEPTION_RUNLINE_TRY_AGAIN)
                if conformationexec == "y":
                    exec(arg)
                else:
                    return
    def do_run(self, arg):
        'Runs the core.py file in the folder specified, it must be in the programs dir in the same dir as LiuOS and exist. Ex: run eteled'
        logging.info(f"Running Python file using run in shell")
        # try:
        runpy.run_path(path_name=f"programs/{arg}/core.py")
        # except: 
            # print(f"{arg} {lang.PROG_HAS_CRASHED}")
    def do_changecred(self, arg):
        'Allows you to set up or change your login credentials.'
        # Use the new elevation call in the LiuOS API
        elevation = api.elevateSession("org.LiuWoodsCode.LiuOS.changecred", "Change Credentials", "LiuWoodsCode", False, True, "Change your LiuOS username and/or password")
        logging.info("Changing login")
        # Asks for username
        if elevation: 
            setusr = input(lang.ENTER_USERNAME_CREATION)
            if setusr == "":
                setusr = "username"
        # Ask for password
            setpass = getpass.getpass(lang.ENTER_PASSWD_CREATION)
            if setpass == "":
                raise Exception("No password supplied")
            if setpass == "password":
                logging.error("Password cannot be set to \"password\" as it is insecure.")
                print(lang.PASSWORD_CANNOT_PASSWORD)
                setpass = "liuos"
            bytehash1 = hashlib.sha3_512(setpass.encode())
            pwdreshash1 = bytehash1.hexdigest()
            content = f"""loginname = \"{setusr}\"
loginpass = \"{pwdreshash1}\""""
            file_path = "cred.py"  # Replace with the actual file path
            with open(file_path, 'w') as file:
                file.write(content)
            print("Credentials saved. LiuOS will exit.")
            exit()
        else:
            print(lang.CHANGECRED_ELEVATION_FAILED)
    def do_logout(self, arg):
        'Closes the shell. Ex: logout'
        logging.warning("Logging out shell session")
        print(lang.LOGGING_OUT)
        # We just close the shell connection
        self.close()
        return True
    def do_shutdown(self, arg):
        'Shuts down the system. May require appropriate low level OS permissions. Ex: shutdown'
        confirm = input(lang.SHUTDOWN_WARNING)
        if confirm == "Y":
            logging.info("Shut down using shell command")
            system_platform = platform.system()
            if system_platform == 'Linux':
                os.system('sudo shutdown now')
            elif system_platform == 'Windows':
                os.system('shutdown /s /t 1 /d "LiuOS initiated shutdown"')
            elif system_platform == 'Darwin':  # MacOS
                os.system('sudo shutdown now')
            else:
                raise OSError("Unsupported operating system")
        else:
            pass
    def do_exit(self, arg):
        'Closes the shell, and quits the script. Ex: exit'
        print(lang.LOGGING_OUT)
        logging.info("Shut down using shell command")
        # We just run the exit() function, like what you call in the Python she;;
        exit()

    # ----- ChatGPT Generated Commands
    def do_webget(self, arg):    
        'Makes a web request Can only use HTTPS if Python was compiled with SSL/TLS support. Ex: webget https://www.apple.com'
        conn = http.client.HTTPSConnection(arg)
        conn.request("GET", "/")
        res = conn.getresponse()
        data = res.read()
        print(data.decode("utf-8"))
        conn.close()
    def do_ver(self, arg):
        "Shows version info"
        verhash = hashlib.sha512(arg.encode())
        eggreshash = verhash.hexdigest()
        # an easter egg
        if eggreshash == "cce4f1f446e397677f525ade22c85bfc8737da9c7606d10d67802aa6513137e46a83ab46a480e6bcc4044b6080b4f3bab112841d2b949e49c4006718ce231c11":
            print("Thanks for the complement!. I'm just a solo developer and really appreciate it!")
        else:
            # all we do is print the var in the language pack
            print(lang.VersionOutput)
    def do_ls(self, arg='.'):
        'Lists files in either the current directory, or a specified directory. Ex: ls /home/eteled/Python'
        if arg == "":
         lsout = os.listdir(".")
         lsout.sort()  # Sort the list alphabetically
	
         for file_name in lsout:
           print(file_name)
        else:
         lsout = os.listdir(arg)
         lsout.sort()  # Sort the list alphabetically
	
         for file_name in lsout:
           print(file_name)

    def do_pwd(self, arg):
        'Displays your current directory. Ex: pwd'
        print(os.getcwd())

    def do_cd(self, arg):
        'Changes directory. Ex: cd programs'
        # we need the current directory
        currentdir = os.getcwd()
        for name in os.listdir(currentdir):
            # might make this more accurate to the linux cd command that is case sensitive
            if name.lower() == arg:
                # found the directory
                dir_path = os.path.join(currentdir, name)
                os.chdir(dir_path)
                IsFound = True
            else:
                # tries to see if you have 2 or 3 dots, and if so just sends you back 1 directory
                # doesn't work with more dots. Too bad! 
                if arg == "..":
                   dir_path = os.path.join(currentdir, "..")
                   os.chdir(dir_path)
                elif arg == "...":
                   dir_path = os.path.join(currentdir, "..")
                   os.chdir(dir_path) 
                else: 
                   logging.info("Dir not found")
        # Set the hostname and current directory
        hostname_color = colored(f'{cred.loginname}@{lang.hostname}-LiuOS', 'light_green')
        currentdir = os.getcwd()
        dir_color = colored(f'{currentdir}', 'light_blue')
        # actually set the prompt
        self.prompt = f"{hostname_color}:{dir_color}$ "

    def do_cp(self, arg):
        'Copies a file specified in input fields when this command is run. Ex: cp'
        # too lazy to work with arg for this
        src = input(lang.SOURCE_FILE)
        dst = input(lang.DEST_FILE)
        # all we do is just write the contents to the file
        # this could introduce an issue if the file already exists
        with open(src, 'r') as f_src:
            with open(dst, 'w') as f_dst:
                f_dst.write(f_src.read())

    def do_mv(self, arg):
        'Moves a file specified in input fields when this command is run. Ex: mv'
        # just cp but deletes the file after
        src = input(lang.SOURCE_FILE)
        dst = input(lang.DEST_FILE)
        with open(src, 'r') as f_src:
            with open(dst, 'w') as f_dst:
                f_dst.write(f_src.read())
        os.remove(src)

    def do_rm(self, arg):
        'Removes the file or folder with the specified path. Ex: rm /home/serialkiller/murder/knife.jpg'
        # all we do is call the remove function
        os.remove(arg)
        
    def do_clear(self, arg):
        'Clears the screen'
        # detects NT and uses the "cls" command, otherwise use "clear"
        os.system('cls' if os.name == 'nt' else 'clear')


    # ----- record and playback -----'
    # just the rec / play functions from the turtle with cmd demo
    # this is kinda like .bat files on Windows systems but for LiuOS
    # i don't even know if this works
    def do_savecmd(self, arg):
        'Save future commands to filename. Ex: savecmd rose.cmd'
        self.file = open(arg, 'w')
    def do_opencmd(self, arg):
        'Playback commands from a file. Ex: opencmd rose.cmd'
        print(lang.CONFORM_RUN_FILE)
        conformation = input()
        if conformation == "yes":
            self.close()
            with open(arg) as f:
                self.cmdqueue.extend(f.read().splitlines())
        elif conformation == "y":
            self.close()
            with open(arg) as f:
                self.cmdqueue.extend(f.read().splitlines())
        else:
            return
    def precmd(self, line):
        line = line
        if self.file and 'playback' not in line:
            print(line, file=self.file)
        return line
    def close(self):
        if self.file:
            self.file.close()
            self.file = None

def parse(arg):
    'Convert a series of zero or more numbers to an argument tuple'
    return tuple(map(int, arg.split()))
# Counter
attemps = 0

def actualsys() :
        logging.debug("Launched main system")
        os.system('cls' if os.name == 'nt' else 'clear')
        logging.debug("Loaded LiuOS Shell")
        LiuShell().cmdloop()
logging.debug("Assigned main system function")
def run_liuos_system():
    # just a GHA check to bypass input() and
    if os.environ.get('GITHUB_ACTIONS') == "true":
        logging.info('Running on GitHub Actions, not using the LiuOS Shell')
        print(lang.ENTER_USERNAME_LOGIN)
        print(lang.ENTER_PASSWD_LOGIN)
        print(lang.FAKE_SUCCESSFUL_LOGIN)
        logging.warning("Fake login completed")
        print(lang.SHELL_INTRO)
        print("LiuOS: pwd")
        # get the current directory
        LiuShell().do_pwd("test")
        print("LiuOS: ls")
        # run directory listing
        LiuShell().do_ls()
        print("Output from an echo command:")
        # runs a system command
        LiuShell().do_runcmd("echo Hello World")
        print("Sample strings:")
        print(lang.SAMPLE_ABC)
        print(lang.SAMPLE_STRING)
        # loads a test program
        TestProg = "programs/helloworld/core.py"
        logging.debug("Launching test program")
        runpy.run_path(path_name=TestProg)
        print("Code completed")
    else:
        # Authentication system
        os.system('cls' if os.name == 'nt' else 'clear')
        print(lang.OS_NAME_LOGIN)
        # detect if the cred has not been changed
        # this is just the hash of the word "password"
        # this will fail if the user sets their password to "password". Too bad!
        if cred.loginpass == "e9a75486736a550af4fea861e2378305c4a555a05094dee1dca2f68afea49cc3a50e8de6ea131ea521311f4d6fb054a146e8282f8e35ff2e6368c1a62e909716":
            # warn the user
            print(lang.CHANGE_CREDENTIAL_ALERT)
        crash_times = 0
        attempts = 0
        # make it so that this has 6 attempts
        while attempts < 7:
            try:
                # ask for the user's creds
                username = input(lang.ENTER_USERNAME_LOGIN)
                logging.debug(f'Entered username {username}')
                password = getpass.getpass(lang.ENTER_PASSWD_LOGIN)
                logging.debug('Entered password')
                # hash the password
                bytehash = hashlib.sha3_512(password.encode())
                pwdreshash = bytehash.hexdigest()
                logging.debug('Generated hash of password')
                if attempts == 6:
                    # Brute force protection
                    logging.fatal("6 or more incorrect credentials entered")
                    ERROR_CODE = "CRED_FORCE_ERROR"
                    # just raise an exception
                    raise Exception(lang.BRUTE_FORCE_CRASH)
                if os.environ.get('GITHUB_ACTIONS') == "true":
                    logging.warning("Running on Github Actions")
                    actualsys()
                elif username == cred.loginname and pwdreshash == cred.loginpass: # using modules is easier to use, but not very versitile
                    print(lang.SUCCESSFUL_LOGIN)
                    logging.debug('Correct login credentials, logged in')
                    # clears the password variable so that a debugger can't sniff the input after login
                    # this doesn't help if you literally set your password to "FuckShinjiAoba"
                    # #PrayForKyoAni
                    password = "FuckShinjiAoba"
                    # makes the hash and the password match up
                    pwdreshash = "8897d5a6fbee6c827ee6d2ba200c276d2597736760ee78b954d32b5b5c4c7f4bd2126762d39d9e938093ad44f7d93485165d1ac6e4a9ad18ad68f6fa69e8184e"
                    actualsys()
                else:
                    print(lang.INCORRECT_LOGIN)
                    logging.error("Incorrect login credentials")
                    attempts += 1
                    continue
            except Exception as e:
                os.system('cls' if os.name == 'nt' else 'clear')    
                error_code = 0
                trace = traceback.format_exc()
                error_description = str(e)
                error_code = hash(error_description)
                error_code_str = str(error_code)
                error_description = f"0x{error_code_str.replace('-', '')}"
                # error message to be displayed on exception
                print(f'\n;(\nA fatal error has occurred causing an exception. LiuOS has stopped to prevent data corruption or other issues.\n\nError code: {error_description}\n\nDescription of error: {e}')
                if should_crash:
                    # Check if we need to show extra info about repeated exceptions
                    if crash_times == 1:
                        print("\nNote: LiuOS has crashed more than once in this Python instance. \nTo attempt to fix the issue, try restarting Python. \nIf the bugcheck reoccurs, file a bug report with the traceback in your LiuOS.log file.\n")
                    if lang.IsDebug:
                        print(f"\n{trace}")
                    FORMAT = 'CRASH | TIME - %(asctime)s | PROCESS - %(processName)s %(process)d | MSG - %(message)s'
                    logging.basicConfig(filename='LiuOS.log', encoding='utf-8', level=logging.DEBUG, format=FORMAT)
                    crashlog = f"Crashed with code {error_description}"
                    logging.fatal(f"Code: {error_description}.\n {trace}")
                    print("System will reset in 15 sec!")
                    time.sleep(15)
                    FORMAT = '%(levelname)s | TIME - %(asctime)s | PROCESS - %(processName)s %(process)d | MSG - %(message)s'
                    logging.basicConfig(filename='LiuOS.log', encoding='utf-8', level=logging.DEBUG, format=FORMAT)
                    attempts = 0
                    error_code = ""
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f"LiuOS {api.VerLiuOS}\nInfo: System recovered from bugcheck {error_description}")
                    error_description = ""
                    crash_times = 1
                else:
                    print("WARN: Crash Bypass")
                    
if __name__ == "__main__":
    IsUsingAPI = False
    run_liuos_system()
else:
    if __name__ == "core":
        print("Info: LiuOS Shell is being used by a LiuOS program")
    else:
        print(f"Warning: LiuOS is being used as a module by {__name__}\nNote: If it's being used by \"core\", then it's being used in a LiuOS program.")
    logging.warning(f"LiuOS should not be used as a Python module ")
