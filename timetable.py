from datetime import datetime

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
    @param arrival_time: a string that identifies the arrival time of the upcoming train.
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
        pass
    def __lt__(self, other):
        pass
    def __ne__(self, other):
        pass
    def __gt__(self, other):
        pass

class ScheduleTable:
    """
    First in First out system. (Queue)
    """
    pass
    # reached end of the day?
    # check weekend or weekday

if __name__ == "__main__":
    import doctest
    doctest.testmod()
