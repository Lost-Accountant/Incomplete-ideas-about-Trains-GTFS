from datetime import datetime
from graphics import *
import json
import pandas


class ScheduleEntry:
    """
    === ScheduleEntry ===
    Context: a entry for a train's arrival on the schedule

    A ScheduleEntry must keep track of:
        Route_name --- route identifier for the arrival
        Direction --- an identifier for the direction of the route
        Arrival_time --- The (planned) arrival time for the upcoming train

    A ScheduleEntry must also be able to compare against one another based on the arrival time, letting trains arriving first be ranked first. It also needs to display useful information on the schedule board.

    === Attributes ===
    @type route: str
    @param route: a string that identifies the route of the arrival train
    @type direction: str
    @param direction: a string that identifies the direction of the route mentioned above
    @type arrival_time: str
    @param arrival_time: a string object that identifies the arrival time of the upcoming train.
    """
    def __init__(self, route = '', direction = '', arrival_time =''):
        """
        Create a schedule entry
        """
        # maybe should have done a getter and setter
        self.route = route
        self.direction = direction
        if arrival_time[:2] == '24':
            self.arrival_time = datetime.strptime('00' + arrival_time[2:], '%H:%M:%S')
        else:
            self.arrival_time = datetime.strptime(arrival_time, '%H:%M:%S')

        # load train information
        file = open('train_info.json', encoding="utf8")
        train_info = json.load(file)
        if self.route in train_info:
            self.numberofcars = train_info[route]["numebr of cars"]
            self.servicetype = train_info[route]["service type"]
            self._operator = train_info[route]["operator"]
            self.code = train_info[route]["code"]
            self.platform = train_info[route]["platform"]
        else:
            self.numberofcars = '8'
            self.servicetype = ''
            self._operator = ''
            self.code = ''
            self.platform = ''


        # find a way to solve direction and platform number lookup


    def __str__(self):
        """
        Produce a user-friendly string representation of ScheduleEntry self.

        @return: string representation of ScheduleEntry self.
        @rtype: str

        >>> a = ScheduleEntry('山手線','外回り・品川', '00:04:00')
        >>> print(a)
        ROUTE    TIME    DIRECTION
        山手線    00:04    外回り・品川
        """
        return 'ROUTE    TIME    DIRECTION\n' \
               '{}    {}    {}'.format(self.route,
                                   self.arrival_time.strftime("%H:%M"),
                                   self.direction)

    def __eq__(self, other):
        """
        Determine if a ScheduleEntry self is equivalent to ScheduleEntry other

        @type self: ScheduleEntry
        @param other: another ScheduleEntry
        @type other: ScheduleEntry
        @return: whether the route, direction, and time are the same as of the otehr ScheduleEntry
        @rtype: bool

        >>> a = ScheduleEntry('山手線','外回り・品川', '00:04:00')
        >>> b = ScheduleEntry('山手線','外回り・品川', '00:04:00')
        >>> a == b
        True
        >>> c = ScheduleEntry('山線','外回り・品川', '00:04:02')
        >>> a == c
        False
        """
        return (type(self) == type(other) and
                (self.route, self.direction, self.arrival_time) ==
                (other.route, other.direction, other.arrival_time))

    def __lt__(self, other):
        """
        Determine whether one ScheduleEntry train arrives earlier than other ScheduleEntry

        @type self: ScheduleEntry
        @param other: another ScheduleEntry
        @type other: ScheduleEntry
        @return: whether the time is earlier than other ScheduleEntry
        @rtype: bool
        >>> a = ScheduleEntry('山手線','外回り・品川', '00:04:00')
        >>> b = ScheduleEntry('山手線','外川', '00:07:36')
        >>> a < b
        True
        >>> a > b
        False
        """
        return (self.arrival_time < other.arrival_time)

    def __gt__(self, other):
        """
        Determine whether one ScheduleEntry train arrives later than other ScheduleEntry

        @type self: ScheduleEntry
        @param other: another ScheduleEntry
        @type other: ScheduleEntry
        @return: whether the time is later than other ScheduleEntry
        @rtype: bool
        >>> a = ScheduleEntry('山手線','外回り・品川', '00:04:00')
        >>> b = ScheduleEntry('山手線','外川', '00:07:36')
        >>> a > b
        False
        """
        return (self.arrival_time > other.arrival_time)

path = "E:\\Textbook\\4th Year\\CSC148\\tokyo trains\\"

class Timetable:
    """
    === Timetable ===
    Context: a collection of ScheduleEntry for displaying the arrival of trains on the display.

    A Timetable must be able to display all information of ScheduleEntry of an arrival train, and be able to jump to the closest train arrival when initiated. Currently the maximum number of trains is 5 at a time. The Timetable should also be able to detect the end of the scheduled service and display relevant message until the next train is near. Based on the day of the week, different ScheduleEntry is needed.

    First in First out system. (Queue)

    === Attributes ===
    @type ScheduleEntry: ScheduleEntry
    @param ScheduleEntry: a ScheduleEntry which contains all relevant information of a train arrival.
    @type _table: GraphWin object
    @param _table: a graphics window object as the background of display
    @type arrival: list
    @param arrival: a list to keep all the ScheduleEntry
    @type index: int
    @param index: an integer to keep track of current time/position
    """
    def __init__(self):
        """
        Initialize a blank black timetable display and an empty list.
        """
        self._table = GraphWin("Train Arrival Schedule", 1540, 900)
        self._table.setBackground("black")
        self.arrival = []
        self._table.getMouse()
        self._index = 0
        #self._table.close()

    #def checkversion(self):
        #"""
        #Check which version of schedule to use based on day of the week.
        #@return:
        #"""
        #pass

    def add_arrival(self, csv_file_name):
        """
        To add all arrivals from a given csv file at once.

        @type Schedule: str
        @param Schedule: a str that points to the csv file needed
        @rtype: None

        >>> path = "E:/Textbook/4th Year/CSC148/tokyo trains/"
        >>> weekday ='weekday schedule.csv'
        >>> train = Timetable()
        >>> train.add_arrival(path + weekday)
        """

        whole_schedule = pandas.read_csv(csv_file_name,
                                         encoding='utf8')
        for id in whole_schedule.index:
            self.arrival.append(ScheduleEntry(
                route=whole_schedule['route_long_name'][id],
                direction=whole_schedule['trip_headsign'][id],
                arrival_time=whole_schedule['arrival_time'][id]
            ))
        # will be triggered by first time execution and later every new day at 5am

    def remove_arrival(self):
        """
        Remove one by one based on time
        @return:
        """
        pass

    def JumpToNow(self):
        """
        Jump to closest arrival and delete all before
        @return:
        """
        pass

    def display(self):
        """
        Display the name of columns and the first 5 upcoming arrival
        @return:
        """
        pass

    def service_unavailable(self):
        """
        Check whether end of service (no arrival left) and display end of service until the next train is within 15 mins
        @return:
        """
        pass

    # reached end of the day?
    # check the end of day and display until the next one

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    # actual script of running the timetable
