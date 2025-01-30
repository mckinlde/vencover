# Environment Class (environment.py)

# Handles the setup of cities, including weather, buildings, and population density.

class Environment:
    def __init__(self, city_name, dimensions, building_density):
        self.city_name = city_name
        self.dimensions = dimensions
        self.building_density = building_density
