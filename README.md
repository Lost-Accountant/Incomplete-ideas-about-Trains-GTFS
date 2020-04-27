# Train Arrival Info Board
> Based on the GTFS file provided and a pre-specified station name, emulating a display with trains' arrival information commonly seen in Japan

**Example Result**
[!["Real time" Arrival at Meguro Station](https://i.imgur.com/vrJh4Ok.png)]()

- GTFS data was from a contest held by Tokyo Department of Transportation or something like that, so it is only a simulated data, but it theoretically works with any GTFS data, preferrably from Japan.
- The program runs at your local time zone since I don't want it to be running at Japan's time zone and stare at a blank board on my daytime.
- Meguro station is chosen in the example just for personal preference.

**How it works**
- Required tool: R and Python
### Step 1
Open up "train_gtfs.rmd":
- Essential library: tidyverse, leaflet, and tidytransit
- If want to change station, change at line 32 "filter(stop_name == <your_preferred_station>)"
