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
print(time.strftime("%H:%M"))

print(df['arrival_time'][1] < df['arrival_time'][2])

# day of the week
# datetime to str
print(datetime.now().strftime("%a"))


# check date of the week
# 0 is monday and 6 is sunday
print(datetime.now().weekday())

# board
# pure text solution
# not correctly displaying japanese
import board

#
# Produce a 3x3 board
#
b1 = board.Board((3, 3))

b1 = board.Board((3, 3))
b1.populate("abcdef")
b1.dump()
b1.draw()

# graphics option
from graphics import *
#out = Image(Point(200,100), "out of service.png")
message = Text(Point(200, 200), "外回り・品川")
def main():
    win = GraphWin("My Circle", 800, 480)
    #c = Circle(Point(50,50), 10)
    #c.draw(win)
    #out.draw(win)
    message.setSize(36)
    message.draw(win)
    win.getMouse() # Pause to view result, otherwise the window will disappear
    win.close()
main()

quit = ''
while quit != 'q':
    quit = input("press q to quit")

