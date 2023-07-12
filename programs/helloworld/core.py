## LiuOS Program Template v1.0
## Program IDs go like this: LiuOS.{YourNameWithNoSpaces}.{YourProgramNameWithNoSpaces} or use the below example as a base.
ProgramID = "LiuOS.LiuWoodsCode.HelloWorld"
## Human readable name for your program
ProgramName = "Hello World"
## Your build number
BuildNum = "6666666"
## Keep this here, it's for logging your code and interfacing with the LiuOS APIs (Although the import part is jank)
import logging
import api
FORMAT = '%(levelname)s | TIME - %(asctime)s | PROCESS - %(processName)s %(process)d | MSG - %(message)s'
logging.basicConfig(filename=f'{ProgramID}.log', encoding='utf-8', level=logging.DEBUG, format=FORMAT)
## Import your modules
import random
# Code goes here.
print(api.VerAPI)
print(api.VerLiuOS)
print(api.RepoURL)
print("Hello world!")
logging.debug("Log message")
logging.info("Log message")
logging.warning("Log message")
logging.error("Log message")
logging.critical("Log message")
logging.fatal("Log message")