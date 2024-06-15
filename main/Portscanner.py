import socket

def port_scan(host, ports):
    open_ports = []
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

def main():
    host = input("Please enter hostname or IP address: ")
    ports = range(1, 1025)  # Scans the first 1024 ports
    open_ports = port_scan(host, ports)
    if open_ports:
        print(f"Open ports at {host}: {open_ports}")
    else:
        print(f"No open ports on {host} found.")

if __name__ == "__main__":
    main()