import pandas
from datetime import datetime

path = "E:\\Textbook\\4th Year\\CSC148\\tokyo trains\\"

weekday = 'weekday schedule.csv'

df = pandas.read_csv(path + weekday, encoding = 'utf8')
print(df)
print(type(df['arrival_time'][1]))

# str to datetime
time = datetime.strptime(df['arrival_time'][1], '%H:%M:%S')
print(time)
print(type(time))

print(df['arrival_time'][1] < df['arrival_time'][2])

# day of the week
# datetime to str
print(datetime.datetime.now().strftime("%a"))

# check date of the week
# 0 is monday and 6 is sunday
datetime.datetime.now().weekday()
