import socket
import ipaddress
import time
import threading
from concurrent.futures import ThreadPoolExecutor

services = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    3389: "RDP",
    5355: "LLMNR",
    8080: "HTTP-Alt"
}

expected_ports = [5355]
open_ports = []
lock = threading.Lock()


def scan_port(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((target, port))
        s.close()
        if result == 0:
            service = services.get(port, "Unknown")
            with lock:
                print(f"port {port} ({service}) is OPEN")
                open_ports.append(port)
    except socket.error:
        pass


def is_valid_target(target):
    try:
        ipaddress.ip_address(target)
        return True
    except ValueError:
        return False


print("=== Port Scanner v0.1 ===")
while True:
    target = input("Target IP: ")
    try:
        start_port = int(input("Start port: "))
        end_port = int(input("End port: "))
    except ValueError:
        print("Error: ports must be numbers")
        continue

    if start_port < 1 or end_port > 65535:
        print("Error: ports must be between 1 and 65535")
    elif start_port > end_port:
        print("Error: start port cannot be greater than end port")
    elif not is_valid_target(target):
        print("Error: invalid target")
    else:
        open_ports = []
        baslangic = time.time()
        with ThreadPoolExecutor(max_workers=100) as executor:
            for port in range(start_port, end_port + 1):
                executor.submit(scan_port, target, port)
        sure = time.time() - baslangic
        print("Scan complete.")
        open_ports.sort()
        print(f"Found {len(open_ports)} open ports: {open_ports}")
        print(f"Scan took {sure:.2f} seconds")

        # whitelist check and report file
        with open("scan_report.txt", "w") as f:
            f.write(f"Target: {target}\n")
            f.write(f"Time: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
            for p in open_ports:
                service = services.get(p, "Unknown")
                if p in expected_ports:
                    status = "normal"
                else:
                    status = "SUSPICIOUS"
                print(f"port {p} ({service}): {status}")
                f.write(f"port {p} ({service}): {status}\n")

    again = input("Scan again? (y/n): ")
    if again == "n":
        break