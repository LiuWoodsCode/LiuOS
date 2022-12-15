# import stuff
import hashlib
import getpass
import lang
import cred
import logging
from os import environ
import sys
import cmd
import runpy
# Log formatting
FORMAT = '%(levelname)s | TIME - %(asctime)s | PROCESS - %(processName)s %(process)d | MSG - %(message)s'
logging.basicConfig(filename='LiuOS.log', encoding='utf-8', level=logging.DEBUG, format=FORMAT)
class LiuShell(cmd.Cmd):
    intro = lang.SHELL_INTRO
    prompt = 'LiuOS: '
    file = None

    # ----- basic turtle commands -----
    def do_run(self, arg):
        'Runs the script specified, it must be in the same dir as LiuOS and exist, or Python will crash. Ex: run eteled.py'
        logging.info("Running command using run in shell")
        runpy.run_path(path_name=arg)
    def do_logout(self, arg):
        'Closes the shell. Ex: logout'
        logging.warning("Logging out shell session")
        print('Logging out...')
        self.close()
        return True
    def do_shutdown(self, arg):
        'Closes the shell, and quits the script. Ex: shutdown'
        print('Logging out...')
        self.close()
        return True

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
        LiuShell().cmdloop()
logging.debug("Assigned main system function")
if environ.get('GITHUB_ACTIONS') == "true":
        logging.info('Running on GitHub Actions, not using the LiuOS Shell')
        print(lang.ENTER_USERNAME_LOGIN)
        print(lang.ENTER_PASSWD_LOGIN)
        print(lang.FAKE_SUCCESSFUL_LOGIN)
        logging.warning("Fake login completed")
        print("Code completed")
else:
 # Authentication system
    while attemps < 6:
        username = input(lang.ENTER_USERNAME_LOGIN)
        logging.debug('Entered username')
        password = getpass.getpass(lang.ENTER_PASSWD_LOGIN)
        logging.debug('Entered password')
        bytehash = hashlib.sha512(password.encode())
        pwdreshash = bytehash.hexdigest()
        logging.debug('Generated hash of password')
        if environ.get('GITHUB_ACTIONS') == "true":
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
raise Exception("Too many password attempts. Because of the risk of a brute force attack, after 6 attempts, you will need to rerun LiuOS to try 6 more times.")
