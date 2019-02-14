# In this we are going to add markers from a text file which is in our working directorey named Volcanes_USA.txt
# got this file while doing practice online

import pandas  # To Read Data From text file in CSV Format
import folium

# Reding File and Extracting Longitude and Latitude
mapsData = pandas.read_csv("Volcanoes_USA.txt")
latitude = list(mapsData['LAT'])
longitude = list(mapsData['LON'])
elevation = list(mapsData['ELEV'])  # Creating popup with ELEV column
placeName = list(mapsData['NAME'])  # Creating tooltip with NAME column

# Creating Map and Feature Group
map = folium.Map(location=[19.877, 75.336], zoom_start=6, tiles="Mapbox Bright")
featureGroup = folium.FeatureGroup(name="My Map FGroup")

# Adding Child to FG in For Loop using ZIP function
for lat, lon, elev, name in zip(latitude, longitude, elevation, placeName):
    featureGroup.add_child(folium.Marker(location=[lat, lon], popup=str(elev), tooltip=name,
                                         icon=folium.Icon(color='green')))

# Adding Feature Group to Map and Saving
map.add_child(featureGroup)
map.save("myMAP1.html")
