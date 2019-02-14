import folium
import pandas

mapsData = pandas.read_csv("Volcanoes_USA.txt")
print(mapsData.columns)


name = list(mapsData['NAME'])
for nm in name:
    print(type(nm))