!/usr/bin/env python3x

import os
import platform
import subprocess
import sys

system = platform.system()

if system == "Darwin":
    result = subprocess.check_output(
        ["sysctl", "-n", "machdep.cpu.brand_string"], universal_newlines=True
    )
    if "Intel" in result:
        print("Intel Mac Detected")
    elif "M1" in result:
        print("M1 Mac Detected")

    # I don't have to set up Macs frequently
    # We'll see if that changes

elif system == "Windows":
    # I don't really work on the command line in Windows
    # We'll see if that changes.
    pass

elif system == "Linux":

    distro = subprocess.check_output(["lsb_release", "-is"], text=True)

    if "Ubuntu" in distro:
        print("Ubuntu detected")
    else:
        print(f"{distro} detected")

    # Install Homebrew

    if not os.path.isdir("homebrew"):
        print("Installing Homebrew")
        subprocess.run(["bash", "install_homebrew.sh"], capture_output=True, text=True)
    else:
        print("Homebrew already installed")

    # Install zsh

    if "zsh" in os.getenv("SHELL"):
        print("Zsh already installed")
    else:
        print("Installing Zsh")
        subprocess.run(["bash", "install_zsh.sh"], capture_output=True, text=True)

    # Install anaconda

    if not os.path.isdir("anaconda3"):

        print("Installing Anaconda")
        subprocess.run(
            [
                "wget",
                "https://repo.anaconda.com/archive/Anaconda3-2023.03-1-Linux-x86_64.sh",
            ]
        )

        subprocess.run(["bash", "Anaconda3-2023.03-1-Linux-x86_64.sh"])
    else:
        print("Anaconda already installed")
else:
    sys.exit(f"Unexpected system {system}")

