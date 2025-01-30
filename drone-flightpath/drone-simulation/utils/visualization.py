# Visualization (Optional)
# Use libraries such as matplotlib for simple 3D visualization.

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

class Visualization:
    @staticmethod
    def plot_drones(drones, collisions):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        # Plot drones
        for drone in drones:
            if drone.active:
                pos = drone.get_position()
                ax.scatter(pos[0], pos[1], pos[2], label=drone.name)

        # Plot collisions
        for collision in collisions:
            if isinstance(collision, tuple) and len(collision) == 2:
                pos1, pos2 = collision
                if all(isinstance(coord, (int, float)) for coord in pos1) and \
                   all(isinstance(coord, (int, float)) for coord in pos2):
                    ax.scatter(pos1[0], pos1[1], pos1[2], color='red', marker='x', s=100)
                    ax.scatter(pos2[0], pos2[1], pos2[2], color='red', marker='x', s=100)
                else:
                    print(f"Warning: Skipping invalid collision data {collision}")
            else:
                print(f"Warning: Unexpected collision format {collision}")

        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.legend()
        plt.show()
