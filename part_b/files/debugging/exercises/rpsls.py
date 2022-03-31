"""Rock Paper Scissors Lizard Spock game."""

from enum import IntEnum
import random


class Action(IntEnum):
    """Represents the actions players can take."""

    ROCK = 0
    PAPER = 1
    SCISSORS = 2
    LIZARD = 3
    SPOCK = 4


def parse_action(text):
    """Translates the player's input into an Action.

    Args:
      text (str): Choice typed by the player.

    Returns:
      The Action that represents the player's input.
    """

    actions = {
        "R": Action.ROCK,
        "P": Action.PAPER,
        "S": Action.SCISSORS,
        "L": Action.LIZARD,
        "K": Action.SPOCK,
    }

    return actions[text]


def get_user_action():
    """Prompts the player to specify an action.

    Returns:
      The action (Action) selected by the player.
    """

    action = None

    while action is None:
        input_text = (
            input("Enter a choice ([R]ock, [P]aper, [S]cissors, [L]izard or Spoc[K]): ")
            .strip()
            .upper()
        )

        if len(input_text) > 0 and input_text[0] in "RPSLK":
            action = parse_action(input_text[0])

    return action


def get_computer_action():
    """Chooses a random action for the computer.

    Returns:
      A random Action.
    """

    return Action(random.randint(0, len(Action) - 1))


def determine_action_winner(action_1, action_2):
    """Describes the result of a round.

    Args:
      action1 (Action): The subject action.
      action2 (Action): The object action.

    Returns:
      A message (str) that describes the outcome.
    """

    print(action_1, action_2)

    result = None

    if (action_1, action_2) == (Action.ROCK, Action.SCISSORS):
        result = "Rock blunts scissors!"
    elif (action_1, action_2) == (Action.ROCK, Action.LIZARD):
        result = "Rock smashes lizard!"
    elif (action_1, action_2) == (Action.PAPER, Action.ROCK):
        result = "Paper covers rock!"
    elif (action_1, action_2) == (Action.PAPER, Action.SPOCK):
        result = "Paper disproves Spock!"
    elif (action_1, action_2) == (Action.SCISSORS, Action.PAPER):
        result = "Scissors cut paper!"
    elif (action_1, action_2) == (Action.SCISSORS, Action.LIZARD):
        result = "Scissors decapitate lizard!"
    elif (action_1, action_2) == (Action.LIZARD, Action.PAPER):
        result = "Lizard eats paper1"
    elif (action_1, action_2) == (Action.LIZARD, Action.SPOCK):
        result = "Lizard poisons Spock!"
    elif (action_1, action_2) == (Action.SPOCK, Action.ROCK):
        result = "Spock vapourises rock!"
    elif (action_1, action_2) == (Action.SPOCK, Action.SCISSORS):
        result = "Spock smashes scissors!"

    return result


def determine_outcome(user_action, computer_action):
    """Decides who won the round.

    Args:
      user_action (Action): The choice made by the player.
      computer_action (Action): The choice made by the computer.

    Returns:
      Tuple of a (str) message and True/False depending on whether the player
      won.

      For example, ("You win!", True)
    """

    if user_action == computer_action:
        return ("Tie!", False)

    user_won = determine_action_winner(user_action, computer_action)

    if user_won:
        return (f"{user_won} You win!", True)

    computer_won = determine_action_winner(computer_action, user_action)

    if computer_won:
        return (f"{computer_won} You lose. :(", False)

    assert False, "Indeterminent outcome"


def determine_whether_quit():
    """Asks whether the player wishes to quit the game.

    Returns:
      True if the player wishes to quit. False otherwise.
    """

    return (
        input("Would you like to play another round? (Y/n): ")
        .strip()
        .upper()
        .startswith("N")
    )


def play_round():
    """Plays a single round of the game.

    Returns:
      True if the player won the round. False otherwise.
    """

    user_action = get_user_action()
    computer_action = get_computer_action()
    message, user_won = determine_outcome(user_action, computer_action)

    print(message)

    return user_won


def play():
    """Plays a number of rounds of the game."""

    rounds_played = 0
    rounds_won = 0

    finished = False

    while not finished:
        user_won = play_round()

        rounds_played += 1

        if user_won:
            rounds_won += 1

        print(f"You have won {rounds_won} out of {rounds_played} round(s).")

        finished = determine_whether_quit()


def main():
    """Launches the game."""

    play()


if __name__ == "__main__":
    main()
