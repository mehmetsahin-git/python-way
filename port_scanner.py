# Port Scanner - Day 1: Banner
import socket


print("=== PortScanner v0.1 ===")
target = input(" Target IP:")
start_port = int(input(" Start port:"))
end_port = int(input(" End port:"))

if start_port < 1 or end_port > 65535 :
    print("Error: ports must be between 1 and 65535")
elif start_port > end_port :
        print("Error: start port cannot be greater than end port")
else:
    
    for port in range(start_port, end_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
           print(f"port {port} is OPEN")
           s.close()
