import socket
import threading
import lru_cache

host: str = "127.0.0.1"
port: int = 3101


def start(host: str, port: int):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.bind((host, port))
        except OSError as e:
            print(str(e))
            raise OSError("Server bind failed, check your server port config")

        s.listen(2) # define the number of clients that can wait in a queue before .accept()
        print("Waiting for a connection; server started —")

        def threaded_client(connection: socket.socket) -> None:
            connection.send(str.encode("Connected"))
            reply: str = ""
            while True:
                try: 
                    data: bytes = connection.recv(2048) # the number of bytes we are loading in
                    reply: str = data.decode("utf-8")
                
                    if not data:
                        print("Disconnected")
                        break
                    else:
                        print("Received: ", reply)
                        print("Sending: ", reply)

                    connection.sendall(reply.encode("utf-8"))
                except ConnectionResetError:
                    print(f"Connection has been reset: {ConnectionResetError}")
                    break

            print("Lost connection")
            connection.close()

        while True:
            connection, address = s.accept()
            print(f"Connected to: {address}")
            print(f"Socket object: {connection}")
            help(socket.socket.accept)

            t = threading.Thread(target=threaded_client, args=(connection,), daemon=True)
            t.start()