import socket

# We can't use 73 (privileged), so let's try 7373 or 1073
# Sometimes firewalls are broad and trust 'anything starting with 73' 
# or just non-standard high ports.
local_port = 7373 
target_ip = "192.168.229.84"
target_port = 80

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    
    # Attempt to bind our side to a specific port before connecting
    # This is the 'manual' version of nc -p
    s.bind(('', local_port)) 
    
    print(f"[*] Attempting connection to {target_ip} via local port {local_port}...")
    s.connect((target_ip, target_port))
    
    print("[+] CONNECTION SUCCESSFUL! The firewall let us through.")
    s.send(b"GET / HTTP/1.1\r\nHost: " + target_ip.encode() + b"\r\n\r\n")
    data = s.recv(1024)
    print(f"[+] Data received: {data[:50]}")
    s.close()

except PermissionError:
    print(f"[!] Local Port {local_port} is restricted by the OS.")
except Exception as e:
    print(f"[-] Connection failed: {e}")

