# import stuff
username = ""
crash_times = 0
ERROR_CODE = "UNKNOWN_ERROR"
should_crash = True
import http.client
import logging
FORMAT = '%(levelname)s | TIME - %(asctime)s | PROCESS - %(processName)s %(process)d | MSG - %(message)s'
logging.basicConfig(filename='LiuOS.log', encoding='utf-8', level=logging.DEBUG, format=FORMAT)
logging.debug("Created logging config")
import api
logging.debug(f"Loaded LiuOS API {api.VerAPI}")
import hashlib
logging.debug("Imported hashlib")
import getpass
logging.debug("Imported getpass")
import lang
logging.debug(f"Loaded LiuOS {lang.CURRENT_LANG}")
import cred
logging.debug("Imported cred.py")
import os
logging.debug("Imported os")
import sys
logging.debug("Imported sys")
import cmd
logging.debug("Imported cmd")
import runpy
logging.debug("Imported runpy")
import time
import traceback

class LiuShell(cmd.Cmd):
    
    intro = lang.SHELL_INTRO
    prompt = f"{cred.loginname}@{lang.hostname}-LiuOS $ "
    file = None

    # ----- LiuOS Shell commands -----
    def do_runcmd(self, arg):
        'Runs the host shell command specified. Ex: runcmd echo'
        logging.info("Running command using runcmd in shell")
        os.system(arg)
    def do_runline(self, arg):
        'Runs the Python line specified. Ex: runline print("hello")'
        logging.info("Running Python code using runline in shell")
        exec(arg)
    def do_run(self, arg):
        'Runs the script specified, it must be in the programs dir in the same dir as LiuOS and exist, or Python will crash. Ex: run eteled.py'
        logging.info(f"Running Python file using run in shell")
        runpy.run_path(path_name="programs/{arg}")
    def do_logout(self, arg):
        'Closes the shell. Ex: logout'
        logging.warning("Logging out shell session")
        print(lang.LOGGING_OUT)
        self.close()
        return True
    def do_shutdown(self, arg):
        'Closes the shell, and quits the script. Ex: shutdown'
        print(lang.LOGGING_OUT)
        logging.info("Shut down using shell command")
        exit()
        return True
    def do_exit(self, arg);
        do_shutdown

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
        print(lang.VersionOutput)
    def do_ls(self, arg='.'):
        'Lists files in either the current directory, or a specified directory. Ex: ls /home/eteled/Python'
        if arg == "":
         lsout = os.listdir(".")
         print(lsout)
        else:
         lsout = os.listdir(arg)
         print(lsout)

    def do_pwd(self, arg):
        'Displays your current directory. Ex: pwd'
        print(os.getcwd())

    def do_cd(self, arg):
        'Changes directory. Ex: cd programs'
        os.chdir(arg)

    def do_cp(self, arg):
        'Copies a file specified in input fields when this command is run. Ex: cp'
        src = input(lang.SOURCE_FILE)
        dst = input(lang.DEST_FILE)
        with open(src, 'r') as f_src:
            with open(dst, 'w') as f_dst:
                f_dst.write(f_src.read())

    def do_mv(self, arg):
        'Moves a file specified in input fields when this command is run. Ex: cp'
        src = input(lang.SOURCE_FILE)
        dst = input(lang.DEST_FILE)
        with open(src, 'r') as f_src:
            with open(dst, 'w') as f_dst:
                f_dst.write(f_src.read())
        os.remove(src)

    def do_rm(self, arg):
        'Removes the file or folder with the specified path. Ex: rm /home/serialkiller/murder/knife.jpg'
        os.remove(arg)
        
    def do_clear(self, arg):
        'Clears the screen'
        os.system('cls' if os.name == 'nt' else 'clear')


    # ----- record and playback -----
    def do_savecmd(self, arg):
        'Save future commands to filename:  RECORD rose.cmd'
        self.file = open(arg, 'w')
    def do_opencmd(self, arg):
        'Playback commands from a file:  PLAYBACK rose.cmd'
        self.close()
        with open(arg) as f:
            self.cmdqueue.extend(f.read().splitlines())
    def precmd(self, line):
        line = line.lower()
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
if os.environ.get('GITHUB_ACTIONS') == "true":
        logging.info('Running on GitHub Actions, not using the LiuOS Shell')
        print(lang.ENTER_USERNAME_LOGIN)
        print(lang.ENTER_PASSWD_LOGIN)
        print(lang.FAKE_SUCCESSFUL_LOGIN)
        logging.warning("Fake login completed")
        print(lang.SHELL_INTRO)
        print("LiuOS: pwd")
        LiuShell().do_pwd("test")
        print("LiuOS: ls")
        LiuShell().do_ls()
        cmd_run = os.getenv("Cmd")
        LiuShell().do_runcmd(cmd_run)
        print("Sample strings:")
        print(lang.SAMPLE_ABC)
        print(lang.SAMPLE_STRING)
        TestProg = "programs/helloworld.py"
        logging.debug("Launching test program")
        runpy.run_path(path_name=TestProg)
        print("Code completed")
else:
 # Authentication system
 print(f"LiuOS {api.VerLiuOS}")
 while attemps < 7:
    try:
        username = input(lang.ENTER_USERNAME_LOGIN)
        logging.debug(f'Entered username {username}')
        password = getpass.getpass(lang.ENTER_PASSWD_LOGIN)
        logging.debug('Entered password')
        bytehash = hashlib.sha3_512(password.encode())
        pwdreshash = bytehash.hexdigest()
        logging.debug('Generated hash of password')
        if attemps == 6:
            ## Brute force protection
            logging.fatal("6 or more incorrect credentials entered")
            ERROR_CODE = "CRED_FORCE_ERROR"
            raise Exception(lang.BRUTE_FORCE_CRASH)
        if os.environ.get('GITHUB_ACTIONS') == "true":
            logging.warning("Running on Github Actions")
            actualsys()
        elif username == cred.loginname and pwdreshash == cred.loginpass:
            print(lang.SUCCESSFUL_LOGIN)
            logging.debug('Correct login credentials, logged in')
            actualsys()
        else:
            print(lang.INCORRECT_LOGIN)
            logging.error("Incorrect login credentials")
            attemps += 1
            continue
    except Exception as e:
        os.system('cls' if os.name == 'nt' else 'clear')    
        error_code = 0
        trace = traceback.format_exc()
        error_description = str(e)
        error_code = hash(error_description)
        error_description = f"0x100{abs(error_code) % 256:02x}"
        
        print(f"\n;(\nA fatal error has occurred causing an exception. LiuOS has stopped to prevent data corruption or other issues.\n\nError code: {error_description}\n\nDescription of error: {e}")
        if should_crash:
            if crash_times == 0:
                print("\nNote: LiuOS has crashed more than once in this Python instance. \nTo attempt to fix the issue, try restarting Python. \nIf the bugcheck reoccurs, file a bug report with the traceback in your LiuOS.log file.\n")
            FORMAT = 'CRASH | TIME - %(asctime)s | PROCESS - %(processName)s %(process)d | MSG - %(message)s'
            logging.basicConfig(filename='LiuOS.log', encoding='utf-8', level=logging.DEBUG, format=FORMAT)
            crashlog = f"Crashed with code {error_description}"
            logging.fatal(f"Code: {error_description}.\n {trace}")
            print("System will reset in 15 sec!")
            time.sleep(15)
            FORMAT = '%(levelname)s | TIME - %(asctime)s | PROCESS - %(processName)s %(process)d | MSG - %(message)s'
            logging.basicConfig(filename='LiuOS.log', encoding='utf-8', level=logging.DEBUG, format=FORMAT)
            attemps = 0
            error_code = ""
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"LiuOS {api.VerLiuOS}\nInfo: System recovered from bugcheck {error_description}")
            error_description = ""
            crash_times = 1
        else:
            print("WARN: Crash Bypass")