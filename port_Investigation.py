import socket

target = "192.168.4.43"
port = 7800

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(3)
    s.connect((target, port))
    print(f"[*] Connected to {target}:{port}")
    
    # Just listen for 2 seconds to see if it speaks first
    banner = s.recv(1024)
    print(f"[+] Service says: {banner.decode('utf-8', errors='ignore')}")
    s.close()
except Exception as e:
    print(f"[!] No immediate banner: {e}")
