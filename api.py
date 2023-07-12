## LiuOS API v0.0.1
import http.client
import os
import platform
import datetime
import ctypes
## LiuOS API v0.0.1
## API Starts here
VerAPI = "0.1.5"
VerLiuOS = "0.3.0"
DebugBuild = False
RepoURL = "https://github.com/LiuWoodsCode/LiuOS"
## Handy GHA check variable
if os.environ.get('GITHUB_ACTIONS') == "true":
    RunningActions = True
else:
    RunningActions = False
def do_webget(self, arg):    
        'Makes a web request Can only use HTTPS if Python was compiled with SSL/TLS support.'
        conn = http.client.HTTPSConnection(arg)
        conn.request("GET", "/")
        res = conn.getresponse()
        data = res.read()
        conn.close()
        return data.decode("utf-8")
        
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

def get_version(self):
        """Returns the version of the program."""
        return {'version': self.version, 'api_version': self.api_version}

def allocate_memory(self, memory_address, size, data):
        """Allocates a block of memory of the specified size at the specified memory address and writes the specified data to it. Python for Windows only."""
        # allocate memory
        ptr = ctypes.windll.kernel32.VirtualAllocEx(ctypes.c_void_p(), memory_address, size, 0x1000 | 0x2000, 0x04)
        # write data to the allocated memory
        ctypes.windll.kernel32.WriteProcessMemory(ctypes.c_void_p(), ptr, data, len(data), None)
        return ptr

def read_file(self, file_path):
        """Reads the contents of the specified file."""
        with open(file_path, 'r') as file:
            return file.read()

def write_file(self, file_path, data):
        """Writes the specified data to the specified file."""
        with open(file_path, 'w') as file:
            file.write(data)

def get_process_list(self):
        """Returns a list of all running processes. Python for Windows only, unless you've got tasklist on a Linux/Unix system."""
        process_list = []
        for process in os.popen('tasklist'):
            process_list.append(process.split()[0])
        return process_list

def kill_process(self, process_name):
        """Kills the process with the specified name. Python for Windows only, unless you've got taskkill /f /im on a Linux/Unix system."""
        os.system('taskkill /f /im ' + process_name)

def get_system_info(self):
        """ Returns the system information"""
        return {'system': platform.system(), 'release': platform.release(), 'version': platform.version(),
                'machine': platform.machine(), 'processor': platform.processor()}
                
def get_memory_info(self):
        """Returns the system memory information"""
        memory_info = os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES')  / (1024. ** 3)
        return {'total': memory_info}

class LiuOSGraphicsAPI:
    def __init__(self):
        print("The graphics API is depercated. Any calls to functions will fail.")

    def open_window(self):
        raise Exception("usage of depercated API")

    def display_image(self, filepath):
        raise Exception("usage of depercated API")

    def print_output(self, text):
        raise Exception("usage of depercated API")

    def open_dialog_box(self, title, message):
        raise Exception("usage of depercated API")

    def open_text_box(self):
        raise Exception("usage of depercated API")

    def open_file_picker(self):
        raise Exception("usage of depercated API")

    def open_folder_picker(self):
        raise Exception("usage of depercated API")
## Handy GHA check variable
