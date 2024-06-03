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


# Sends ICMP packets to every host in the specified network
def icmp_ping_sweep(network):

    ip_list = list(ipaddress.IPv4Network(network).hosts())

    active_hosts = 0
    
    for ip in ip_list:

        print(f"Pinging {ip} - please wait...")

        response = sr1(IP(dst=str(ip))/ICMP(), timeout=2, verbose=0)
        
        if response is None:

            print(f"{ip} is down or unresponsive.")

        elif response.haslayer(ICMP):

            if response[ICMP].type == 3 and response[ICMP].code in [1, 2, 3, 9, 10, 13]:

                print(f"{ip} is actively blocking ICMP traffic.")

            else:

                print(f"{ip} is responding.")

                active_hosts += 1
    
    print(f"Total active hosts: {active_hosts}")


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

        print("Select mode:")
        print("-------------------------")
        print("1. TCP Port Range Scanner")
        print("2. ICMP Ping Sweep")
        print("-------------------------")
        mode = input("Enter 1 or 2: ")

        if mode == '1':

            target_host = input("Enter the target host IP: ")
            port_input = input("Enter ports to scan (ex., 22,80,443 or 20-25): ")

            target_ports = get_ports(port_input)
            tcp_port_scan(target_host, target_ports)
            break

        elif mode == '2':

            network = input("Enter the network address (ex., 10.10.0.0/24): ")

            icmp_ping_sweep(network)
            break

        else:

            print("Invalid selection. Please try again!")
            input("Press Enter to continue..")
    

    