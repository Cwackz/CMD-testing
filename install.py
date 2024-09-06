import os
import subprocess


INSTALL_VERSION = "1.0" #current version
pass

def install():
    os.system("clear")
    print("Installing required packages...")
    subprocess.run(["pip3", "install", "prompt_toolkit", "rich", "paramiko"])
    print("Installation complete!")
    with open(".install_version", "w") as f:
        f.write(INSTALL_VERSION)
    print("Please run 'python3 main.py' to start the program.")

if __name__ == "__main__":
    install()