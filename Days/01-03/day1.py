import sys
import time
from datetime import datetime
from datetime import timedelta

time_now = datetime.today()
start_time = int(input("Please enter a number for the countdown: "))
start_time_to_add = timedelta(seconds=start_time)
time_end = time_now + start_time_to_add
print("When the countdown ends, it will be {}".format(time_end.strftime('%H:%M:%S')))

for x in range(start_time):
    mins, secs = divmod(start_time, 60)
    sys.stdout.write('\r' + "{:02d}:{:02d}".format(mins, secs))
    sys.stdout.flush()
    time.sleep(1)
    start_time -= 1
    if start_time == 0:
        sys.stdout.write('\r' + "Done!")
