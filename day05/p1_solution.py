import sys
from itertools import groupby

file_name = sys.argv[1]

f = open(file_name, "r")
lines = f.read().splitlines()
f.close()

seeds = lines[0].split(": ")[1].split()
seeds = [int(seed) for seed in seeds]
lines = lines[1:]

groups = [list(g) for k, g in groupby(lines, key=bool) if k]

seed_to_soil_map = dict()
for line in groups[0][1:]:
    data = line.split()
    for offset in range(int(data[2])):
        seed_to_soil_map[int(data[1]) + offset] = int(data[0]) + offset

soil_to_fertilizer_map = dict()
for line in groups[1][1:]:
    data = line.split()
    for offset in range(int(data[2])):
        soil_to_fertilizer_map[int(data[1]) + offset] = int(data[0]) + offset

fertilizer_to_water_map = dict()
for line in groups[2][1:]:
    data = line.split()
    for offset in range(int(data[2])):
        fertilizer_to_water_map[int(data[1]) + offset] = int(data[0]) + offset

water_to_light_map = dict()
for line in groups[3][1:]:
    data = line.split()
    for offset in range(int(data[2])):
        water_to_light_map[int(data[1]) + offset] = int(data[0]) + offset

light_to_temperature_map = dict()
for line in groups[4][1:]:
    data = line.split()
    for offset in range(int(data[2])):
        light_to_temperature_map[int(data[1]) + offset] = int(data[0]) + offset

temperature_to_humidity_map = dict()
for line in groups[5][1:]:
    data = line.split()
    for offset in range(int(data[2])):
        temperature_to_humidity_map[int(data[1]) + offset] = int(data[0]) + offset

humidity_to_location_map = dict()
for line in groups[6][1:]:
    data = line.split()
    for offset in range(int(data[2])):
        humidity_to_location_map[int(data[1]) + offset] = int(data[0]) + offset

locations = []

for seed in seeds:
    soil = seed_to_soil_map.get(seed, seed)
    fertilizer = soil_to_fertilizer_map.get(soil, soil)
    water = fertilizer_to_water_map.get(fertilizer, fertilizer)
    light = water_to_light_map.get(water, water)
    temperature = light_to_temperature_map.get(light, light)
    humidity = temperature_to_humidity_map.get(temperature, temperature)
    location = humidity_to_location_map.get(humidity, humidity)
    locations.append(location)

print(min(locations))
