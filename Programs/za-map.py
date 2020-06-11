import folium
import pandas

map = folium.Map(location=[-29.1913828,24.4497398], zoom_start=6)
data_json = open("world.json", 'r', encoding='utf-8-sig').read()
data_json2 = open("za.json", 'r', encoding='utf-8-sig').read()# there must be a problem with my imorting or my data

fg = folium.FeatureGroup(name="Population")
markers = folium.FeatureGroup(name="ZA cities (markers)")

data = pandas.read_csv("za.csv",encoding="utf8")
lat = list(data["lat"])
lng = list(data["lng"])
city = list(data["city"])
value = list(data["population"])

for i in range(0,len(data)):
    folium.Marker([data.iloc[i]['lat'], data.iloc[i]['lng']], popup=data.iloc[i]['city']).add_to(markers)


fg.add_child(folium.GeoJson(data=data_json,
style_function=lambda x: {'fillColor':'green' if x['properties']
['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else
'red' }))

map.add_child(markers)
map.add_child(fg)

map.add_child(folium.LayerControl())

map.save("worldmap2020.html")
