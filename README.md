# LiuOS

[![LiuOS Tests](https://github.com/LiuWoodsCode/LiuOS/actions/workflows/python-package.yml/badge.svg?branch=main)](https://github.com/LiuWoodsCode/LiuOS/actions/workflows/python-package.yml) [![Vulnerability Check](https://github.com/LiuWoodsCode/LiuOS/actions/workflows/codeql.yml/badge.svg)](https://github.com/LiuWoodsCode/LiuOS/actions/workflows/codeql.yml) [![LiuOS Testing on older Python releases](https://github.com/LiuWoodsCode/LiuOS/actions/workflows/python-multi.yml/badge.svg)](https://github.com/LiuWoodsCode/LiuOS/actions/workflows/python-multi.yml)

A Python project meant to be like a computer's operating system in Python (logo and catchy slogan coming soon, preorder now!)

## How do I use this?

### Hacking


LiuOS is open source, and you can modify its code to your liking! Simply run:

```
git clone https://github.com/LiuWoodsCode/LiuOS
```

in your terminal, at the directory you want a "LiuOS" folder in and start hacking away!

### Learning

While you might not exactly be able to learn from my code, it does show some of the fundamentals of Python, and stuff like exception handling and authentication.

## Troubleshooting

### Why can't it find the `cred` module?

In short, this is caused by issues in Git not allowing us to have a file on GitHub, while having `gitignore` file ignore changes to it. 

To fix the missing module, run `python3 setup.py` while in the directory that contains the LiuOS repository. This will copy the template file over to `cred.py` and allow LiuOS to start.

## Can I boot this on my PC?


While you can have it run on login of your main OS (Windows, macOS, or Linux) there is currently no way to have LiuOS (or Python in general).

### BIOS/UEFI boot programs

Technically, if you enough of x86_64 ASM or Rust, you could port Python to a boot program, it wouldn't be feasible.

For example, Windows 11 isn't running from the UEFI of your PC, what's running in the UEFI is actualy Windows Boot Manager, which loads the NT kernel and completes the rest of the boot chain.

### Linux, and startup programs

#### Setting up Ubuntu Server 22.04 as LiuOS



1. Install Ubuntu: Download the Ubuntu Server ISO image from the official Ubuntu website (<https://ubuntu.com/download/server>) and create a bootable USB drive. Make sure to install Ubuntu on your desired machine.
2. Update and upgrade packages: After the installation completes and you have a terminal prompt, update the package lists and upgrade the system by running the following commands:

   ```
   sudo apt update
   sudo apt upgrade
   ```
3. Install Git: Git is required to clone the repository. Install it by running:

   ```
   sudo apt install git
   ```
4. Clone the repository: Use Git to clone the repository from the specified URL. Run the following command:

   ```
   git clone https://github.com/LiuWoodsCode/LiuOS
   ```
5. Install Python: Most likely, Python is already installed on Ubuntu, but you can ensure the latest version is available by running:

   ```
   sudo apt install python3
   ```
6. Install project dependencies: Navigate to the cloned repository directory using `cd` command:

   ```
   cd LiuOS
   ```

   Then, if there is a requirements.txt file present in the repository, install the required dependencies using pip:

   ```
   pip install -r requirements.txt
   ```
7. Test the Python program: Before proceeding to set up the startup, test your Python program to ensure it runs correctly. Run the program using the Python interpreter:

   ```
   python3 setup.py
   ```


1. Set up the startup service: To run your Python program at startup, you can create a systemd service. Create a new service file using a text editor:

   ```
   sudo nano /etc/systemd/system/my_python_service.service
   ```
2. In the text editor, add the following content to the service file:

   ```
   [Unit]
   Description=My Python Service
   After=network.target
   
   [Service]
   ExecStart=/usr/bin/python3 /path/to/core.py
   WorkingDirectory=/path/to/LiuOS
   User=<your_username>
   Group=<your_group>
   
   [Install]
   WantedBy=multi-user.target
   ```

   Replace `/path/to/LiuOS` with the path to the cloned repository. Additionally, replace `<your_username>` and `<your_group>` with your actual username and group.
3. Save the file and exit the text editor.
4. Enable and start the service: To enable the service and make it start at boot, run the following commands:

   ```
   sudo systemctl enable my_python_service.service
   sudo systemctl start my_python_service.service
   ```
5. Reboot your system: Restart your Ubuntu machine to test if the service starts automatically and runs your Python program at startup:

   ```
   sudo reboot
   ```

Upon rebooting, LiuOS should boot after logging into Ubuntu.

##### Doing updates

###### Ubuntu Updates

When you are logged into LiuOS, run these 2 commands to do updates to Ubuntu:

```
runcmd sudo apt update
runcmd sudo apt upgrade
```

This should update Ubuntu to the latest packages

###### LiuOS Updates 
TODO: Do this section
