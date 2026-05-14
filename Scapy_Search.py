from scapy.all import ARP, Ether, srp

def scan_for_ghosts(ip_range):
    # Create an ARP request packet
    # Ether(dst="ff:ff:ff:ff:ff:ff") broadcasts it to everyone
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp

    print(f"Scanning {ip_range}... looking for ghosts.")
    result = srp(packet, timeout=3, verbose=0)[0]

    for sent, received in result:
        print(f"IP: {received.psrc} | MAC: {received.hwsrc}")

scan_for_ghosts("192.168.48.0/24")
