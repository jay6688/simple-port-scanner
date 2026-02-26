import socket

# 1. Set our new practice target
target_domain = "scanme.nmap.org"

# 2. Computers need IP addresses, not domain names. This translates it for us!
target_ip = socket.gethostbyname(target_domain) 

print(f"Scanning target: {target_ip}...")

# 3. Use range() to scan ports 1 through 100. (It stops just before 101)
for port in range(1, 101):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # 4. Dropped the timeout to 0.5 seconds so the loop runs faster
        s.settimeout(0.5) 
        
        result = s.connect_ex((target_ip, port)) 
        
        if result == 0:
            print(f"[+] Port {port} is OPEN!")
            try:
                # Tell the socket to receive up to 1024 bytes of data, decode it, and strip extra spaces
                banner = s.recv(1024).decode().strip()
                if banner:
                    print(f"    [>] Service Banner: {banner}")
            except Exception as e:
                # If the port doesn't send a banner, we just ignore it and move on
                pass
            
        s.close()

    except Exception as e:
        pass
    
