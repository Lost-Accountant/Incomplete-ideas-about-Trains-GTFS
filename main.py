from timetable import Timetable
from datetime import datetime
import time

if __name__ == "__main__":
    # actual script of running the timetable
    path = "E:/Textbook/4th Year/CSC148/tokyo trains/"
    weekday ='weekday schedule.csv'
    weekend = 'weekend schedule.csv'
    train = Timetable()

    # determine which version to use
    if datetime.now().isoweekday() < 6:
        train.add_arrival(path + weekday)
    else:
        train.add_arrival(path + weekend)

    while True:
        train.JumpToNow()
        train.display()
        time.sleep(20)
        train.clear_table()
        train.service_unavailable()
