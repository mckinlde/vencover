# Visualization (Optional)
# Use libraries such as matplotlib for simple 3D visualization.

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

class Visualization:
    @staticmethod
    def plot_drones(drones, collisions):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        # Track if labels were added
        has_labels = False

        # Plot drones
        for drone in drones:
            if drone.active:
                pos = drone.get_position()
                ax.scatter(pos[0], pos[1], pos[2], label=drone.name)
                has_labels = True

        # Plot collisions
        for collision in collisions:
            if isinstance(collision, tuple) and len(collision) == 2:
                pos1, pos2 = collision
                if all(isinstance(coord, (int, float)) for coord in pos1) and \
                   all(isinstance(coord, (int, float)) for coord in pos2):
                    ax.scatter(pos1[0], pos1[1], pos1[2], color='red', marker='x', s=100)
                    ax.scatter(pos2[0], pos2[1], pos2[2], color='red', marker='x', s=100)

        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

        # Suppress the legend warning
        if has_labels:
            ax.legend()
        else:
            ax.legend().set_visible(False)  # Hide empty legend

        plt.show()
