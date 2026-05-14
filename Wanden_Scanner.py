import socket

target = "192.168.48.1"
port = 22

try:
    s = socket.socket()
    s.settimeout(2)
    s.connect((target, port))
    # SSH servers send a 'banner' immediately upon connection
    banner = s.recv(1024)
    print(f"Service Banner: {banner.decode().strip()}")
    s.close()
except Exception as e:
    print(f"Could not grab banner: {e}")

