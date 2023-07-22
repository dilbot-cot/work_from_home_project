class TimeCalculator:
    @staticmethod
    def calculate_hours(start_time, end_time):
        start_hour, start_minute = map(int, start_time.split(':'))
        end_hour, end_minute = map(int, end_time.split(':'))
        return end_hour - start_hour + (end_minute - start_minute) / 60.0