import json
import pygal

from pygal.maps.world import World
from pygal.style import LightColorizedStyle, RotateStyle

from countryCodes import getCountryCode

FILENAME = "population_data.json"

# load the data into a list
with open(FILENAME) as f:
    popData = json.load(f)

# build a dictionary of population data
ccPopulations = {}
for popDict in popData:
    if popDict['Year'] == '2010':
        countryName = popDict['Country Name']
        population = int(float(popDict['Value']))
        code = getCountryCode(countryName)

        if code:
            ccPopulations[code] = population

# group the countries into 3 population levels
ccPops1, ccPops2, ccPops3 = {}, {}, {}
for cc, pop in ccPopulations.items():
    if pop < 10000000:
        ccPops1[cc] = pop
    elif pop < 1000000000:
        ccPops2[cc] = pop
    else:
        ccPops3[cc] = pop

wmStyle = RotateStyle("#336699", base_style=LightColorizedStyle)
wm = World(style=wmStyle)
wm.title = "World Population in 2010, by Country"
wm.add("0-10m", ccPops1)
wm.add("10m-1bn", ccPops2)
wm.add(">1bn", ccPops3)

wm.render_to_file("worldPopulation.svg")
