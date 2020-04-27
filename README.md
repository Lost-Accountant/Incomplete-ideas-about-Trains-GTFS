# Train Arrival Info Board
> Based on the GTFS file provided and a pre-specified station name, emulating a display with trains' arrival information commonly seen in Japan

Suggestion welcome for making this board more realistic

**Example Result**
[!["Real time" Arrival at Meguro Station](https://i.imgur.com/vrJh4Ok.png)]()

- GTFS data was from a contest held by Tokyo Department of Transportation or something like that, so it is only a simulated data from limited number of agencies (therefore no private firms and certain public lines), but it theoretically works with any GTFS data, preferrably from Japan.
- The program runs at your local time zone since I don't want it to be running at Japan's time zone and stare at a blank board on my daytime.
- Meguro station is chosen in the example just for personal preference.

**How it works**
- Required tool: R and Python
### Step 1
Open up "train_gtfs.rmd":
- Essential library: tidyverse, leaflet, and tidytransit
- If want to change station, change at line 32:
```shell
stop_ids <- tokyo_gtfs$stops %>%
  filter(stop_name == '<YOUR_PREFERRED_STATION>') %>%
  select(stop_id)
```
- Result would be 2 csv files, "weekday_schedule.csv" and "weekend_schedule.csv"
- R is used here since I found a convenient package for this job, tidytransit.

### Step 1.5
Edit information in "train_info.json" for:
- number of cars: the number of carriages in one train for a given train line.
- service type: local, express, limited express, rapid, airport express, or shinkansen type.
- code: the english code for the train line
- operator: the owner of the train line, currently not essential at all.
- platform: the platform number for the train line. Looking for suggestion on stations with multiple levels of platforms.

This step is just for the complete experience, otherwise only Direction, Destination, and Dep Time will be displayed.

### Step 2
Run "timetable.py"
- Essential library in the same repository: graphyics.py
- Other required library: pandas, json, and datetime
- Current output refreshes every minute and is designed for a 1080p screen. Resolution can be adjusted in the class Timetable
```shell
 def __init__(self):
        """
        Initialize a blank black timetable display and an empty list.
        """
        self.table = GraphWin("Train Arrival Schedule", <length>, <width>)
```
