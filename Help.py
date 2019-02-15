import folium
import pandas

mapsData = pandas.read_csv("Volcanoes_USA.txt")
# print(mapsData.columns)


# name = list(mapsData['NAME'])
# for nm in name:
#     print(type(nm))

# print(help(folium.GeoJson))

l = lambda x : x+10
print(l(5))