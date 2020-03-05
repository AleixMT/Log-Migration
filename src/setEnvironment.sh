#!/usr/bin/env bash
# A simple portable shell script to initialize and customize a Linux working environment. Needs to be executed first
# as root and then as current user.
# Author: Pedro Espadas
# Date Created: 3/3/2020
# Version: 1.0

if [ "$(whoami)" != "root" ]; then  # executed if the user is root
	# Create folder for user software
	mkdir -p ~/.bin  # Create binaries user folder
	chmod 755 ~/.bin  # Change permissions
	cd ~
	userBinariesFolder=$(pwd)/.bin

	# Make sure that ~/.local/bin is present
	mkdir -p ~/.local/bin

	# Create folder for user launchers
	mkdir -p ~/.local/share/applications

	# pycharm
	cd $userBinariesFolder
	pycharm_version=pycharm-community-2019.1.1  # targeted pycharm version
	if [ ! -d $pycharm_version ]; then  # Do installation only if the program is present
		wget -q https://download.jetbrains.com/python/$pycharm_version.tar.gz  # Download
		tar xzf $pycharm_version.tar.gz  # unzip
		rm $pycharm_version.tar.gz*  # remove zip
		rm -f ~/.local/bin/pycharm  # ensure there is not collision with another link
		ln -s $(pwd)/$pycharm_version/bin/pycharm.sh ~/.local/bin/pycharm  # create soft link
	fi
	# Create desktop entry for pycharm launcher
	if [ -d $pycharm_version ]; then
		pycharm_launcher="[Desktop Entry]
Version=1.0
Type=Application
Name=PyCharm
Icon=$HOME/.bin/$pycharm_version/bin/pycharm.png
Exec=pycharm
Comment=Python IDE for Professional Developers
Terminal=false
StartupWMClass=jetbrains-pycharm"
		echo -e "$pycharm_launcher" > ~/.local/share/applications/pycharm.desktop
		chmod 775 ~/.local/share/applications/pycharm.desktop
	fi

	if [ -z "$(echo $PATH | grep -Eo "~/.local/bin" )" ]; then 
		echo "export PATH=$PATH:~/.local/bin" >> ~/.bashrc
	fi

else
	# Update repositories and system
	apt -y update
	apt -y upgrade

	# GNU C compiler, git suite, python3, pip3, python3-tk (tkinter)
	apt install -y gcc git-all python3 python3-pip python3-tk

	# Clean
	apt -y -qq autoremove
	apt -y -qq autoclean
fi
