#!/bin/bash

"""This module listens for data on a socket an echoes it back to the client."""

import selectors
import socket
from typing import List, Tuple

HOST = "127.0.0.1"
PORT = 9000


def main() -> None:
    """Listens for data on a socket and echoes it back to the client."""

    selector = selectors.DefaultSelector()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        server_address = (HOST, PORT)
        server_socket.bind(server_address)
        server_socket.setblocking(False)
        server_socket.listen(5)

        selector.register(server_socket, selectors.EVENT_READ)

        while True:
            events: List[Tuple[selectors.SelectorKey, int]] = selector.select(timeout=3)

            if len(events) == 0:
                print("Waiting for events...")

            for event, _ in events:
                event_socket = event.fileobj

                if event_socket == server_socket:
                    connection, client_address = server_socket.accept()
                    connection.setblocking(False)
                    print(f"Accepted a connection from {client_address}")
                    selector.register(connection, selectors.EVENT_READ)
                else:
                    data = event_socket.recv(4096)
                    event_socket.send(data)


if __name__ == "__main__":
    main()
