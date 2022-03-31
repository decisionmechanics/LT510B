#!/bin/bash

"""Simple number guessing game played over telnet."""

import random
import socket
from typing import Tuple

HOST = "127.0.0.1"
PORT = 9000


def check_guess(guess: int, attempts: int, secret: int) -> Tuple[bool, str]:
    """Checks whether a guess is correct.

    Args:
      guess: The guess.
      attempts: The number of guesses made so far (including this one).
      secret: The correct answer.

    Returns:
      A tuple that denotes if the guess was correct and an accomapaning message.
    """

    if guess < secret:
        return False, f"It's bigger than {guess}. Try again."
    if guess > secret:
        return False, f"It's smaller than {guess}. Try again."

    return (
        True,
        f"Congratulations. You guessed I was thinking of {secret} in {attempts} attempt(s).",
    )


def main() -> None:
    """Plays a round of the game."""

    secret = random.randint(1, 100)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        server_address = (HOST, PORT)
        server_socket.bind(server_address)
        server_socket.listen(5)

        print(f"Listening for connections on {server_address}")

        connection, client_address = server_socket.accept()
        print(f"Accepted a connection from {client_address}")

        attempts = 0

        connection.sendall(b"What number between 1 and 100 am I thinking of?\r\n")

        while True:
            buffer = b""

            while True:
                data = connection.recv(4096)

                buffer += data

                if buffer.endswith(b"\r\n"):
                    buffer = buffer[0:-2]

                    break

                connection.sendall(data)

            guess = int(buffer.decode("utf-8"))

            attempts += 1

            success, message = check_guess(guess, attempts, secret)

            connection.sendall(bytes(f"{message}\r\n", "utf-8"))

            if success:
                break


if __name__ == "__main__":
    main()
