# Visualization (Optional)
# Use libraries such as matplotlib for simple 3D visualization.

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

class Visualization:
    @staticmethod
    def plot_drones(drones, collisions):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        
        for drone in drones:
            positions = drone.get_position()
            ax.scatter(positions[0], positions[1], positions[2], label=drone.name)
        
        for collision in collisions:
            pos1, pos2 = collision
            ax.scatter(pos1[0], pos1[1], pos1[2], color='red', marker='x', s=100)
            ax.scatter(pos2[0], pos2[1], pos2[2], color='red', marker='x', s=100)
        
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.legend()
        plt.show()
