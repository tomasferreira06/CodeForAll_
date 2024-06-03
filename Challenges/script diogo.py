#!/usr/bin/env python3

import ipaddress
from scapy.all import ICMP, IP, sr1, TCP

# Define end host and TCP port range. Take care not to populate the host bits here.
network = "10.0.2.0/24"
ip_list = ipaddress.IPv4Network(network).hosts()
hosts_count = 0

for host in ip_list:
    print("Pinging", str(host), "- please wait...")
    response = sr1(
        IP(dst=str(host))/ICMP(),
        timeout=2,
        verbose=0
    )

    print(response)