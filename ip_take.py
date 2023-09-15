from jumbo import *
from jumbo import url
from socket import gethostbyname
from urllib.parse import urlparse

parsed_url = urlparse(url)
ip_address = parsed_url.hostname
port = parsed_url.port
ip_address2 = gethostbyname(ip_address)

if port is None:
    port = 80

print(f"IP-адрес: {ip_address2}")
print(f"Порт: {port}")
