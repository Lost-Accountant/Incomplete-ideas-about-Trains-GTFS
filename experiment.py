import pandas

path = "E:\\Textbook\\4th Year\\CSC148\\tokyo trains\\"

weekday = 'weekday schedule.csv'

df = pandas.read_csv(path + weekday, encoding = 'utf8')
print(df)
print(type(df['route_long_name'][1]))
