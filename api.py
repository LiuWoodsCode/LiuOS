## LiuOS API v0.0.1
import http.client
import os
import platform
import datetime
import ctypes
import tkinter as tk
from tkinter import PhotoImage, filedialog, messagebox, StringVar
## LiuOS API v0.0.1
## API Starts here
VerAPI = "0.1.5"
VerLiuOS = "0.2.5"
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
        return {'version': self.version, 'api_version': self.api_version, 'build_date': self.build_date}

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
        self.root = tk.Tk()
        self.root.title("Graphics API")

    def open_window(self):
        self.root.mainloop()

    def display_image(self, filepath):
        img = PhotoImage(file=filepath)
        label = tk.Label(self.root, image=img)
        label.image = img
        label.pack()

    def print_output(self, text):
        os.system("lpr -P printer_name " + text)

    def open_dialog_box(self, title, message):
        messagebox.showinfo(title, message)

    def open_text_box(self):
        text_var = StringVar()
        entry = tk.Entry(self.root, textvariable=text_var)
        entry.pack()
        return text_var

    def open_file_picker(self):
        filepath = filedialog.askopenfilename()
        return filepath

    def open_folder_picker(self):
        folderpath = filedialog.askdirectory()
        return folderpath
## Handy GHA check variable