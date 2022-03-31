"""This module tests the cards module."""

import random
import pytest
import cards
from cards import CardsType


@pytest.fixture(name="deck")
def deck_fixture() -> CardsType:
    """Creates a card deck fixture.

    Returns:
      The new card deck.
    """

    return cards.create_deck()


def test_create_deck_returns_deck_of_52_cards(deck: CardsType) -> None:
    """Tests that newly created deck contains 52 playing cards."""

    # Arrange

    # Act

    # Asset
    assert len(deck) == 52


def test_create_deck_returns_deck_with_all_suits(deck: CardsType) -> None:
    """Tests that cards of all fours suits are present in a new deck."""

    # Arrange
    expected_suits = set(cards.Suit)

    # Act

    # Asset
    actual_suits = {card[0] for card in deck}
    assert actual_suits == expected_suits


def test_create_deck_returns_deck_with_all_values(deck: CardsType) -> None:
    """Tests that all values of cards are present in a new deck."""

    # Arrange
    expected_values = set(range(1, 14))

    # Act

    # Asset
    actual_values = {card[1] for card in deck}
    assert actual_values == expected_values


def test_shuffle_deck_shuffles_first_card(deck: CardsType) -> None:
    """Tests that the first card in a deck is changed after a shuffle."""

    # Arrange
    first_card = deck[0]

    # Ensure deterministic results
    random.seed(614)

    # Act
    cards.shuffle_deck(deck)

    # Asset
    assert deck[0] != first_card


def test_shuffle_deck_shuffles_last_card(deck: CardsType) -> None:
    """Tests that the last card in a deck is changed after a shuffle."""

    # Arrange
    last_card = deck[-1]

    # Ensure deterministic results
    random.seed(614)

    # Act
    cards.shuffle_deck(deck)

    # Asset
    assert deck[-1] != last_card


def test_deal_hand_returns_5_cards(deck: CardsType) -> None:
    """Tests that dealing a hand returns 5 cards, by default."""

    # Arrange

    # Act
    hand, _ = cards.deal_hand(deck)

    # Asset
    assert len(hand) == 5


def test_deal_hand_of_2_cards_returns_2_cards(deck: CardsType) -> None:
    """Tests that dealing a hand of 2 cards returns that size of hand."""

    # Arrange

    # Act
    hand, _ = cards.deal_hand(deck, 2)

    # Asset
    assert len(hand) == 2


def test_deal_hand_returns_cards_from_top_of_deck(deck: CardsType) -> None:
    """Tests that hands are dealt from the top of the deck."""

    # Arrange

    # Act
    hand, _ = cards.deal_hand(deck)

    # Asset
    assert hand == deck[:5]


def test_deal_hand_removes_n_cards_from_deck(deck: CardsType) -> None:
    """Tests that the remaining deck is reduced by the size of the hand."""

    # Arrange

    # Act
    _, remaining_deck = cards.deal_hand(deck)

    # Asset
    assert len(remaining_deck) == 52 - 5
