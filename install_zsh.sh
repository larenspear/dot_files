#!/bin/bash

##December 2024 edit - why do this instead of loading modules? Great question.
##I used this on my university cluster to get zsh because I was desperate.

# zsh will not install without ncurses. If the machine doesn't have this library, it will need to be installed first.
export CXXFLAGS=" -fPIC" CFLAGS=" -fPIC" CPPFLAGS="-I${HOME}/include" LDFLAGS="-L${HOME}/lib"
wget https://ftp.gnu.org/pub/gnu/ncurses/ncurses-6.2.tar.gz
tar -xzvf ncurses-6.2.tar.gz
cd ncurses-6.2
./configure --prefix=$HOME --enable-shared
make
make install
cd .. && rm ncurses-6.2.tar.gz && rm -r ncurses-6.2

wget -O zsh.tar.xz https://sourceforge.net/projects/zsh/files/latest/download
mkdir zsh && unxz zsh.tar.xz && tar -xvf zsh.tar -C zsh --strip-components 1
cd zsh
./configure --prefix=$HOME
make
make install
cd .. && rm zsh.tar && rm -r zsh
echo -e "export SHELL=~/bin/zsh\nexec ~/bin/zsh -l" >> ~/.bash_profile # or chsh
