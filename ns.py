import subprocess
from concurrent.futures import ThreadPoolExecutor
import socket




def ping_host(ip):
    result = subprocess.run(["ping", "-c", "1", ip], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if result.returncode == 0:
        return True
    else:
        return False
    

def host_name(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except socket.herror:
         return "unknown"


def scan_network(base):
    ips = [f"{base}.{i}" for i in range(1, 256)]
    with ThreadPoolExecutor(max_workers=100) as executor:
        results = executor.map(ping_host, ips)
    for ip, result in zip(ips, results):
        hostname = host_name(ip)
        if result == True:
             print(f"{ip} is alive - {hostname}")


scan_network("192.168.1")    
