#!/bin/bash

"""Decrypts data in top_secret.bin.

The data was encrypted using AES-128.

The BASE64 encoding of the original encyption key is:

  b"6p7i52YHsSwO4Wt4XXJhZA=="
"""

import base64
from Crypto.Cipher import AES

KEY = b"6p7i52YHsSwO4Wt4XXJhZA=="


def main() -> None:
    """Decrypts top_secret.bin and displays its contents as plaintext."""

    with open("../../data/top_secret.bin", "rb") as encrypted_file:
        nonce = encrypted_file.read(16)
        tag = encrypted_file.read(16)
        ciphertext = encrypted_file.read()

    decryption_key = base64.b64decode(KEY)
    cipher = AES.new(decryption_key, AES.MODE_EAX, nonce)
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)

    print(plaintext.decode("utf-8"))


if __name__ == "__main__":
    main()
