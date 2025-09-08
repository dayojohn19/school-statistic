import osmium
import csv

""" Extract schools from OSM data and save to CSV """

class SchoolHandler(osmium.SimpleHandler):
    def __init__(self):
        super(SchoolHandler, self).__init__()
        self.schools = []

    def node(self, n):
        if 'amenity' in n.tags and n.tags['amenity'] == 'school':
            self.schools.append({
                'id': n.id,
                'name': n.tags.get('name', ''),
                'lat': n.location.lat,
                'lon': n.location.lon
            })

handler = SchoolHandler()
handler.apply_file("philippines.osm.pbf")

print("Extracted", len(handler.schools), "schools")

# Save to CSV
with open("schools.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["id", "name", "lat", "lon"])
    writer.writeheader()
    writer.writerows(handler.schools)

print("Saved to schools.csv")
