#!/bin/bash

"""This module listens for data on a socket an echoes it back to the client."""

import asyncio
from asyncio import AbstractEventLoop
import socket
from typing import NoReturn

HOST = "127.0.0.1"
PORT = 9000


async def listen_for_connections(
    server_socket: socket.socket, loop: AbstractEventLoop
) -> NoReturn:
    """Listens for incoming connections.

    Args:
      server_socket: Socket to listen on.
      loop: Event loop.
    """
    while True:
        connection, client_address = await loop.sock_accept(server_socket)
        connection.setblocking(False)
        print(f"Accepted a connection from {client_address}")
        asyncio.create_task(echo(connection, loop))


async def echo(connection: socket.socket, loop: AbstractEventLoop) -> None:
    """Echoes data back to the client.

    Args:
      socket: Client socket.
      loop: Event loop.
    """

    try:
        while True:
            data = await loop.sock_recv(connection, 1024)

            if not data:
                break

            await loop.sock_sendall(connection, data)

    finally:
        connection.close()


async def main() -> None:
    """Listens for data on a socket and echoes it back to the client."""

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        server_address = (HOST, PORT)
        server_socket.bind(server_address)
        server_socket.setblocking(False)
        server_socket.listen(5)

        print(f"Listening for connections on {server_address}")

        await listen_for_connections(server_socket, asyncio.get_event_loop())


if __name__ == "__main__":
    asyncio.run(main())
