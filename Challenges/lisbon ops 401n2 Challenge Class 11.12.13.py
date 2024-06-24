import random
import ipaddress
import os
from scapy.all import sr1, IP, TCP, ICMP


# Scans specified ports/port range for the specified host
def tcp_port_scan(host, ports):

    for port in ports:

        # Randomize the TCP source port
        src_port = random.randint(1024, 65535)
        
        # Create the TCP SYN packet with a randomized source port
        pkt = IP(dst=host)/TCP(sport=src_port, dport=port, flags='S')
        
        response = sr1(pkt, timeout=2, verbose=0)

        if response is None:

            print(f"Port {port}: Filtered (no response)")
    
        elif response.haslayer(TCP):

            if response[TCP].flags == 0x12:  # SYN-ACK Packet
                
                rst_pkt = IP(dst=host)/TCP(sport=src_port, dport=port, flags='R')

                sr1(rst_pkt, timeout=2, verbose=0)
                print(f"Port {port}: Open")

            elif response[TCP].flags == 0x14:  # RST-ACK Packet

                print(f"Port {port}: Closed")

            else:

                print(f"Port {port}: Filtered (unexpected flags {response[TCP].flags})")
        else:

            print(f"Port {port}: Filtered (no TCP layer)")


def scan_host(host, ports):

    print(f"Pinging {host} - please wait...")

    response = sr1(IP(dst=str(host)) / ICMP(), timeout=2, verbose=0)

    if response is None:

        print(f"{host} is down or unresponsive.")

    elif response.haslayer(ICMP):

        if response[ICMP].type == 3 and response[ICMP].code in [1, 2, 3, 9, 10, 13]:

            print(f"{host} is actively blocking ICMP traffic.")

        else:

            print(f"{host} is responding.")
            tcp_port_scan(host, ports)


# Sends ICMP packets to every host in the specified network
def scan_network(network, ports):

    ip_list = list(ipaddress.IPv4Network(network).hosts())

    for ip in ip_list:

        scan_host(str(ip), ports)


# Organizes the ports independent of being by range or single ports
def get_ports(port_input):

    ports = set()
    parts = port_input.split(',')

    for part in parts:

        if '-' in part:

            start, end = part.split('-')
            ports.update(range(int(start), int(end) + 1))

        else:

            ports.add(int(part))
    return sorted(ports)

if __name__ == "__main__":

    while True:
    
        os.system('cls' if os.name == 'nt' else 'clear')

        scan_type = input("Enter scan type (host/network): ")

        if scan_type.lower() == "host":

            hosts_input = input("Enter the target host IP (ex. 8.8.8.8): ")
            port_input = input("Enter ports to scan (ex., 22,80,443 or 20-25): ")
            target_ports = get_ports(port_input)

            scan_host(hosts_input, target_ports)
            break

        elif scan_type.lower() == "network":

            network = input("Enter the target network address (ex., 10.10.0.0/24): ")
            port_input = input("Enter ports to scan (ex., 22,80,443 or 20-25): ")
            target_ports = get_ports(port_input)

            scan_network(network, target_ports)
            break

        else:
            print("Invalid selection. Please enter 'host' or 'network'.")

    print("Scan completed.")
    
    

    