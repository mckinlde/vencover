# Environment Class (environment.py)

# Handles the setup of cities, including weather, buildings, and population density.

import pandas as pd


class Environment:
    def __init__(self, city_name, dimensions, building_density, weather, population_density, takeoff_locations):
        self.city_name = city_name
        self.dimensions = dimensions
        self.building_density = building_density
        self.weather = weather
        self.population_density = population_density
        self.takeoff_locations = takeoff_locations
        self.buildings = []

    def load_city_data(self, file_path):
        df = pd.read_csv(file_path)
        city_data = df[df['City Name'] == self.city_name].iloc[0]
        self.building_density = city_data['Building Density (buildings/km²)']
        self.population_density = city_data['Population Density (people/km²)']
        self.takeoff_locations = city_data['Takeoff/Landing Locations']

    def define_no_fly_zones(self):
        # Define areas where drones cannot fly based on buildings or regulations
        pass

