import psutil
network_interfaces = psutil.net_if_stats()
print(network_interfaces.keys())