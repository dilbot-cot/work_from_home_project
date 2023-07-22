from csv_handler import CSVHandler
from date_handler import DateHandler
from input_handler import InputHandler
from time_calculator import TimeCalculator

class WorkFromHomeLog:
    def __init__(self, csv_handler, date_handler, input_handler, time_calculator):
        self.csv_handler = csv_handler
        self.date_handler = date_handler
        self.input_handler = input_handler
        self.time_calculator = time_calculator
        self.data = self.csv_handler.load_data()
        self.total_hours = self.calculate_previous_hours()

    def calculate_previous_hours(self):
        # Calculate the total hours from previous entries
        total_hours = 0
        for row in self.data[1:]:
            if row[1] == 'Y':
                total_hours += self.time_calculator.calculate_hours(row[2], row[3])
        return total_hours

    def update_log(self):
        # Iterate over all the dates
        for date in self.date_handler.date_range():
            if date.weekday() < 5:  # Exclude weekends
                # Check if this date is already in data
                if any(row[0] == date.strftime('%d/%m/%Y') for row in self.data):
                    continue
                wfh, start_time, end_time = self.input_handler.get_user_input(date)
                if wfh == 'exit':
                    break
                if wfh == 'y':
                    self.total_hours += self.time_calculator.calculate_hours(start_time, end_time)
                self.data.append([date.strftime('%d/%m/%Y'), wfh.upper(), start_time, end_time])
        self.save_data()

    def save_data(self):
        # Remove old total hours from data if exists
        self.data = [row for row in self.data if row[0] != 'Total WFH hours']
        # Append the new total hours to the end
        self.data.append(['Total WFH hours', round(self.total_hours, 2), '', ''])
        # Save the updated data back to the CSV
        self.csv_handler.save_data(self.data)
        print("No more data to input. Application now closing.")