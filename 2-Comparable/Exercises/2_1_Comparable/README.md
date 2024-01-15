## 🎯 Objectives

- Practice making class objects that are comparable

## 🔨 Setup

Make sure you are using `python3.10` or later.

Create two new files, `pokemon.py` and `test_pokemon.py` and copy the code (shown below)
into the appropriate files.

If you have not yet set-up `pytest`, (`pytest` will be underlined by the IDE), install `pytest`.
(Click on the underlined `pytest`, and choose the option to install)

[How to use PyTest](https://www.jetbrains.com/help/pycharm/pytest.html#create-pytest-test)



## 🚦 Let's Go

1. Implement the `Pokemon` class to track the Pokemon's `name`, `type`, and `level`.
   - Use an [`enum`](https://docs.python.org/3.11/howto/enum.html#enum-basic-tutorial) for the `type`.
2. Implement the following `Comparable` Protocol (see below) for the `Pokemon` class.
3. For comparisons
   - The order priority is: 
     - first by `name` (alphabetical) 
     - and then by `level` (increasing).
   - Ex. A Bulbasaur is "less than" a Charmander because B comes before C alphabetically.
   - Ex. A level 1 Bulbasaur is "less than" a level 2 Bulbasaur because while their names are the same, their levels are not.
   - Ex. A level 1 Bulbasaur is "equal to" another level 1 Bulbasaur because both their names and levels are the same.


Starting code: (`pokeman.py`)
```python
from typing import Protocol
from enum import Enum


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


# Not really needed, but other functions can use this protocol to ensure
# what is being passed in is comparable
class Comparable(Protocol):
    def __lt__(self, other) -> bool: pass
    def __eq__(self, other) -> bool: pass


if __name__ == "__main__":
    main()
```

Test File:
```python
import pytest
from .pokemon import Pokemon, PokemonType


def test_pokemon_was_created_successfully():
    name = "Bulbasaur"
    level = 10
    ptype = PokemonType.GRASS
    pokemon: Pokemon = Pokemon(name, 10, ptype)
    assert name == pokemon.name
    assert level == pokemon.level
    assert ptype == pokemon.is_type


def test_pokemon_can_be_compared():
    pokemon1 = Pokemon("Bulbasaur", 10, PokemonType.GRASS)
    pokemon2 = Pokemon("Bulbasaur", 10, PokemonType.GRASS)
    pokemon3 = Pokemon("Bulbasaur", 11, PokemonType.GRASS)
    pokemon4 = Pokemon("Charmander", 9, PokemonType.FIRE)
    pokemon5 = Pokemon("Squirtle", 10, PokemonType.WATER);

    assert pokemon1 == pokemon2
    assert pokemon1 < pokemon3
    assert pokemon3 > pokemon2
    assert pokemon1 < pokemon4
    assert pokemon5 > pokemon4
```