import datetime
import time

class Time:
    start_time = time.time()

    @staticmethod
    def current_time():
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
