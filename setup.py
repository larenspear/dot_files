#!/usr/bin/env python3x

import argparse
from pathlib import Path
import platform
import sys
import subprocess
import os
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

    #Install homebrew
    if not os.path.isdir("homebrew"):
        print("Installing Homebrew")
        subprocess.run(['bash', 'install_homebrew.sh'], capture_output=True, text=True)

    #Install zsh
    try:
        output = subprocess.check_output(['zsh', '--version'])
        print(output)
    except:
        print("Installing zsh")
        subprocess.run(['bash', 'install_zsh.sh'], capture_output=True, text=True)

    #link files

    symlinks = (
        ('bashrc', '.bashrc'),
        ('tmux.conf', f'{config_dir}/tmux/'),
        ('vim', '.vim'),
        ('zsh', f'{config_dir}/'),
    )

    for file, p in symlinks:
        path = Path(p)
        if not path.is_absolute():
            path = Path.home() / path
        if p.endswith('/'):
            path /= file
        target = Path(os.path.relpath(dotfile_dir / file, path.parent))
        if path.is_symlink() and target == Path(os.readlink(path)):
            continue
        rel_path = path.relative_to(Path.home())
        print(f'symlink {rel_path} to {target}')
        path.parent.mkdir(parents=True, exist_ok=True)
        if path.exists():
            if input(f'Replace {rel_path}? ') != 'y':
                continue
            path.unlink()
        path.symlink_to(target)

    #Tmux
    if not (tpm_dir := data_dir / 'tmux/plugins/tpm').exists():
        subprocess.run(['git', 'clone', 'https://github.com/tmux-plugins/tpm', tpm_dir], check=True)
        subprocess.run(tpm_dir / 'bin/install_plugins', check=True)

    if not (data_dir / 'vim/plugged').exists():
        subprocess.run(['vim', '+PlugInstall', '+qall'], env=vim_env, check=True)
else:
    sys.exit(f'Unexpected system {system}')

