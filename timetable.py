from datetime import datetime
import graphics

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
        self.route = route
        self.direction = direction
        self.arrival_time = datetime.strptime(arrival_time, '%H:%M:%S')
        # search up platform number
        # search up train type
        # search up car numbers


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


class Timetable:
    """
    === Timetable ===
    Context: a collection of ScheduleEntry for displaying the arrival of trains on the display.

    A Timetable must be able to display all information of ScheduleEntry of an arrival train, and be able to jump to the closest train arrival when initiated. Currently the maximum number of trains is 5 at a time. The Timetable should also be able to detect the end of the scheduled service and display relevant message until the next train is near. Based on the day of the week, different ScheduleEntry is needed.

    First in First out system. (Queue)

    === Attributes ===
    @type ScheduleEntry: ScheduleEntry
    @param ScheduleEntry: a ScheduleEntry which contains all relevant information of a train arrival.
    @type date: int
    @param date: an int that keeps track of the date of the week and requests the corresponding ScheduleEntry from data.
    """
    pass
    # reached end of the day?
    # check weekend or weekday
    # check the end of day and display until the next one

if __name__ == "__main__":
    import doctest
    doctest.testmod()
