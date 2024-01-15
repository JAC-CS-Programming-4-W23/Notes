import pytest
from pokemon import Pokemon, PokemonType, PokemonTeamDeckOverflowError, PokemonNotFoundError

@pytest.fixture
def pokemon_collection():
    return (
        Pokemon("Bulbasaur", 10, PokemonType.GRASS),
        Pokemon("Bulbasaur", 10, PokemonType.GRASS),
        Pokemon("Bulbasaur", 11, PokemonType.GRASS),
        Pokemon("Charmander", 9, PokemonType.FIRE),
        Pokemon("Squirtle", 10, PokemonType.WATER),
        Pokemon("Pikachu", 10, PokemonType.GRASS)
    )

def test_pokemon_was_created_successfully(pokemon_collection):
    name = "Bulbasaur"
    level = 10
    ptype = PokemonType.GRASS
    pokemon: Pokemon = Pokemon(name, 10, ptype)
    assert name == pokemon.name
    assert level == pokemon.level
    assert ptype == pokemon.type


def test_pokemon_can_be_compared(pokemon_collection):
    pokemon1, pokemon2, pokemon3, pokemon4, pokemon5, pokemon6 = pokemon_collection

    assert pokemon1 == pokemon2
    assert pokemon1 < pokemon3
    assert pokemon3 > pokemon2
    assert pokemon1 < pokemon4
    assert pokemon5 > pokemon4

def test_pokemon_binary_search(pokemon_collection):
    collection: list[Pokemon] = list(pokemon_collection)
    collection.sort()

    pos_bulbasaur_10 = Pokemon.binary_search(collection, "Bulbasaur", 10)
    assert pos_bulbasaur_10 == 0 or pos_bulbasaur_10 == 1
    assert Pokemon.binary_search(collection, collection[2].name, collection[2].level) == 2
    assert Pokemon.binary_search(collection, collection[3].name, collection[3].level) == 3
    assert Pokemon.binary_search(collection, collection[4].name, collection[4].level) == 4
    assert Pokemon.binary_search(collection, collection[5].name, collection[5].level) == 5

def test_pokemon_add_to_team__card_exists(pokemon_collection):
    team: list[Pokemon] = list()
    collection = list(pokemon_collection)
    collection.sort()

    for i in range(3):
        card = collection[i]
        Pokemon.add_to_team(collection, team,  card.name, card.level)

    for i in range(3):
        assert collection[i] in team
    assert len(team) == 3

def test_pokemon_add_to_team__card_does_not_exist(pokemon_collection):
    collection = list(pokemon_collection)
    collection.sort()
    team = list()

    # name doesn't exist
    with pytest.raises(PokemonNotFoundError):
        Pokemon.add_to_team(collection, team, "Foo", 10)

    # name/level combination doesn't exist
    with pytest.raises(PokemonNotFoundError):
        Pokemon.add_to_team(collection, team, "Bulbasaur", 9999)

def test_pokemon_add_to_team__too_many_cards_in_team_deck(pokemon_collection):
    team: list[Pokemon] = list()
    collection = list(pokemon_collection)
    collection.sort()

    for i in range(6):
        card = collection[i]
        Pokemon.add_to_team(collection, team,  card.name, card.level)

    assert len(team) == 6

    with pytest.raises(PokemonTeamDeckOverflowError):
        card = collection[1]
        Pokemon.add_to_team(collection, team,  card.name, card.level)
