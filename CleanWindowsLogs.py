import os
import subprocess
import ctypes
import sys
import time
import shutil


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    print("[ERROR] Error #1 (Run as Administrator)")
    sys.exit()

def print_title():
    os.system('title Widnows Logs Cleaner (WLC) by @godsnico v1.0')
    title = r"""
   _____ _      ______          _   _   _______ ____   ____  _      
  / ____| |    |  ____|   /\   | \ | | |__   __/ __ \ / __ \| |     
 | |    | |    | |__     /  \  |  \| |    | | | |  | | |  | | |     
 | |    | |    |  __|   / /\ \ | . ` |    | | | |  | | |  | | |     
 | |____| |____| |____ / ____ \| |\  |    | | | |__| | |__| | |____ 
  \_____|______|______/_/    \_\_| \_|    |_|  \____/ \____/|______|
    """
    print(title)


def loading_animation():
    animation = "|/-\\"
    for i in range(20):
        time.sleep(0.1)
        sys.stdout.write("\r[" + animation[i % len(animation)] + "]")
        sys.stdout.flush()
    print("\r[+] Loading complete!")
    time.sleep(1)
    clean_temp_logs()
    print("\r[+] Cleanup complete!") 
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')  

def clean_temp_logs():
    temp_paths = [
        os.environ['TEMP'],
        os.path.join(os.environ['WINDIR'], 'Temp'),      
        os.path.join(os.environ['WINDIR'], 'Logs'),
        os.path.join(os.environ['WINDIR'], 'Prefetch')
    ]

    for path in temp_paths:
        if os.path.exists(path):
            print(f"[-] Cleaning: {path}")
            try:
                shutil.rmtree(path, ignore_errors=True)
                os.makedirs(path, exist_ok=True)  
            except Exception as e:
                print(f"[ERROR] Failed to clean {path}: {e}")

print_title()
loading_animation()
