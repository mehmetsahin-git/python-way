# Port Scanner - Day 1: Banner
import socket


def scan_port(target, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((target, port))
    s.close()
    if result == 0:
          return True
    else:
        return False


print("=== Port Scanner v0.1 ===")
while True:
    target = input("Target IP: ")
    start_port = int(input("Start port: "))
    end_port = int(input("End port: "))

    if start_port < 1 or end_port > 65535:
        print("Error: ports must be between 1 and 65535")
    elif start_port > end_port:
        print("Error: start port cannot be greater than end port")
    else: 
        for port in range(start_port, end_port + 1):
            if scan_port(target, port):
                print(f"port {port} is OPEN")
        print("Scan complete.")

    again = input("Scan again? (y/n): ")
    if again == "n":
        break