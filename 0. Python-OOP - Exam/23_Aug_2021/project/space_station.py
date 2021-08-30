from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.number_of_successful_missions = 0
        self.number_of_not_completed_missions = 0

    def add_astronaut(self, astronaut_type: str, name: str):

        if self.astronaut_repository.find_by_name(name):
            return f"{name} is already added."
        if astronaut_type == "Biologist":
            self.astronaut_repository.astronauts.append(Biologist(name))
            return f"Successfully added {astronaut_type}: {name}."
        elif astronaut_type == "Geodesist":
            self.astronaut_repository.astronauts.append(Geodesist(name))
            return f"Successfully added {astronaut_type}: {name}."
        elif astronaut_type == "Meteorologist":
            self.astronaut_repository.astronauts.append(Meteorologist(name))
            return f"Successfully added {astronaut_type}: {name}."
        else:
            raise Exception("Astronaut type is not valid!")

    def add_planet(self, name: str, items: str):

        if self.planet_repository.find_by_name(name):
            return f"{name} is already added."

        planet = Planet(name)
        planet.items = items.split(", ")
        self.planet_repository.planets.append(planet)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        astronaut = self.astronaut_repository.find_by_name(name)
        if not astronaut:
            raise Exception(f"Astronaut {name} doesn't exists!")

        self.astronaut_repository.astronauts.remove(astronaut)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.increase_oxygen(10)

    def send_on_mission(self, planet_name: str):
        find_planet = [p for p in self.planet_repository.planets if p.name == planet_name]
        if not find_planet:
            raise Exception("Invalid planet name!")

        sorted_astronaut = []
        for astronaut in self.astronaut_repository.astronauts:
            if astronaut.oxygen > 30:
                sorted_astronaut.append(astronaut)

        if not sorted_astronaut:
            raise Exception("You need at least one astronaut to explore the planet!")
        choosing_astronaut = []
        for astronaut in sorted(sorted_astronaut, key=lambda x: -x.oxygen):
            if len(choosing_astronaut) < 5:
                choosing_astronaut.append(astronaut)
            else:
                break

        planet = find_planet[0]
        counter = 0

        for astronaut in choosing_astronaut:
            if planet.items:
                counter += 1
                for item in planet.items[::-1]:

                    astronaut.backpack.append(item)
                    planet.items.remove(item)
                    astronaut.breathe()
                    if astronaut.oxygen <= 0:
                        break
            else:
                self.number_of_successful_missions += 1
                return f"Planet: {planet_name} was explored. {counter} astronauts participated in collecting items."

        self.number_of_not_completed_missions += 1
        return "Mission is not completed."

    def report(self):
        result = [f"{self.number_of_successful_missions} successful missions!",
                  f"{self.number_of_not_completed_missions} missions were not completed!",
                  f"Astronauts' info:"]
        for astronaut in self.astronaut_repository.astronauts:
            result.extend([f"Name: {astronaut.name}",
                           f"Oxygen: {astronaut.oxygen}",
                           f"Backpack items: {', '.join(astronaut.backpack) if astronaut.backpack else 'none'}"])

        return '\n'.join(result)