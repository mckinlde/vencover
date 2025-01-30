from scipy.spatial import KDTree

class CollisionDetector:
    def detect_collisions(self, drones):
        positions = [drone.get_position() for drone in drones if drone.active]

        if len(positions) < 2:
            return []

        tree = KDTree(positions)
        collisions = []

        for i, drone in enumerate(drones):
            if not drone.active:
                continue
            
            neighbors = tree.query_ball_point(drone.get_position(), r=max(drone.size))
            for j in neighbors:
                if i != j and drones[j].active:
                    # Ensure the collision log stores numeric positions
                    collisions.append((drone.get_position(), drones[j].get_position()))
                    drone.active = False
                    drones[j].active = False

        return collisions
