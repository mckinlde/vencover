# Outputs
# Create detailed reports with:

# Number of collisions, flight success/failure rates.
# Drone travel efficiency metrics.
# Damage assessment based on collisions.


import csv


class FileIO:
    @staticmethod
    def load_csv(file_path):
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]

    @staticmethod
    def write_report(file_path, data):
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(data[0].keys())
            for row in data:
                writer.writerow(row.values())
