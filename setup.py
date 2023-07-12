import os
def rename_file_if_not_exists(filename, new_filename):
    if not os.path.exists(filename):
        if os.path.exists(new_filename):
            return True
        else:
            os.rename(new_filename, filename)
            print(f"Created default cred file.")
    else:
        return True
rename_file_if_not_exists("defaultcred.py", "cred.py")