import folium
map = folium.Map(location=[19.877,75.336],zoom_start=6,tiles="Mapbox Bright")
# map.add_child(folium.Marker(location=[19.877,75.336],popup="Auranagabad",tooltip="This is a a marker",icon=folium.Icon(color='green')))

# region Creating Feature Group
#Creating A FeatureGroup
featureGroup = folium.FeatureGroup(name="My Map FGroup")
# insted of Adding a child direct to Map we can add it To FeatureGroup SO we comment Line no 3.
# By Creating FG we can add multiple Child to our Map

# featureGroup.add_child(folium.Marker(location=[19.877,75.336],popup="Auranagabad",tooltip="This is a a marker",icon=folium.Icon(color='green')))
# featureGroup.add_child(folium.Marker(location=[18.877,74.336],popup="Auranagabad",tooltip="This is a a marker",icon=folium.Icon(color='green')))

# We can Add child in for loop as well

for coordinates in [[19.877,75.336],[18.877,74.336],[20.877,76.336]]:
    featureGroup.add_child(folium.Marker(location=coordinates,popup="Auranagabad",tooltip="This is a a marker",icon=folium.Icon(color='green')))
# endregion

# region Adding Feature Group to Map and Saving
map.add_child(featureGroup)
map.save("myMAP.html")
# endregion