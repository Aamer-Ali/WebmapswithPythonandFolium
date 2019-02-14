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
featureGroup = folium.FeatureGroup(name="My Map FGroup")

# Adding Child to FG in For Loop using ZIP function
for lat, lon, elev, name in zip(latitude, longitude, elevation, placeName):
    featureGroup.add_child(folium.CircleMarker(location=[lat, lon], radius=6, popup=str(elev) + " m", tooltip=name,
                                               fill_color=changeMarkerColor(elev),color='gray',fill_opacity=0.7))

# Adding Feature Group to Map and Saving
map.add_child(featureGroup)
map.save("myMAP1.html")
