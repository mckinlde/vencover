# Drone Class (drone.py)

import math

class Drone:
    def __init__(self, name, speed, position, size, destination):
        self.name = name
        self.speed = speed  # Speed in meters per second
        self.position = position  # [x, y, z]
        self.size = size  # [length, width, height]
        self.destination = destination
        self.active = True  # Indicates if flight is ongoing

    def move(self, time_step):
        if self.active:
            # Compute direction vector
            direction = [self.destination[i] - self.position[i] for i in range(3)]
            distance = math.sqrt(sum(d**2 for d in direction))

            if distance <= self.speed * time_step:
                # Reached destination
                self.position = self.destination
                self.active = False
            else:
                # Normalize direction and move drone
                unit_direction = [d / distance for d in direction]
                self.position = [self.position[i] + unit_direction[i] * self.speed * time_step for i in range(3)]

    def get_position(self):
        return self.position
