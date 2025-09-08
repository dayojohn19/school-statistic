import osmium
import csv

class PublicSchoolHandler(osmium.SimpleHandler):
    def __init__(self):
        super(PublicSchoolHandler, self).__init__()
        self.schools = []

    def node(self, n):
        if 'amenity' in n.tags and n.tags['amenity'] == 'school':
            # check if it's a public school
            operator_type = n.tags.get('operator:type', '').lower()
            operator = n.tags.get('operator', '').lower()

            if operator_type in ['public', 'government', 'state'] or \
               'deped' in operator or 'government' in operator or 'public' in operator:
                self.schools.append({
                    'id': n.id,
                    'name': n.tags.get('name', ''),
                    'operator': n.tags.get('operator', ''),
                    'lat': n.location.lat,
                    'lon': n.location.lon
                })

handler = PublicSchoolHandler()
handler.apply_file("philippines.osm.pbf")

print("Extracted", len(handler.schools), "public schools")

# Save to CSV
with open("public_schools.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["id", "name", "operator", "lat", "lon"])
    writer.writeheader()
    writer.writerows(handler.schools)

print("Saved to public_schools.csv")
