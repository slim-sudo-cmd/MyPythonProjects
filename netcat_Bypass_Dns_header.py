import socket

target = "192.168.1.1"
port = 53

# This is a standard DNS query for google.com
dns_query = b'\xaa\xaa\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x03www\x06google\x03com\x00\x00\x01\x00\x01'

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    s.connect((target, port))
    
    print(f"[*] Sending DNS query to {target}...")
    s.send(dns_query)
    
    data = s.recv(1024)
    print(f"[+] Received Response: {data.hex()}")
    print("[!] Service is ACTIVE and responding to queries.")
    s.close()
except Exception as e:
    print(f"[!] No response: {e}")

