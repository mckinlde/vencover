from scipy.spatial import KDTree

class CollisionDetector:
    def detect_collisions(self, drones):
        # Extract positions of active drones
        positions = [drone.get_position() for drone in drones if drone.active]

        # Prevent crash if there are no active drones
        if len(positions) < 2:
            return []

        # Construct KDTree for efficient collision detection
        tree = KDTree(positions)
        collisions = []

        for i, drone in enumerate(drones):
            if not drone.active:
                continue
            
            neighbors = tree.query_ball_point(drone.get_position(), r=max(drone.size))
            for j in neighbors:
                if i != j and drones[j].active:
                    collisions.append((drone.name, drones[j].name))
                    drone.active = False
                    drones[j].active = False

        return collisions
