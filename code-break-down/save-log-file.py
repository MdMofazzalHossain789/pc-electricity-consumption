from datetime import datetime
import os

TOTAL_ENERGY = "15"
AVG_HOURLY = "5"

date = datetime.now().date()
filename = f"log-file-{date}.txt"
script_loc = __file__
script_path = os.path.abspath(script_loc)
script_dir = os.path.dirname(script_path)
output_dir = os.path.join(script_dir, filename)

with open(output_dir, 'w') as file:
    
    file.write(f"Date: {date}\n")
    file.write(f'Total Estimated Consumption: {TOTAL_ENERGY}\n')
    file.write(f"Average Hourly Consumption: {AVG_HOURLY}\n")
    
print(f"Saved log: {filename}")
    