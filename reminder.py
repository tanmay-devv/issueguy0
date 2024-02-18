import os
import time

def run_program():
    os.system('/home/tanmay/Documents/isuueguy/dsfjk.py')
def schedule(hour, minute):
    while True:
        current_time=time.localtime()
        if current_time.tm_hour == hour and current_time.tm_min == minute:
            run_program()
            time.sleep(24*60*60)
        else:
            time.sleep(60)

schedule(9, 0)
