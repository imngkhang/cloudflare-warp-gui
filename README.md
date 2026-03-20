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

    $ sudo apt install git python3 python3-venv python3-pip 
    $ git clone https://github.com/imngkhang/cloudflare-warp-gui
    $ cd cloudflare-warp-gui
    $ bash install.sh
    $ sudo chmod +x /usr/share/applications/warp-gui.desktop

> Disclaimer: This script use "sudo" to copy the desktop file and the binary to /usr/bin. If you don't want to use "sudo", you can execute the following commands to install it manually.



 

Now search for `Cloudflare WARP` in your desktop menu.


## Hidden Mode
If you only want to use the tray icon, you can run the program in hidden mode.
    
    $ warp-qt --hide

## Uninstall

Remove the file "/usr/bin/warp-qt" and "/usr/share/applications/warp-gui.desktop" 

## Screenshot

![Cloudflare WARP GUI](icons/Screenshot.png)

## Resolved Issues
- [There are 2 tray icons of WARP CLI and this GUI app](https://github.com/mrmoein/warp-cloudflare-gui/issues/11)
