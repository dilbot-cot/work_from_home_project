import os
from csv_handler import CSVHandler
from date_handler import DateHandler
from input_handler import InputHandler
from time_calculator import TimeCalculator
from work_from_home_log import WorkFromHomeLog

# Create file path
desktop = os.path.join(os.path.join(os.environ['HOME']), 'Desktop')
log_file = os.path.join(desktop, "WFH_log.csv")

csv_handler = CSVHandler(log_file)
date_handler = DateHandler("01/07/2024", "30/06/2025")
input_handler = InputHandler()
time_calculator = TimeCalculator()

wfh_log = WorkFromHomeLog(csv_handler, date_handler, input_handler, time_calculator)
wfh_log.update_log()