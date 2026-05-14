import socket

def get_gateway_and_test():
    # This trick finds your local IP and the gateway by "pretending" to connect
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        # Usually, the gateway is the .1 or .254 of your subnet
        gateway_guess = local_ip.rsplit('.', 1)[0] + '.1'
        print(f"Internal IP: {local_ip}")
        print(f"Likely Gateway: {gateway_guess}")
        
        # Test if the gateway has an open management port (SSH)
        t = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        t.settimeout(1)
        if t.connect_ex((gateway_guess, 22)) == 0:
            print(f"CRITICAL: Gateway {gateway_guess} has SSH (Port 22) OPEN.")
        else:
            print("Port 22 is closed on gateway.")
        t.close()
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        s.close()

get_gateway_and_test()

