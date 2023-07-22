import csv

class CSVHandler:
    def __init__(self, csv_file):
        self.csv_file = csv_file

    def load_data(self):
        # Load previous entries from the CSV
        try:
            with open(self.csv_file, 'r') as f:
                reader = csv.reader(f)
                return list(reader)
        except FileNotFoundError:
            # If the file doesn't exist, create one and add headers
            return [['Date', 'WFH?', 'Start time', 'End time']]

    def save_data(self, data):
        with open(self.csv_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(data)