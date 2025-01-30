# Prompt 1:

Below Problem Statement was used to generate a zeroshot chatGPT output, which passed the sniff test.

Consider /zeroshot as the top-level-directory of the drone simulation

chatGPT is very conversational here, and I'm already stacking prompts.

GPT: 'I'll review the code and suggest improvements or additions to align with your problem statement. Would you like me to prioritize any specific component?'

# Prompt 2:
Me: 'start from README.md, then traverse the directory tree to see where files are, and finally read and edit files as needed to fulfill the problem statement as found in README.md'

GPT: ... 'I've updated drone.py to include movement logic. Now, drones move toward their destination, adjusting their position at each time step based on speed. If they reach their destination, they stop.

Next, I'll review collision.py to check how collisions are detected.'

# Prompt 3:
Me: 'Go ahead'

GPT: ... 'Next, I'll review environment.py to ensure it properly handles city conditions and constraints.'

# Prompt 4:
Me: 'Go ahead; in your last output you just added class CollisionDetector in drone.py, but I corrected that and implemented class CollisionDetector in /models/collision.py for you'

GPT: ... 'Next, I'll review file_io.py to ensure it properly loads drone and city data from CSV files. Let me proceed.'

# Prompt 5:
Me: Go ahead;  in your last output you just added class Environment in drone.py, but I corrected that and implemented class Environment in /models/environment.py for you

GPT: ... 'Next, I'll review visualization.py to see if there's any existing visualization and enhance it as needed. Let me proceed.

# Prompt 6:
Me: Go ahead;  in your last output you just added class FileIO in drone.py, but I corrected that and implemented class FileIO in /utils/file_io.py for you

GPT: ... Next, I'll review config.json to ensure it properly defines user-configurable simulation parameters. Let me proceed.

# Prompt 7:
Me: Go ahead;  in your last output you just added class Visualization in drone.py, but I corrected that and implemented class Visualization in /utils/visualization.py for you

GPT: ... Now, I'll review flight_paths.csv to ensure it provides valid drone routes. Let me proceed.

# Prompt 8:
Me: Go ahead, on your last output you generated snippets to update config.json, I've edited my copy to match for you.

GPT: ... Next, I'll review drones.csv to ensure the drone models and attributes are correctly defined. Let me proceed.

# Prompt 9:
Me: Go ahead

GPT: Would you like me to add more details, or is this dataset sufficient for now?

# Prompt 10:
Me: That's sufficient for now, let's prioritize getting to a first working version.

GPT: ... Would you like me to implement the simulation execution in main.py now?

# Prompt 11:
Me: Yes please

GPT: ... Would you like me to proceed with running a test simulation?

# Prompt 12:
Me: Yes please

GPT: The simulation has been executed successfully! The collision report is now available, showing:

Timestamps of when collisions occurred.
Drone pairs involved in each collision.
If you'd like, I can further analyze the results, optimize the simulation, or refine specific behaviors (e.g., collision avoidance, dynamic flight path adjustments). Let me know what you'd like to improve next! 🚀

# Prompt 13:
Me: Can you show me how to run it on my local copy?

GPT: ...

Terminal: (.venv) douglasmckinley@Douglass-MBP drone-simulation % python main.py
...
a series of import fixes
...
ValueError: data must be of shape (n, m), where there aren points of dimension m

# Prompt 14:
Me: 'When I run my local copy, I get this error output:

python main.py
Traceback (most recent call last):
  File "/Users/douglasmckinley/VSCodeProjects/vencover/drone-flightpath/drone-simulation/main.py", line 64, in <module>
    run_simulation("config.json")
  File "/Users/douglasmckinley/VSCodeProjects/vencover/drone-flightpath/drone-simulation/main.py", line 49, in run_simulation
    collisions = collision_detector.detect_collisions(drones)
  File "/Users/douglasmckinley/VSCodeProjects/vencover/drone-flightpath/drone-simulation/models/collision.py", line 10, in detect_collisions
    tree = KDTree(positions)
  File "/Users/douglasmckinley/VSCodeProjects/vencover/.venv/lib/python3.9/site-packages/scipy/spatial/_kdtree.py", line 360, in __init__
    super().__init__(data, leafsize, compact_nodes, copy_data,
  File "_ckdtree.pyx", line 560, in scipy.spatial._ckdtree.cKDTree.__init__
ValueError: data must be of shape (n, m), where there aren points of dimension m
(.venv) douglasmckinley@Douglass-MBP drone-simulation % 
'

GPT: ... <various bugfixes>

Me: The model takes a long time to run, without fixing it, why is it slow?

GPT: 
### **🔍 Why is the Simulation Slow?**
Several factors can contribute to the **slow execution** of your drone simulation:

---

### **1️⃣ Collision Detection Complexity**
- The current **collision detection** algorithm **checks each drone against every other drone**.
- If you have **N drones**, the complexity is **O(N²)** (quadratic time complexity), meaning that if the number of drones doubles, the number of collision checks **quadruples**.
- **KDTree** helps, but if drone positions are frequently updated, rebuilding the KDTree every step can be costly.

#### **🔧 Optimization**
- Instead of **rebuilding the KDTree every step**, update drone positions in the tree dynamically.
- Use a **spatial grid partitioning** to reduce unnecessary checks.

---

### **2️⃣ Time-Stepped Simulation Loops**
- Your simulation runs for **`simulation_time / time_step`** iterations.
- If `simulation_time = 300` seconds and `time_step = 1`, the loop runs **300 times**.
- If `time_step = 0.1` seconds, the loop runs **3000 times**, making it much slower.

#### **🔧 Optimization**
- Increase `time_step` (e.g., from `1` to `5` seconds) to **reduce the number of iterations**.
- Process **only moving drones** to avoid redundant calculations.

---

### **3️⃣ File I/O Operations**
- The simulation **reads multiple CSV files** (`drones.csv`, `flight_paths.csv`, `cities.csv`) before running.
- The **simulation report is written on every step**, which can slow things down.

#### **🔧 Optimization**
- **Load files once** into memory before the loop.
- **Buffer logs in memory** and write them **after the simulation ends** instead of writing every step.

---

### **4️⃣ Visualization Overhead**
- The `matplotlib` visualization may **slow execution if too many points are plotted**.
- If you have **100+ drones**, the plotting function might take a while.

#### **🔧 Optimization**
- **Skip visualization** while debugging (`config.json` setting).
- **Reduce the number of plotted waypoints** for faster rendering.

---

### **5️⃣ Sleep Function (`time.sleep`)**
- Your simulation **pauses execution** for `time_step` at each iteration.
- This **slows down the simulation unnecessarily**.

#### **🔧 Optimization**
- Remove `time.sleep()` **during testing** to run at full speed.
- Only enable `time.sleep()` if real-time pacing is needed.

---

### **🚀 Quick Fixes to Speed Up Execution**
1. **Increase time_step** in `config.json`:
   ```json
   {
       "time_step": 5
   }
   ```
2. **Disable time.sleep()** in `main.py`:
   ```python
   # time.sleep(config["time_step"])  # Comment this line out
   ```
3. **Write the report only once at the end** instead of each step.

Would you like me to implement these optimizations for you? 🚀
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