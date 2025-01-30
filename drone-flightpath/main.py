# Execute the simulation using the configured setup
config_path = "/drone-flightpath/zeroshot/config.json"

# Run the simulation
try:
    # Load configuration
    with open(config_path, 'r') as file:
        config = json.load(file)

    # Load city environment
    environment = Environment(config["city_name"], None, None, None, None, None)
    environment.load_city_data("/drone-flightpath/zeroshot/data/cities.csv")

    # Load drones
    drone_models = FileIO.load_csv("/drone-flightpath/zeroshot/data/drones.csv")
    flight_paths = FileIO.load_csv("/drone-flightpath/zeroshot/data/flight_paths.csv")

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

    # Save results
    report_path = f"/drone-flightpath/zeroshot/{config['output_report']}"
    FileIO.write_report(report_path, logs)

    # Display results
    logs_df = pd.DataFrame(logs)
    tools.display_dataframe_to_user(name="Simulation Report", dataframe=logs_df)

except Exception as e:
    str(e)
