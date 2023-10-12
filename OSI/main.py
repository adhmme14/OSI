import os
import time

def main():
    while True:
        print("""
(1) list
(0) exit""")
        
        command = input("OSI: ")

        if command == "1":
            print("""
1 - Alpine Linux
2 - Arch Linux
3 - Debian
4 - Fedora
5 - Manjaro AArch64
6 - OpenSUSE
7 - Pardus
8 - Ubuntu
9 - Void Linux""")
        
            type = input("Select OS: ")

            if type == "1":
                os.system("proot-distro install alpine")

            elif type == "2":
                os.system("proot-distro install archlinux")

            elif type == "3":
                os.system("proot-distro install debian")

            elif type == "4":
                os.system("proot-distro install fedora")

            elif type == "5":
                os.system("proot-distro install manjero-aarch64")

            elif type == "6":
                os.system("proot-distro install opensuse")

            elif type == "7":
                os.system("proot-distro install pardus")

            elif type == "8":
                os.system("proot-distro install ubuntu")

            elif type == "9":
                os.system("proot-distro install void")

        elif command == "0":
            print("\033[92m[\033[91m!\033[92m]\033[97m Exiting")
            break

main()