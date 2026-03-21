# Cloudflare WARP GUI

A GUI application based on [warp-cli](https://developers.cloudflare.com/warp-client/get-started/linux) for Linux.

## Quick Access

- [Installation](#installation)
- [Hidden Mode](#hidden-mode)
- [Uninstall](#uninstall)
- [Screenshot](#screenshot)
- [Resolved Issues](#resolved-issues)

## Installation

Read the [warp-cli install](https://developers.cloudflare.com/warp-client/get-started/linux) documentation. Install `warp-cli` and register with the `$ warp-cli registration new` command. Ensure you test your connection and accept any TOS notices by trying `$ warp-cli connect` and then `$ warp-cli disconnect`.

Then execute the following command:

    $ sudo apt install git python3 python3-venv python3-pip build-essential patchelf (Replace "apt" with your package manager)
    $ git clone https://github.com/imngkhang/cloudflare-warp-gui
    $ cd cloudflare-warp-gui
    $ sudo ./install.sh
    $ sudo chmod +x /usr/share/applications/warp-gui.desktop

> Disclaimer: This script use "sudo" to copy the desktop file and the binary to /usr/bin. If you don't want to use "sudo", you can execute the following commands to build and install it manually, and if you don't like to compile, you can use the command in the [original repo](https://github.com/mrmoein/warp-cloudflare-gui), as the Installation section, or if you using "doas", you can replace all the "sudo" command bellow with "doas".

    $ sudo apt install git python3 python3-venv python3-pip build-essential patchelf (Replace "apt" with your package manager)
    $ git clone https://github.com/imngkhang/cloudflare-warp-gui
    $ cd cloudflare-warp-gui
    $ python3 -m venv venv
    $ source venv/bin/activate
    $ pip3 install -U pip wheel setuptools nuitka zstandard
    $ pip3 install -r requirements.txt
    $ sudo cp icons/logo.png /usr/share/icons/hicolor/32x32/warp_gui.png
    $ python3 -m nuitka --standalone --onefile --output-dir=dist --enable-plugin=pyqt5 --include-data-dir=icons=icons --include-data-dir=warp_gui/ui=warp_gui/ui --include-data-dir=designer=designer --include-data-dir=requirements=requirements --include-data-files=requirements.txt=requirements.txt --include-data-files=LICENSE=LICENSE -o warp-qt main.py
    $ sudo cp /dist/warp-qt /usr/bin/ && sudo chmod +x /usr/bin/warp-qt
    $ sudo cat <<EOF > /usr/share/warp-gui.desktop 
     [Desktop Entry]
     Name=Cloudflare WARP 
     Version=1.0
     Comment=A gui app base on warp-cli for linux
     Exec=warp-qt
     Icon=warp_gui
     Terminal=false
     Type=Application
     EOF
    $ deactivate 
    $ sudo chmod +x /usr/share/applications/warp-gui.desktop

Now search for `Cloudflare WARP` in your app menu.


## Hidden Mode
If you only want to use the tray icon, you can run the program in hidden mode.
    
    $ warp-qt --hide

## Uninstall

Remove the file "/usr/bin/warp-qt" and "/usr/share/applications/warp-gui.desktop" by this command:

    $ sudo rm -f /usr/bin/warp-qt && sudo rm -f /usr/share/applications/warp-gui.desktop

## Screenshot

![Cloudflare WARP GUI](icons/Screenshot.png)

## Resolved Issues
- [There are 2 tray icons of WARP CLI and this GUI app](https://github.com/mrmoein/warp-cloudflare-gui/issues/11)
