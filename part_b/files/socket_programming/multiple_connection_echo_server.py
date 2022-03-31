#!/bin/bash

"""This module listens for data on a socket an echoes it back to the client."""

import socket

HOST = "127.0.0.1"
PORT = 9000


def main() -> None:
    """Listens for data on a socket and echoes it back to the client."""

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        server_address = (HOST, PORT)
        server_socket.bind(server_address)
        server_socket.listen(5)

        print(f"Listening for connections on {server_address}")

        while True:
            connection, client_address = server_socket.accept()
            print(f"Accepted a connection from {client_address}")

            while True:
                data = connection.recv(4096)

                if not data or data == b"\r\n":
                    break

                connection.sendall(data)

            connection.close()


if __name__ == "__main__":
    main()
