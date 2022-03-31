#!/bin/bash
# pylint: disable=no-value-for-parameter,unexpected-keyword-arg

"""Converts between metric and imperial measures.

This script can convert between:
- miles and km
- lbs and kg
- degF and degC

Usage:
  metric_imperial_commands.py distance 10
  metric_imperial_commands.py -i weight 1
"""

import click

CONTEXT_SETTINGS = {"help_option_names": ["-h", "--help"]}


@click.group(context_settings=CONTEXT_SETTINGS, chain=True)
@click.version_option(version="1.0.0")
@click.pass_context
@click.option(
    "--imperial",
    "-i",
    is_flag=True,
    help="Convert from metric to imperial",
    show_default=True,
)
def main(ctx, imperial):
    """Performs the main task of the script."""

    ctx.obj["imperial"] = imperial


@main.command(help="Convert distance")
@click.pass_context
@click.argument("value", type=float)
def distance(ctx, value):
    """Converts between distance units.

    Args:
      value (float): miles or km.
    """

    if not ctx.obj["imperial"]:
        print(f"{value} miles is {value * 1.609344:.2f} km")
    else:
        print(f"{value} km is {value / 1.609344:.2f} miles")


@main.command(help="Convert weight")
@click.pass_context
@click.argument("value", type=float)
def weight(ctx, value):
    """Converts between weight units.

    Args:
      value (float): lbs or kg.
    """

    if not ctx.obj["imperial"]:
        print(f"{value} lbs is {value * 0.4535924:.2f} kg")
    else:
        print(f"{value} kg is {value / 0.4535924:.2f} lbs")


@main.command(help="Convert temperature")
@click.pass_context
@click.argument("value", type=float)
def temperature(ctx, value):
    """Converts between temperature units.

    Args:
      value (float): degF or degC.
    """

    if not ctx.obj["imperial"]:
        print(f"{value} degF is {(value - 32) * 5 / 9:.2f} degC")
    else:
        print(f"{value} degC is {value * 9 / 5 + 32:.2f} degF")


if __name__ == "__main__":
    main(obj={})
