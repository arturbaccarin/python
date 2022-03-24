import ipaddress

ip = '192.168.0.1'

endereco = ipaddress.ip_address(ip)
rede = ipaddress.ip_network(ip)

print(endereco + 256)
print(rede)