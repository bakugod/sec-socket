import socket

def main():
    host_ip, server_port = "127.0.0.1", 9999
    tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_client.connect((host_ip, server_port))
    data = input("data: ")
    tcp_client.send(data.encode())
    received = tcp_client.recv(1024)
    print("Bytes Sent:     {}".format(data))
    print("Bytes Received: {}".format(received.decode()))
    tcp_client.close()


while(True):
    try:
        main()
    except EOFError:
        exit()
    except KeyboardInterrupt:
        exit()