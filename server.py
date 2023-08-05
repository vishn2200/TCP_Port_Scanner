import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 12345)) # Bind to a specific address and port
s.listen(5) # Listen for incoming connections
print("Port Scanner Server is running...")

def portScanner(port, ip):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    if s.connect_ex((ip, port)):
        return "The port is closed"
    else:
        return "The port is open"

while True:
    conn, addr = s.accept() # Accept a new connection
    print('Connection from:', addr)
    conn.sendall("Welcome to Port Scanner Server!".encode())

    # Receive data from client
    data = conn.recv(1024).decode().strip()
    if data == '1':
        host = conn.recv(1024).decode().strip()
        ips = socket.gethostbyname_ex(host)[2]
        conn.sendall("List of IPs: {}".format(ips).encode())
    else:
        ips = [conn.recv(1024).decode().strip()]
    
    port = int(conn.recv(1024).decode().strip())
    
    for ip in ips:
        result = portScanner(port, ip)
        conn.sendall(result.encode())

    conn.close()