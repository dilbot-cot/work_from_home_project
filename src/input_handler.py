import re

class InputHandler:
    @staticmethod
    def get_user_input(date):
        while True:
            wfh = input(f"Did you work from home on {date.strftime('%A %d/%m/%Y')}? (y/n/exit)").lower()
            if wfh in ['y', 'n', 'exit']:
                break
            else:
                print("This is an invalid input, please try again")
        if wfh == 'y':
            start_time = InputHandler.get_valid_time("Enter your start time (24hr format hh:mm): ")
            end_time = InputHandler.get_valid_time("Enter your end time (24hr format hh:mm): ")
        else:
            start_time, end_time = '00:00', '00:00'
        return wfh, start_time, end_time

    @staticmethod
    def get_valid_time(prompt):
        while True:
            time = input(prompt)
            if re.match(r'^([01]\d|2[0-3]):([0-5]\d)$', time):
                break
            else:
                print("Invalid time format. Please input time in the format hh:mm (24hr format).")
        return time