import asyncio
import socket
import socketserver

data: str = ""

class Handler_TCPServer(socketserver.BaseRequestHandler):
    def handle(self):
        # self.request - TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        data = self.data
        print(data)

        # print("{} sent:".format(self.client_address[0]))
        # print(self.data)
        # just send back ACK for data arrival confirmation
        self.request.sendall("ACK from TCP Server".encode())


class Handler(object):
    """
    The TCP Server class for demonstration.
    """

    def __init__(self, _type, close_message, close_timer=None, host="localhost", port=9999):
        self.type = _type
        self.close_message = close_message
        self.close_timer = close_timer
        self.host = host
        self.port = port

    def start(self):
        if self.type == "tcp":
            self.socketserver = socketserver.TCPServer(
                (self.host, self.port), Handler_TCPServer)
            print(data)
        if self.type == "udp":
            self.socketserver = socketserver.UDPServer(
                (self.host, self.port), Handler_TCPServer)
        if self.close_timer == None:
            self.socketserver.serve_forever()
        if self.close_timer != None:
            self.socketserver.serve_forever()

    def finish(self):
        self.socketserver.server_close()
        print(self.close_message)


if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    tcp_server = Handler("tcp", "Server Stopped", None, HOST, PORT)
    tcp_server.start()
