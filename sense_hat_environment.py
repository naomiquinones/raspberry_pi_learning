from sense_hat import SenseHat
import time
from datetime import datetime
import pytz

sh = SenseHat()
sh.clear()

pressure = sh.get_pressure()
print(pressure)

temp = sh.get_temperature()
print(temp)

humidity = sh.get_humidity()
print(humidity)

DURATION = 1.5 * 60
INTERVAL = 5
total_readings = int(DURATION / INTERVAL)

pst = pytz.timezone('America/Los_Angeles')

readings_dict = {}

print(f"Starting {total_readings} temp readings over {DURATION} seconds")

for i in range(total_readings):
    current_utc = datetime.utcnow()
    current_pst = pytz.utc.localize(current_utc).astimezone(pst)
    current_time = current_pst.strftime("%Y-%m-%d %H:%M:%S PST")
    temp = sh.get_temperature()
    readings_dict[current_time] = temp
    print(f"Adding {current_time}: {temp} C")
    time.sleep(5)

print("Finished reading temp")
sh.clear()

print("----\nOutput dictionary data")
for time, temp in readings_dict.items():
    print(f"{time}: {temp}")
