"""This module tests the cards module."""

import random
import cards


def test_create_deck_returns_deck_of_52_cards() -> None:
    """Tests that newly created deck contains 52 playing cards."""

    # Arrange

    # Act
    deck = cards.create_deck()

    # Asset
    assert len(deck) == 52


def test_create_deck_returns_deck_with_all_suits() -> None:
    """Tests that cards of all fours suits are present in a new deck."""

    # Arrange
    expected_suits = set(cards.Suit)

    # Act
    deck = cards.create_deck()

    # Asset
    actual_suits = {card[0] for card in deck}
    assert actual_suits == expected_suits


def test_create_deck_returns_deck_with_all_values() -> None:
    """Tests that all values of cards are present in a new deck."""

    # Arrange
    expected_values = set(range(1, 14))

    # Act
    deck = cards.create_deck()

    # Asset
    actual_values = {card[1] for card in deck}
    assert actual_values == expected_values


def test_shuffle_deck_shuffles_first_card() -> None:
    """Tests that the first card in a deck is changed after a shuffle."""

    # Arrange
    deck = cards.create_deck()
    first_card = deck[0]

    # Ensure deterministic results
    random.seed(614)

    # Act
    cards.shuffle_deck(deck)

    # Asset
    assert deck[0] != first_card


def test_shuffle_deck_shuffles_last_card() -> None:
    """Tests that the last card in a deck is changed after a shuffle."""

    # Arrange
    deck = cards.create_deck()
    last_card = deck[-1]

    # Ensure deterministic results
    random.seed(614)

    # Act

    cards.shuffle_deck(deck)

    # Asset
    assert deck[-1] != last_card


def test_deal_hand_returns_5_cards() -> None:
    """Tests that dealing a hand returns 5 cards, by default."""

    # Arrange
    deck = cards.create_deck()

    # Act
    hand, _ = cards.deal_hand(deck)

    # Asset
    assert len(hand) == 5


def test_deal_hand_of_2_cards_returns_2_cards() -> None:
    """Tests that dealing a hand of 2 cards returns that size of hand."""

    # Arrange
    deck = cards.create_deck()

    # Act
    hand, _ = cards.deal_hand(deck, 2)

    # Asset
    assert len(hand) == 2


def test_deal_hand_returns_cards_from_top_of_deck() -> None:
    """Tests that hands are dealt from the top of the deck."""

    # Arrange
    deck = cards.create_deck()

    # Act
    hand, _ = cards.deal_hand(deck)

    # Asset
    assert hand == deck[:5]


def test_deal_hand_removes_n_cards_from_deck() -> None:
    """Tests that the remaining deck is reduced by the size of the hand."""

    # Arrange
    deck = cards.create_deck()

    # Act
    _, remaining_deck = cards.deal_hand(deck)

    # Asset
    assert len(remaining_deck) == 52 - 5
