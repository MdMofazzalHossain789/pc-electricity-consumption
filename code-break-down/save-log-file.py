from datetime import datetime
import os

TOTAL_ENERGY = "15"
AVG_HOURLY = "5"

date = datetime.now().date()
filename = f"log-file-{date}.txt"
current_dir = os.getcwd()
output_dir = os.path.join(current_dir, filename)

with open(output_dir, 'w') as file:
    
    file.write(f"Date: {date}\n")
    file.write(f'Total Estimated Consumption: {TOTAL_ENERGY}\n')
    file.write(f"Average Hourly Consumption: {AVG_HOURLY}\n")
    
print(f"Saved log: {filename}")
    