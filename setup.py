import platform
import subprocess

def get_os_specific_command():
    current_os = platform.system()
    if current_os == "Windows":
        return "copy defaultcred.py cred.py"
    elif current_os == "Darwin" or current_os == "Linux":
        return "cp -- \"defaultcred.py\" \"cred.py\""
    else:
        raise OSError("LiuOS is incompatible with your low-level OS.")

def run_command(command):
    try:
        output = subprocess.check_output(command, shell=True, text=True, stderr=subprocess.STDOUT)
        print(output)
    except subprocess.CalledProcessError as e:
        print("Error executing the command:", e)

if __name__ == "__main__":
    current_directory_command = get_os_specific_command()
    run_command(current_directory_command)
