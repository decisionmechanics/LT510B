#!/bin/bash
# pylint: disable=unnecessary-pass

"""This module represents a bank account.

You can make deposits, withdraw money and check the balance.

Usage:
  account = create_bank_account()
  account.deposit(100)
"""

import datetime as dt
import time
from typing import List, TypedDict


class SpecialOfferDictionary(TypedDict):
    """Represents a special offer returned from a web API.

    Attributes:
      description: The description of the offer.
      expires: Date on which the offer expires.
    """

    description: str
    expires: dt.date


class BankAccountError(Exception):
    """Custom bank account exception."""

    pass


# This isn't typed as typing function attributes is distracting
def create_bank_account(initial_balance=0):
    """Creates a bank account with a default balance of 0.

    Attributes:
      deposit (function): Increases the balance by the specified amount.
      withdraw (function): Decreases the balance by the specified amount.

    Args:
      initial_balance (float): The starting balance.

    Returns:
      A bank account closure.
    """

    balance = initial_balance

    def deposit(amount: float) -> float:
        """Increases the balance on the account.

        Args:
          amount: Sum to deposit.

        Returns:
          The new balance.
        """

        nonlocal balance

        balance += amount

        return balance

    def withdraw(amount: float) -> float:
        """Decreases the balance on the account.

        There's no overdraft facility. You can't withdraw money you don't have.

        Args:
          amount: Sum to deposit.

        Returns:
          The new balance.
        """

        nonlocal balance

        if amount > balance:
            raise BankAccountError(
                f"You can't withdraw {amount} given a balance of {balance}"
            )

        balance -= amount

        return balance

    def bank_account() -> float:
        return balance

    bank_account.deposit = deposit
    bank_account.withdraw = withdraw

    return bank_account


def fetch_special_offers() -> List[SpecialOfferDictionary]:
    """Fetches a list of special offers.

    Returns:
      The current offers.
    """

    time.sleep(3)

    return [{"description": "Free shipping.", "expires": dt.date(2021, 12, 31)}]


def main() -> None:
    """Creates and uses a sample bank account."""

    savings_account = create_bank_account(100)
    print(savings_account())
    savings_account.withdraw(50)
    print(savings_account())
    savings_account.deposit(25)
    print(savings_account())
    savings_account.withdraw(100)


if __name__ == "__main__":
    main()
