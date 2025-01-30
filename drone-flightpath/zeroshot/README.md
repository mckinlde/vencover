Problem statement:

Design and implement a simulation system for autonomous drones navigating the airspace above a city.  The system should simulate the movement of drones based on user-defined inputs and calculate the number of potential collisions during the simulation.

Inputs:
1. City Dimensions: Define the size of the airspace (e.g., 1000x1000x500 units).
2. Drone Configuration:
- number of drones.
- model-specific attributes such as speed, size (see "data/cities.csv" and "data/drones.csv").
3. Flight Paths:
- Each drone's starting position, destination, and waypoints.
- permissible takeoff and landing locations.
- optionally, include random or pre-defined flight paths.
4. Environmental conditions: weather, building structures, population density (as few or as many as you wish)
5. Simulation time: total duration for the simulation and the time step granulatiry (e.g., 1-second intervals).

Outputs:
1. A report showing:
- Anomalous situations: number of collisions, number of uncompleted flights, damages (drones, people, buildings, etc.).
- Statistics on drone efficiency (e.g., average travel time, successful completions).

Functional Requirements:
1. Drone Simulation:
- Each drone should move according to its speed and defined flight path.
- Include simple rules for drone behavior, such as slowing down or adjusting direction when near other drones.
2. Collision Detection:
- Detect and log collisions based on drone size and proximity.
- Consider 3D space for detection (x, y, z coordinates).
3. User Configuration:
- Allow users to define inputs via a configuration file or command-line arguments.
4. Simulation Logic:
- Run over discrete time steps and update frone positions accordingly.

Non-Functional Requirements:
1. Use any programming language you'd like.
2. Modular and extensible codebase for future enhancements (e.g., adding weather effects or dynamic path planning).
3. Handle edge cases, such as drones starting at the same position or moving along intersecting paths.

Evaluation Criteria:
1. Code Quality:
- Structure, readability, and modularity.
- Use of appropriate data structures and algorithms.
2. Collision detection logic:
- Accuracy and efficiency of detecting collisions in 3D space.
3. Simulation Realism:
- How well the simulation mimics real-world scenarios.
4. Visualization (Bonus):
- Quality and clarity of visual representation (if implemented).
5. Documentation:
- Brief but clear instructions on how to configure, run, and understand the simulation.

drone_simulation/
│
├── main.py           # Entry point for the simulation
├── config.json        # User-defined configuration inputs
├── models/            # Simulation logic and data models  
│   ├── drone.py       # Drone behavior and attributes  
│   ├── environment.py # City environment setup  
│   └── collision.py   # Collision detection logic  
│
├── data/              # Static data files  
│   ├── drones.csv     
│   ├── cities.csv     
│   └── flight_paths.csv  
│
├── utils/             # Helper functions  
│   ├── file_io.py     # Read/parse CSV and JSON  
│   └── visualization.py # Optional visualization  
│
└── README.md          # Documentation on usage
