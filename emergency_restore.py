import os
import sys
import ctypes
import platform
import subprocess
import shutil

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_as_admin():
    if sys.platform.startswith('win'):
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

def restore_hosts_file():
    print("[*] Restoring hosts file...")
    hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
    backup_path = hosts_path + ".exam_shield_backup"
    
    if os.path.exists(backup_path):
        try:
            shutil.copy2(backup_path, hosts_path)
            os.remove(backup_path)
            print("[+] Repaired hosts file from backup.")
            return
        except Exception as e:
            print(f"[-] Failed to restore from backup: {e}")

    if os.path.exists(hosts_path):
        try:
            with open(hosts_path, 'r') as f:
                content = f.read()
            if "# EXAM SHIELD BLOCKING - DO NOT EDIT" in content:
                # Remove everything between the markers
                start = content.find("# EXAM SHIELD BLOCKING - DO NOT EDIT")
                end = content.find("# END EXAM SHIELD BLOCKING")
                if start != -1 and end != -1:
                    end += len("# END EXAM SHIELD BLOCKING")
                    new_content = content[:start] + content[end:]
                    with open(hosts_path, 'w') as f:
                        f.write(new_content)
                    print("[+] Removed Exam Shield blocks from hosts file.")
            else:
                print("[+] Hosts file is clean.")
        except Exception as e:
            print(f"[-] Failed to edit hosts file: {e}")

def restore_dns():
    print("[*] Restoring DNS settings to automatic (DHCP)...")
    try:
        if platform.system().lower() == "windows":
            subprocess.run(['netsh', 'interface', 'ip', 'set', 'dns', 'name="Local Area Connection"', 'source=dhcp'], capture_output=True)
            subprocess.run(['netsh', 'interface', 'ip', 'set', 'dns', 'name="Wi-Fi"', 'source=dhcp'], capture_output=True)
            subprocess.run(['ipconfig', '/flushdns'], capture_output=True)
            print("[+] DNS settings restored to DHCP for all generic adapters.")
    except Exception as e:
        print(f"[-] Failed to restore DNS: {e}")

def kill_exam_shield_processes():
    print("[*] Stopping any stuck Exam Shield processes...")
    try:
        if platform.system().lower() == "windows":
            subprocess.run(['taskkill', '/F', '/IM', 'exam_shield.exe'], capture_output=True)
            print("[+] Exam Shield processes killed. Keyboard hooks released.")
    except Exception as e:
        print(f"[-] Failed to kill processes: {e}")

if __name__ == "__main__":
    if not is_admin():
        print("This script requires Administrator privileges. Requesting...")
        run_as_admin()
        sys.exit(0)
    
    print("=" * 50)
    print("      Exam Shield Emergency Restore Tool")
    print("=" * 50)
    print("Use this tool if Exam Shield crashed and left your internet")
    print("or system blocked.")
    print("")
    
    kill_exam_shield_processes()
    restore_hosts_file()
    restore_dns()
    
    print("=" * 50)
    print("Restore complete! Please check if your internet is working.")
    print("=" * 50)
    input("Press Enter to exit...")
