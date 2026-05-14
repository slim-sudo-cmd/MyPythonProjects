import socket

target = "192.168.4.43"
port = 7800

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)

try:
    s.connect((target, port))
    # Send a standard HTTP request just in case it's a hidden web panel
    s.send(b"GET / HTTP/1.1\r\nHost: 192.168.4.43\r\n\r\n")
    response = s.recv(1024)
    print(f"[+] Response: {response.decode(errors='ignore')}")
except Exception as e:
    print(f"[-] No response: {e}")
finally:
    s.close()

