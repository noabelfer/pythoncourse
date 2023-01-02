from datetime import datetime
import time

start = datetime.now()
print('start: ',start)
time.sleep(61)
print('end: ',datetime.now())
duration = datetime.now() - start
duration_minutes = int(duration.total_seconds())//60
print("duration_minutes ",duration_minutes,' time left : ',90-duration_minutes)
 










