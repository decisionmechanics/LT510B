#!/bin/bash

"""This module represents a deck of playing cards.

You can
- create a deck
- shuffle the deck
- deal a hand
"""

from enum import IntEnum
import random
from typing import List, Tuple


class Suit(IntEnum):
    """Represents the suit of a playing card."""

    CLUBS = 0
    DIAMONDS = 1
    HEARTS = 2
    SPADES = 3


CardType = Tuple[Suit, int]
CardsType = List[CardType]


def create_deck() -> CardsType:
    """Creates a deck of 52 cards.

    Returns:
      The new deck of cards.
    """

    return [(suit, value) for value in range(1, 14) for suit in Suit]


def shuffle_deck(deck: CardsType) -> None:
    """Shuffles a deck of cards.

    The deck is shuffle in-place.

    Args:
      deck: Deck of playing cards to be shuffled.
    """

    random.shuffle(deck)


def deal_hand(deck: CardsType, count: int = 5) -> Tuple[CardsType, CardsType]:
    """Deals a hand of cards.

    Args:
      count: Numbers of cards to deal (defaults to 5).

    Returns:
      A tuple compromising the dealt hand and the remaining deck.
    """

    hand = deck[:count]
    remaining_deck = deck[count:]

    return hand, remaining_deck


def main() -> None:
    """Creates and uses a sample deck of playing cards."""

    deck = create_deck()
    shuffle_deck(deck)

    print(f"The initial deck contains {len(deck)} cards.")

    hand, deck = deal_hand(deck)
    print(hand)

    hand, deck = deal_hand(deck)
    print(hand)

    print(f"The remaining deck contains {len(deck)} cards.")


if __name__ == "__main__":
    main()
