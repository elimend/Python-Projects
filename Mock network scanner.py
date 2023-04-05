import socket

host = input("Enter the IP address or hostname to scan: ")

for port in range(1, 1000):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.1)
    result = s.connect_ex((host, port))
    if result == 0:
        print(f"Port {port}: Open")
    s.close()
