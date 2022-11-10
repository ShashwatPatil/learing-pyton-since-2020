import datetime
import time
def time_now(random,num,delay):
    for a in range(num):
        d = datetime.datetime.now()
        time_now = d.microsecond
        random_num = time_now % random
        time.sleep(delay)
        print(random_num)
