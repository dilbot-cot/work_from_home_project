import datetime

class DateHandler:
    def __init__(self, start_date_str, end_date_str):
        self.start_date = datetime.datetime.strptime(start_date_str, "%d/%m/%Y")
        self.end_date = min(datetime.datetime.now(), datetime.datetime.strptime(end_date_str, "%d/%m/%Y"))

    def date_range(self):
        delta = self.end_date - self.start_date
        for i in range(delta.days + 1):
            yield self.start_date + datetime.timedelta(days=i)