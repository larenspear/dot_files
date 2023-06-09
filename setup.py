#!/usr/bin/env python3x

import argparse
from pathlib import Path
import platform
import sys
import subprocess
parser = argparse.ArgumentParser()

args = parser.parse_args()

dotfile_dir = Path(__file__).parent
config_dir = Path.home() / '.config'
data_dir = Path.home() / '.local/share'

system = platform.system()

if system == 'Darwin':
    result = subprocess.check_output(['sysctl', '-n', 'machdep.cpu.brand_string'],universal_newlines=True)
    if "Intel" in result:
        print("Intel Mac Detected")
    elif "M1" in result:
        print("M1 Mac Detected")

elif system == 'Windows':
    pass

elif system == 'Linux':
    distro = subprocess.check_output(['lsb_release', '-is'], text=True)
    distro = distro.rstrip()
    if "Ubuntu" in distro:
        print("Ubuntu detected")
    else:
        print(f"{distro} detected")
else:
    sys.exit(f'Unexpected system {system}')
