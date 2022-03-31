# !/bin/bash

"""This script accesses google.com via a SOCKS5 proxy."""

import socket
import socks


def main() -> None:
    """Accesses google.com via a SOCKS5 proxy."""

    client_socket = socks.socksocket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.set_proxy(
        socks.SOCKS5, "127.0.0.1", username="dante", password="platypus"
    )

    client_socket.connect(("www.google.com", 80))
    client_socket.sendall(b"GET / HTTP/1.1\r\n\r\n")
    print(client_socket.recv(4096))


if __name__ == "__main__":
    main()
