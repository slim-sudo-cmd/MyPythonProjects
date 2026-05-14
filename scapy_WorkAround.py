from scapy.all import *

target = "192.168.1.1"
# We pretend to be the 'trusted' port 73
# and we send a TCP SYN to port 80
ip = IP(dst=target)
tcp = TCP(sport=73, dport=80, flags="S")

print(f"[*] Sending crafted SYN from source port 73 to {target}:80...")
response = sr1(ip/tcp, timeout=2)

if response:
    print(f"[+] SUCCESS! Received response: {response.summary()}")
else:
    print("[-] Still filtered. The firewall is smarter than we thought.")

