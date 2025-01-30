# Simulation Logic
# Implement the core simulation in main.py.

import math
from scipy.spatial import KDTree
import pandas as pd
import csv
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time
import json
from models.environment import Environment
from models.drone import Drone
from models.collision import CollisionDetector
from utils.file_io import FileIO
from utils.visualization import Visualization


def run_simulation(config_path):
    # Load configuration
    with open(config_path, 'r') as file:
        config = json.load(file)

    # Load city environment
    environment = Environment(config["city_name"], None, None, None, None, None)
    environment.load_city_data("data/cities.csv")

    # Load drones
    drone_models = FileIO.load_csv("data/drones.csv")
    flight_paths = FileIO.load_csv("data/flight_paths.csv")
    
    drones = []
    for i, path in enumerate(flight_paths[:config["num_drones"]]):
        model = drone_models[i % len(drone_models)]  # Assign model in a round-robin fashion
        size = list(map(float, model["Dimensions (m)"].split('x')))
        start_pos = [int(path["Start X"]), int(path["Start Y"]), int(path["Start Z"])]
        end_pos = [int(path["End X"]), int(path["End Y"]), int(path["End Z"])]
        drones.append(Drone(model["Model Name"], float(model["Max Speed (m/s)"]), start_pos, size, end_pos))
    
    # Initialize collision detector
    collision_detector = CollisionDetector()
    
    # Run simulation loop
    logs = []
    for step in range(0, config["simulation_time"], config["time_step"]):
        for drone in drones:
            drone.move(config["time_step"])
        
        collisions = collision_detector.detect_collisions(drones)
        if collisions:
            for collision in collisions:
                logs.append({"time": step, "collision": collision})
        
        time.sleep(config["time_step"])  # Simulate real-time execution
    
    # Save results
    FileIO.write_report(config["output_report"], logs)
    
    # Visualize results
    Visualization.plot_drones(drones, [log["collision"] for log in logs])
    

if __name__ == "__main__":
    run_simulation("config.json")
