import os
import subprocess
from typing import Final, Literal

# from server import host, port
import server


CLEAR_WIN: Final = "cls"
CLEAR_UNIX: Final = "clear"

DEBUG_MODE: bool = True

def clear_terminal() -> None:
    """Clear the console screen across Windows, macOS, and Linux."""
    # `nt` indicates Windows; otherwise, the OS is Unix-like (`posix`).
    command: Literal["cls", "clear"] = CLEAR_WIN if os.name == "nt" else CLEAR_UNIX
    
    # shell=True is required on Windows because `cls` is a built-in cmd, not an executable
    subprocess.run(command, check=False, shell=True)

def debug_mode():
    clear_terminal()
    cache = LRUCache(capacity = 3, duration = 10)
    cache.put("A", 1)
    cache.put("B", 2)
    cache.put("C", 3)

    cache.get("A")

    cache.put("D", 4)
    cache.get("B")

    print(cache)
    print(list(cache.dict.items()))

def main() -> None:
    print("11/18/26 — 2:58PM")
    server.start(server.host, server.port)

if __name__ == "__main__":
    main()

# >>> import socket
# >>> c = socket.create_connection(("127.0.0.1", 3013))
# >>> c.sendall(b"hello")
# >>> c.recv(2048)
# b'hello'
# >>> c.close()