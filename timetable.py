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
    :@type route_name: str
    :@param route_name: a string that identifies the route of the arrival train
    :@type direction: str
    :@param direction: a string that identifies the direction of the route mentioned above
    :@type arrival_time: str
    """
    def __init__(self, ):
        """

        """
        pass

class ScheduleTable:
    """
    First in First out system.
    """
    pass


