import socket

target_ip = "192.168.1.1"
target_port = 73

# We use UDP (DGRAM)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(5)

try:
    # We don't 'bind' locally (to avoid permission denied)
    # We just send a probe to see if it triggers a leak
    print(f"[*] Probing Port 73 on {target_ip}...")
    sock.sendto(b"\x00\x00\x00\x00", (target_ip, target_port))
    
    data, addr = sock.recvfrom(1024)
    print(f"[+] DATA RECEIVED from {addr}: {data.hex()}")
except Exception as e:
    print(f"[!] No data returned, but packet was sent: {e}")

