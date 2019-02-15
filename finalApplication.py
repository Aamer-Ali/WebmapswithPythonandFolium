# Here we are going to create Geojson polygon layer
import pandas
import folium

# Reading File and Extracting Longitude and Latitude
mapsData = pandas.read_csv("Volcanoes_USA.txt")
latitude = list(mapsData['LAT'])
longitude = list(mapsData['LON'])
elevation = list(mapsData['ELEV'])  # Creating popup with ELEV column
placeName = list(mapsData['NAME'])  # Creating tooltip with NAME column


# Function For getting elevation and changing color of marker...
def changeMarkerColor(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    elif 3000 < elevation:
        return 'red'


# Creating Map and Feature Group
map = folium.Map(location=[38.55, -99.09], zoom_start=6, tiles="Mapbox Bright")
featureGroup_Volcanoes = folium.FeatureGroup(name="Volcanoes")

# Feature group for making markers on the bases of different data
# Adding Child to FG in For Loop using ZIP function
for lat, lon, elev, name in zip(latitude, longitude, elevation, placeName):
    featureGroup_Volcanoes.add_child(folium.CircleMarker(location=[lat, lon], radius=6, popup=str(elev) + " m", tooltip=name,
                                                         fill_color=changeMarkerColor(elev), color='gray', fill_opacity=0.7))

# Feature Group for making layer onthe bases of population
featureGroup_Population = folium.FeatureGroup(name="Population")
featureGroup_Population.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read()
                                      , style_function=lambda x: {
        'fillColor': 'green' if x['properties']['POP2005'] < 10000000
        else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

# Adding Feature Group to Map and Saving
map.add_child(featureGroup_Volcanoes)
map.add_child(featureGroup_Population)
map.add_child(folium.LayerControl())
# The above line of code going to give full control on the layers which we added to our map. We can setvisible or make our added layer invisible.
map.save("myMAP1.html")
