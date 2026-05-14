import socket

def udp_probe(ip, port):
    try:
        # Switch to DGRAM for UDP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(4) 
        
        # Standard "Hello" or Discovery strings
        probes = [b"\x00", b"HELP\n", b"\x01\x00\x00\x00"]
        
        for probe in probes:
            print(f"[*] Probing {ip}:{port} with {probe.hex()}...")
            s.sendto(probe, (ip, port))
            try:
                data, addr = s.recvfrom(1024)
                print(f"[+] RESPONSE from {addr}: {data}")
            except socket.timeout:
                continue 
        s.close()
    except Exception as e:
        print(f"[!] Socket Error: {e}")

target_ip = "192.168.1.1"
# Port 5 (Remote Job Entry) is almost always a ghost; 73 is the focus
udp_probe(target_ip, 73)

