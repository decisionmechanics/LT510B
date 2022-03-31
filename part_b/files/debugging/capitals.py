#!/bin/bash

"Quiz game where the player has to identify the capital city of countries."

from enum import IntEnum
import json
import random
from typing import Dict, List


class YesNo(IntEnum):
    "Represents a binary response."
    YES = 0
    NO = 1


CapitalsType = Dict[str, str]


def load_capitals(document_path: str) -> CapitalsType:
    """Loads the quiz data from a JSON document.

    Args:
      document_path: Location of JSON document containing the quiz data.

    Returns:
      The countries and their capital cites.
    """

    with open(document_path, encoding="utf8") as json_file:
        return {
            capital["country"]: capital["capital"] for capital in json.load(json_file)
        }


def choose_random_country(countries: List[str]):
    """Selects a random country.

    Args:
      countries: List of countries to choose from.
    """

    return countries[random.randint(0, len(countries) - 1)]


def choose_candidate_capitals(capitals: CapitalsType, chosen_country: str) -> List[str]:
    """Select 4 capital cities.

    Args:
      capitals: Capital cities.
      chosen_country: Country that's capital must be included in the selection.
    """

    other_capitals = [
        capital for country, capital in capitals.items() if country != chosen_country
    ]

    random.shuffle(other_capitals)
    other_capitals = other_capitals[:3]

    candidate_capitals = [capitals[chosen_country]] + other_capitals[:3]
    random.shuffle(candidate_capitals)

    return candidate_capitals


def play_once(countries: List[str], capitals: CapitalsType) -> bool:
    """Play one round of the quiz.

    Guess one country's capital city from a choice of 4.

    Args:
      countries: Countries to choose from.
      capitals: Capital cities.

    Returns:
      Whether the correct capital was chosen or not.
    """

    chosen_country = choose_random_country(countries)
    chosen_capital = capitals[chosen_country]
    candidate_capitals = choose_candidate_capitals(capitals, chosen_country)

    print(f"What is the capital of {chosen_country}?")

    for i, candidate_capital in enumerate(candidate_capitals):
        print(f"  {i + 1}. {candidate_capital}")

    selection = int(input("Enter you answer [1-4]: "))

    correct = candidate_capitals[selection - 1] == chosen_capital

    if correct:
        print("Well done!")
    else:
        print(f"Sorry. The capital of {chosen_country} is {chosen_capital}.")

    return correct


def check_continue() -> YesNo:
    """Asks if the user wish to play again.

    Returns:
      User's response.
    """

    yes = not input("Do you wish to play again? (Y/n) ").upper().startswith("N")

    return YesNo.YES if yes else YesNo.NO


def main() -> None:
    """Performs the main task of the script."""

    capitals = load_capitals("capitals.json")
    countries = list(capitals.keys())

    attempts = 0
    correct = 0

    playing = True

    while playing:
        if play_once(countries, capitals):
            correct += 1

        attempts += 1

        print(f"You have answered {correct} correctly out of {attempts}.")

        playing = check_continue() == YesNo.YES


if __name__ == "__main__":
    main()
