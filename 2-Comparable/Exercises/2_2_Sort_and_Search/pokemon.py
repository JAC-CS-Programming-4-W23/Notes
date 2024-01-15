from __future__ import annotations
from typing import Protocol, Optional
from enum import Enum


class PokemonNotFoundError(Exception):
    """Raised if trying to put a pokemon card into your 'team' if you don't actually have that card"""


class PokemonTeamDeckOverflowError(Exception):
    """"Raised if there is an attempt to add more than six cards to your team deck"""


class PokemonType(Enum):
    FIRE = 1
    WATER = 2
    GRASS = 3


def main():
    """
        To Do:
            * Instantiate two Pokémon here with different names and levels.
            * Verify that your code works by doing simple comparisons
            * Run the first test in PokemonTest to verify that creation is working.
            * Run the second test in PokemonTest to verify that the comparisons are working.
    """


class Pokemon:
    """ Implement the Pokémon class using the Compare Protocol """

    def __init__(self, name: str, level: int, ptype: PokemonType = None):
        self.name: str = name
        self.level: int = level
        self.type: PokemonType = ptype

    def __lt__(self, other):
        if self.name == other.name:
            return self.level < other.level
        return self.name < other.name

    def __eq__(self, other):
        return self.name == other.name and self.level == other.level

    @staticmethod
    def binary_search(data: list[Pokemon], name: str, level: int) -> Optional[int]:
        low: int = 0
        high: int = len(data) - 1
        mid: int = (low + high) // 2  # // is integer division
        value = Pokemon(name, level)

        while low <= high:
            if data[mid] < value:  # value would be on the right side
                low = mid + 1
            elif value < data[mid]:  # value would be on the left side
                high = mid - 1
            elif data[mid] == value:  # have we found it?
                return mid  # return the index

            mid = (low + high) // 2  # recalculate the mid-point

        return None  # we've looked everywhere and we can't find it

    @staticmethod
    def add_to_team(collection: list[Pokemon], team: list[Pokemon],
                    name: str, level: int):
        # find card position
        index = Pokemon.binary_search(collection, name, level)
        if index is None:
            raise PokemonNotFoundError
        if len(team) > 5:
            raise PokemonTeamDeckOverflowError
        team.append(collection[index])


    def __repr__(self):
        return f"Pokemon({self.name}, {self.level}, {self.type})"

    def __str__(self):
        return repr(self)
