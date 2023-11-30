import datetime
import time

class Time:
    start_time = time.time()
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
