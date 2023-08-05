import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(2)

def portScanner(port, ip):
    if s.connect_ex((ip, port)):
        print("The port is closed")
    else:
        print("The port is open")

def get_ips(host):
    try:
        ips = socket.gethostbyname_ex(host)
    except socket.gaierror:
        ips=[]
        print("Invalid address.")
        quit()
    return ips[2]

print("Press 1 for entering domain name, else IP address: ")
choice = input()

if choice == '1':
    host = input("Enter the website URL you wish to scan: ")
    ips = get_ips(host)
    print("List of IPs:", ips)
else:
    ips = input("Please enter the IP you want to scan: ")
    ips = [ips]

port = int(input("Please enter the port you want to scan: "))

for ip in ips:
    portScanner(port, ip)