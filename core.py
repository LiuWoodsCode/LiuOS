# import stuff
import hashlib
import getpass
import lang
import cred
import logging
# Log formatting
FORMAT = '%(levelname)s | TIME - %(asctime)s | PROCESS - %(processName)s %(process)d | MSG - %(message)s'
logging.basicConfig(filename='LiuOS.log', encoding='utf-8', level=logging.DEBUG, format=FORMAT)
# Counter
attemps = 0
# Authentication system
while attemps < 3:
    username = input(lang.ENTER_USERNAME_LOGIN)
    logging.debug('Entered username')
    password = getpass.getpass(lang.ENTER_PASSWD_LOGIN)
    logging.debug('Entered password')
    bytehash = hashlib.sha512(password.encode())
    pwdreshash = bytehash.hexdigest()
    logging.debug('Generated hash of password')
    
    if username == cred.loginname and pwdreshash == cred.loginpass:
        print(lang.SUCCESSFUL_LOGIN)
        logging.debug('Correct login credentials, logged in')
        break
    else:
        print(lang.INCORRECT_LOGIN)
        logging.error("Incorrect login credentials")
        attemps += 1
        continue
print("")