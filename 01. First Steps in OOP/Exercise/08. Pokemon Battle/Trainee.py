from pokemon import Pokemon


class Trainer:
    pokemons = []

    def __init__(self, name):
        self.name = name

    def add_pokemon(self, pokemon):
        if pokemon not in self.pokemons:
            self.pokemons.append(pokemon)
            return f"Caught {pokemon.name} with health {pokemon.health}"
        return "This pokemon is already caught"

    def release_pokemon(self, pokemon_name):
        for po in self.pokemons:
            if pokemon_name == po.name:
                self.pokemons.remove(po)
                return f"You have released {pokemon_name}"
        return "Pokemon is not caught"

    def trainer_data(self):
        res1 = f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemons)}\n"
        res2 = [f"- {po.pokemon_details()}" for po in self.pokemons]
        return res1 + "\n".join(res2)
