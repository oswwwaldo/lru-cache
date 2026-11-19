import socket

from server import host, port


class Network:
    def __init__(self, host: str, port: int):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port
        self.address = (self.host, self.port)
        self.id = self.connect()

        print(self.id)

    def __enter__(self):
        pass
    def __exit__(self):
        pass

    def connect(self) -> str:
        try:
            self.client.connect(self.address)
            return self.client.recv(2048).decode()
        except ConnectionResetError:
            print(f"Connection has been reset: {ConnectionResetError}")
            raise

    def send(self, data: str):
        try:
            self.client.sendall(str.encode(data))
            return self.client.recv(2048).decode()
        except OSError as e:
            print(e)

if __name__ == "__main__":
    n = Network(host, port)
    print(n.send("hi"))
    print(n.send("oswaldo"))