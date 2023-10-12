import os
import time

print("\033[97mLoading...")
time.sleep(2)

print("Loading Complete \033[92m[\033[91m!\033[92m]\033[97m")

complete = input("Are you sure you want to install(y/n) ")

if complete == "y":
    print("\033[92m[\033[91m!\033[92m]\033[97m Installing...")
    os.system("pkg install proot-distro")
    print("\033[92m[\033[91m!\033[92m]\033[97m Installing complete")

elif complete == "n":
    print("\033[92m[\033[91m!\033[92m]\033[97m Exiting")