# Port Scanner - Day 1: Banner

name = input(" User Name:")
print(f"Hello {name}")
target = input(" Target IP:")
start_port = int(input(" Start port:"))
end_port = int(input(" End port:"))

if start_port < 1 or end_port > 65535 :
    print("Error: ports must be between 1 and 65535")
elif start_port > end_port :
        print("Error: start port cannot be greater than end port")
else:
    print(f"Valid range: {start_port} to {end_port}")
    print(f"Scanning {target} from port {start_port} to {end_port}")
