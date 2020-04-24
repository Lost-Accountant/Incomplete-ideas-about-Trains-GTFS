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
    :@type route: str
    :@param route: a string that identifies the route of the arrival train
    :@type direction: str
    :@param direction: a string that identifies the direction of the route mentioned above
    :@type arrival_time: str
    :@param arrival_time: a string that identifies the arrival time of the upcoming train.
    """
    def __init__(self, route = '', direction = '', arrival_time =''):
        """
        Create a schedule entry
        """
        self.route = route,
        self.direction = direction
        self.arrival_time = datetime.strptime(arrival_time, '%H:%M:%S')
        

    def __str__(self):
        pass
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


