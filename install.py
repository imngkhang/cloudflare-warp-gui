import os
import sys
from pathlib import Path

cur_path = sys.path[0]

os.system("pip3 install -U pip wheel setuptools nuitka zstandard")
os.system("pip3 install -r requirements.txt")
os.system("mkdir -p ~/.local/share/icons")
os.system("cp {}/icons/logo.png /usr/share/icons/hicolor/32x32/apps/warp_gui.png".format(cur_path))
os.system("python3 -m nuitka --standalone --onefile --output-dir=dist --enable-plugin=pyqt5 --include-data-dir=icons=icons --include-data-dir=warp_gui/ui=warp_gui/ui --include-data-dir=designer=designer --include-data-dir=requirements=requirements --include-data-files=requirements.txt=requirements.txt --include-data-files=LICENSE=LICENSE -o warp-qt main.py")
os.system("cp {}/dist/warp-qt /usr/bin/ && sudo chmod +x /usr/bin/warp-qt")
desktop_file = '/usr/share/applications/warp-gui.desktop'.format(Path.home())

file = open(desktop_file, 'w+')
file.write('''[Desktop Entry]
Name=Cloudflare WARP 
Version=1.0
Comment=A gui app base on warp-cli for linux
Exec=warp-qt
Icon=warp_gui
Terminal=false
Path={}
Type=Application
'''.format(cur_path, cur_path))
print('Desktop file created at "{}"'.format(desktop_file))


