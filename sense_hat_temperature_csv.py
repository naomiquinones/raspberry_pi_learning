from sense_hat import SenseHat
import time
from datetime import datetime
import pytz
import csv

sh = SenseHat()
sh.clear()

DURATION = 1.5 * 60
INTERVAL = 5
total_readings = int(DURATION / INTERVAL)

pst = pytz.timezone('America/Los_Angeles')

temp_readings_dict = {}

print(f"STARTING {total_readings} temp readings over {DURATION} seconds\n")

for i in range(total_readings):
    current_utc = datetime.utcnow()
    current_pst = pytz.utc.localize(current_utc).astimezone(pst)
    current_time = current_pst.strftime("%Y-%m-%d %H:%M:%S PST")
    temp = sh.get_temperature()
    temp_readings_dict[current_time] = temp
    print(f"Adding {current_time}: {temp} C")
    time.sleep(5)

print("\nFINISHED reading temp\n")
sh.clear()

print("-----\nOUTPUTTING DICTIONARY DATA\n")
for time, temp in temp_readings_dict.items():
    print(f"{time}: {temp}")

csv_filename = "temperatures.csv"
headers = ["Time", "Temperature"]

print("-----\nWRITING DATA TO CSV FILE\n")

with open(csv_filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(temp_readings_dict.items())
