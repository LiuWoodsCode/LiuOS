## LiuOS API v0.0.1
import os
import requests
## API Starts here
VerAPI = "0.0.1"
VerLiuOS = "0.1.1"
DebugBuild = False
RepoURL = "https://github.com/LiuWoodsCode/LiuOS"
## Handy GHA check variable
if os.environ.get('GITHUB_ACTIONS') == "true":
    RunningActions = True
else:
    RunningActions = False
def webget(self, arg):
        url = "http://www.example.com"
        headers = {
         "User-Agent": f"LiuOS{VerLiuOS}_webget"
         }

        response = requests.get(url, headers=headers)
        
def ls(self, arg='.'):
        'Lists fil in either the current directory, or a specified directory. Ex: ls /home/eteled/Python'
        if arg == "":
         lsout = os.listdir(".")
         print(lsout)
        else:
         lsout = os.listdir(arg)
         print(lsout)

def pwd(self, arg):
        'Displays your current directory. Ex: pwd'
        print(os.getcwd())

def cd(self, arg):
        'Changes directory. Ex: cd programs'
        os.chdir(arg)

def cp(src, dst):
        'Copies a file specified in input fields when this command is run. Ex: cp'
        with open(src, 'r') as f_src:
            with open(dst, 'w') as f_dst:
                f_dst.write(f_src.read())

def mv(src, dst):
        'Moves a file specified in input fields when this command is run. Ex: cp'
        cp(src, dst)
        os.remove(src)

def rm(self, arg):
        os.remove(arg)