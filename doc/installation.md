# Installation
## Mac OSX
1. Als Admin anmelden
### Python installieren
1. Download Python3.*: https://www.python.org/ftp/python/3.6.1/python-3.6.1-macosx10.6.pkg
2. `python-3.*.*-macosx*.*.pkg` ausführen
### git installieren
1. Download git: https://sourceforge.net/projects/git-osx-installer/files/git-2.13.0-intel-universal-mavericks.dmg/download?use_mirror=autoselect
2. `git-*.dmg` öffnen und installieren
### PIP installieren
1. Terminal öffnen
2. Folgende Befehle im Terminal ausführen:
  ```
  $ sudo su
  $ curl -O https://bootstrap.pypa.io/get-pip.py
  $ python3 get-pip.py
  $ rm get-pip.py
  ```
### PyQt5 installieren
1. Terminal öffnen
2. Folgende Befehle im Terminal ausführen:
  ```
  $ sudo su
  $ pip3 install PyQt5
  ```
### Programm herunterladen und ausführen
1. Terminal öffnen
2. Folgende Befehle im Terminal ausführen:
  ```
  $ git clone https://github.com/hansegucker/wuerfel.git
  $ cd wuerfel
  $ python3 wuerfelgui.py
  ```
