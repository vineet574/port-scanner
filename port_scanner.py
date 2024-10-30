# port_scanner.py

import socket
from common_ports import ports_and_services

def get_open_ports(target, port_range, verbose=False):
    open_ports = []

    # Helper function to validate IP
    def is_valid_ip(ip):
        try:
            socket.inet_aton(ip)
            return True
        except socket.error:
            return False

    # Resolve target to IP or check if it's an IP
    try:
        if is_valid_ip(target):
            ip_address = target
            url = None
        else:
            ip_address = socket.gethostbyname(target)
            url = target
    except socket.gaierror:
        return "Error: Invalid hostname" if not is_valid_ip(target) else "Error: Invalid IP address"

    # Scan ports within range
    for port in range(port_range[0], port_range[1] + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)  # Short timeout for faster scanning
        result = sock.connect_ex((ip_address, port))
        if result == 0:
            open_ports.append(port)
        sock.close()

    # Prepare verbose output if requested
    if verbose:
        output = f"Open ports for {url if url else ip_address} ({ip_address})\n"
        output += "PORT     SERVICE\n"
        for port in open_ports:
            service = ports_and_services.get(port, 'unknown')
            output += f"{port:<9}{service}\n"
        return output.strip()

    return open_ports
