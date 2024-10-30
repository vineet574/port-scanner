# main.py

from port_scanner import get_open_ports

# Test with IP address
print(get_open_ports("209.216.230.240", [440, 445]))

# Test with URL and verbose output
print(get_open_ports("scanme.nmap.org", [20, 80], True))
