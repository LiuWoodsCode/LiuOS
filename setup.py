import platform
import subprocess
import os

def get_os_specific_command_cred():
    current_os = platform.system()
    if current_os == "Windows":
        return "copy defaultcred.py cred.py"
    elif current_os == "Darwin" or current_os == "Linux":
        return "cp -- \"defaultcred.py\" \"cred.py\""
    else:
        raise OSError("LiuOS is incompatible with your low-level OS.")
    
def get_os_specific_command_russian():
    current_os = platform.system()
    if current_os == "Windows":
        return "copy langru.py lang.py"
    elif current_os == "Darwin" or current_os == "Linux":
        return "cp -- \"langru.py\" \"lang.py\""
    else:
        raise OSError("LiuOS is incompatible with your low-level OS.")

def get_os_specific_command_english():
    current_os = platform.system()
    if current_os == "Windows":
        return "copy langen.py lang.py"
    elif current_os == "Darwin" or current_os == "Linux":
        return "cp -- \"langen.py\" \"lang.py\""
    else:
        raise OSError("LiuOS is incompatible with your low-level OS.")

def run_command(command):
    try:
        output = subprocess.check_output(command, shell=True, text=True, stderr=subprocess.STDOUT)
        print(output)
    except subprocess.CalledProcessError as e:
        print("Error executing the command:", e)

file_path = "cred.py"
if os.path.exists(file_path):
    run_command(get_os_specific_command_cred())

print("Select your language:")
print("1. English")
print("2. Russian")
language_choice = input("Enter the number of the language you want to use: ")

if language_choice == "1":
    current_directory_command = get_os_specific_command_english()
    run_command(current_directory_command)
elif language_choice == "2":
    current_directory_command = get_os_specific_command_russian()
    run_command(current_directory_command)
else:
    print("Invalid choice. LiuOS will use the default language (English).")
    current_directory_command = get_os_specific_command_english()
    run_command(current_directory_command)

if __name__ == "__main__":
    current_directory_command = get_os_specific_command_cred()
    
