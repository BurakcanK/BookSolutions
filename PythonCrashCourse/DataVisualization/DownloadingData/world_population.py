import json
import pygal
from pygal.maps.world import World
from pygal.style import LightColorizedStyle, RotateStyle

from country_codes import get_country_code

FILENAME = "population_data.json"

# load the data into a list
with open(FILENAME) as f:
    pop_data = json.load(f)

# build a dictionary of population data
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict["Year"] == "2010":
        country_name = pop_dict["Country Name"]
        population = int(float(pop_dict["Value"]))
        code = get_country_code(country_name)

        if code:
            cc_populations[code] = population

# group the countries into 3 population levels
cc_pops1, cc_pops2, cc_pops3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops1[cc] = pop
    elif pop < 1000000000:
        cc_pops2[cc] = pop
    else:
        cc_pops3[cc] = pop

wm_style = RotateStyle("#336699", base_style=LightColorizedStyle)
wm = World(style=wm_style)
wm.title = "World Population in 2010, by Country"
wm.add("0-10m", cc_pops1)
wm.add("10m-1bn", cc_pops2)
wm.add(">1bn", cc_pops3)

wm.render_to_file("world_population.svg")
