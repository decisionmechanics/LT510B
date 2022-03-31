#!/bin/bash

"""Fetches quotes from a web API.

Args:
  Optional number (int) of quotes to retrieve. Defaults to 3.
"""

import sys
import time
from typing import List, TypedDict
import requests

Quote = TypedDict("Quote", {"text": str, "from": str})

INSPIRATIONAL_QUOTES_URL = (
    "https://inspirational-quotes.azurewebsites.net/api/InspirationalQuotes"
)


def fetch_quote(url: str, session: requests.Session) -> Quote:
    """Fetches a quote from a web API.

    Args:
      url: Web API endpoint.
      session: An active session.

    Returns
      A quote.
    """

    with session.get(url) as response:
        return response.json()


def fetch_quotes(quote_count: int) -> List[Quote]:
    """Fetches quotes from a web API.

    Args:
      quote_count: Number of quotes to fetch.

    Returns:
      A list of quotes.
    """

    with requests.Session() as session:
        return [
            fetch_quote(INSPIRATIONAL_QUOTES_URL, session) for _ in range(quote_count)
        ]


def main() -> None:
    """Retrieves quotes from a web API and displays them."""

    quote_count = int(sys.argv[1]) if len(sys.argv) > 1 else 3

    start_time = time.perf_counter()

    quotes = fetch_quotes(quote_count)

    duration = time.perf_counter() - start_time

    for quote in quotes:
        text = quote["text"].strip("“")

        print(f'"{text}" -- {quote["from"]}')

    print(f"Fetched {quote_count} inspirational quote(s) in {duration:.2f} seconds")


if __name__ == "__main__":
    main()
