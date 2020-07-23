import folium
import pandas


def volcano_color(height):
    if height > 4000:
        return "red"
    elif height > 2000:
        return "orange"
    else:
        return "green"


map = folium.Map(location=[49.96, 14.08], zoom_start=6)
vol = pandas.read_csv("Volcanoes.txt")
lat = list(vol["LAT"])
lon = list(vol["LON"])
nam = list(vol["NAME"])
elv = list(vol["ELEV"])

fgv = folium.FeatureGroup(name="Volcanoes")

for lt, ln, nm, el in zip(lat, lon, nam, elv):
    fgv.add_child(folium.Marker(location=[lt, ln], icon=folium.Icon(color=volcano_color(el)), popup="Volcano: " + nm))

fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
                             style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000
                             else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))


map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("map.html")
