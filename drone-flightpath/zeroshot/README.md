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
