import socket
import threading
from queue import Queue

# 1. Target Setup
target_domain = "scanme.nmap.org"
target_ip = socket.gethostbyname(target_domain)
print(f"[*] Scanning target: {target_ip}...")

# 2. Create the Queue (The stack of work)
queue = Queue()

# 3. The Scanning Function (What each worker actually does)
def scan_port(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5) 
        result = s.connect_ex((target_ip, port))
        
        if result == 0:
            print(f"[+] Port {port} is OPEN!")
            try:
                banner = s.recv(1024).decode().strip()
                if banner:
                    print(f"    [>] Service Banner: {banner}")
            except:
                pass
        s.close()
    except:
        pass

# 4. The Worker Function
def worker():
    # As long as there are ports left in the queue, keep grabbing them
    while not queue.empty():
        port = queue.get()
        scan_port(port)
        queue.task_done()

# 5. Fill the Queue with ports 1 through 1024 (The common ports)
for port in range(1, 1025):
    queue.put(port)

# 6. Spawn 100 Workers (Threads)
thread_list = []
for _ in range(100):
    thread = threading.Thread(target=worker)
    thread_list.append(thread)
    thread.start()

# 7. Wait for all workers to finish before exiting
for thread in thread_list:
    thread.join()

print("[*] Scan complete!")
