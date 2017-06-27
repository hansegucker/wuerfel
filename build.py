# coding=utf-8
#!/usr/bin/env python

import os

def yesnoanswer (question):
    answer = input(question + "[j/n]")
    answer = answer.replace(" ", "")
    if answer == "j":
        answer = True
    elif answer == "y":
        answer = True
    elif answer == "J":
        answer = True
    elif answer == "Y":
        answer = True
    else:
        answer = False
    return answer

print("Builder v1.0.0 - wuerfelgui bauen")
print("#################################")
while True:
    print("Bitte wählen Sie ihr Betriebssystem:")
    print("\t 1 steht für Linux")
    print("\t 2 steht für Windows")
    print("\t 3 steht für Mac OSX")
    operationsystem = input("Betriebssystem: ")
    operationsystem = int(operationsystem)
    if operationsystem == 1 or operationsystem == 2 or operationsystem == 3:
        break
    print("")
    print("Bitte geben Sie eine 1, 2 oder 3 ein!")

input("Bitte erfüllen Sie die Abhängigkeiten, die in doc/installation.md beschrieben sind. [ENTER]")

print("Baue die Programmdateien")
# if operationsystem == 3:
#     os.system("rd /s /q build")
#     os.system("rd /s /q dist")

os.system("pyinstaller src/wuerfelgui.py")

if operationsystem == 1:
    print("Kopiere Programmdateien ...")
    os.system("cp -r dist/wuerfelgui install-linux/usr/share")
    os.system("rm -R -f build")
    os.system("rm -R -f dist")

    print("Baue deb-Packet ...")
    os.system("cd install-linux && ./build.sh")

    os.system("rm -R -f wuerfel-install-linux/usr/share/wuerfelgui")
