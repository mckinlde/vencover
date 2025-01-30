Below Problem Statement was used to generate a zeroshot chatGPT output, which passed the sniff test.

Consider /zeroshot as the top-level-directory of the drone simulation

chatGPT is very conversational here, and I'm already stacking prompts.

GPT: 'I'll review the code and suggest improvements or additions to align with your problem statement. Would you like me to prioritize any specific component?'

Me: 'start from README.md, then traverse the directory tree to see where files are, and finally read and edit files as needed to fulfill the problem statement as found in README.md'

GPT: ... 'I've updated drone.py to include movement logic. Now, drones move toward their destination, adjusting their position at each time step based on speed. If they reach their destination, they stop.

Next, I'll review collision.py to check how collisions are detected.'

Me: 'Go ahead'

GPT: ... 'Next, I'll review environment.py to ensure it properly handles city conditions and constraints.'

Me: 'Go ahead; in your last output you just added class CollisionDetector in drone.py, but I corrected that and implemented class CollisionDetector in /models/collision.py for you'

GPT: ... 'Next, I'll review file_io.py to ensure it properly loads drone and city data from CSV files. Let me proceed.'

Me: Go ahead;  in your last output you just added class Environment in drone.py, but I corrected that and implemented class Environment in /models/environment.py for you

GPT: ... 'Next, I'll review visualization.py to see if there's any existing visualization and enhance it as needed. Let me proceed.

Me: Go ahead;  in your last output you just added class FileIO in drone.py, but I corrected that and implemented class FileIO in /utils/file_io.py for you

GPT: ... Next, I'll review config.json to ensure it properly defines user-configurable simulation parameters. Let me proceed.

Me: Go ahead;  in your last output you just added class Visualization in drone.py, but I corrected that and implemented class Visualization in /utils/visualization.py for you

GPT: ... Now, I'll review flight_paths.csv to ensure it provides valid drone routes. Let me proceed.

Me: Go ahead, on your last output you generated snippets to update config.json, I've edited my copy to match for you.
-----

Problem statement:

Design and implement a simulation system for autonomous drones navigating the airspace above a city.  The system should simulate the movement of drones based on user-defined inputs and calculate the number of potential collisions during the simulation.

Inputs:
1. City Dimensions: Define the size of the airspace (e.g., 1000x1000x500 units).
2. Drone Configuration:
- number of drones.
- model-specific attributes such as speed, size (see section called "data).
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

Data (.csv file):
Model Name,Max Speed (m/s),Range (km),Dimensions (m),Payload Capacity (kg),Battery Life (hours),Another property,Another property,etc
Falcon-X,20,50,1.2x0.8x0.5,5,2.5,,,
SkySurfer,15,30,1.0x0.6x0.4,3,3,,,
HawkEye,25,70,1.5x1.0x0.6,8,2,,,
AeroScout,18,40,1.1x0.7x0.5,4,3.5,,,
CloudRider,22,60,1.3x0.9x0.6,6,2.8,,,
Deliverance,30,10,2.0x1.0x1.5,10,1,,,
feel free to add rows and columns!,,,,,,,,
,,,,,,,,
,,,,,,,,
,,,,,,,,
,,,,,,,,
City Name,Building Density (buildings/km²),Average Building Height (m),Population Density (people/km²),Takeoff/Landing Locations,Another property,Another property,etc,
Metroville,1200,50,10000,150,,,,
Skyline City,800,45,7500,120,,,,
Urban Heights,1500,60,12000,180,,,,
AeroTown,1000,55,9000,140,,,,
Cloudscape,950,40,8500,130,,,,
Windy Ridge,700,35,7000,110,,,,
Valley Haven,600,30,5000,100,,,,
Summit View,750,25,6000,95,,,,
Crystal Bay,500,20,4000,85,,,,
Golden Plains,400,15,3000,75,,,,
feel free to add rows and columns!,,,,,,,,