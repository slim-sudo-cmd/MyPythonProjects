import socket

target = "192.168.4.43"
port = 7800
commands = [b"HELP\n", b"STATS\n", b"GET / HTTP/1.1\n\n", b"VERSION\n"]

for cmd in commands:
    try:
        # Create a new socket for each attempt
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        s.connect((target, port))
        
        print(f"[*] Trying command: {cmd.strip().decode()}")
        s.send(cmd)
        
        response = s.recv(1024)
        if response:
            print(f"[+] Response: {response.decode('utf-8', errors='ignore').strip()}")
        s.close()
    except Exception as e:
        print(f"[-] No response or failed: {e}")

