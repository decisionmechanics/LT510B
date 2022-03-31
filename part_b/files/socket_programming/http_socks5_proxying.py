# !/bin/bash

"""This script accesses learningtree.com via a SOCKS5 proxy.

pip install 'requests[socks]' is required.
"""

import requests


def main() -> None:
    """Accesses learningtree.com via a SOCKS5 proxy."""

    response = requests.get(
        "https://learningtree.com",
        proxies=dict(
            http="socks5://dante:platypus@127.0.0.1:1080",
            https="socks5://dante:platypus@127.0.0.1:1080",
        ),
    )

    print(response.content)
