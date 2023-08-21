"""
import osmium

class RoadDataCollector(osmium.SimpleHandler):
    def __init__(self):
        super().__init__()
        self.roads = {}
        print("Bruh")

    def way(self, w):
        tags = w.tags

        if 'ref' in tags and tags['ref'] == 'E11':
            way_id = w.id
            lanes = tags.get('lanes', None)
            self.roads[way_id] = lanes

osm_file_path = 'C:\\Users\\AhmedA9\\Downloads\\Map.osm'
collector = RoadDataCollector()
collector.apply_file(osm_file_path)
#print(collector.roads.items())

for way_id, lanes in collector.roads.items():
    print(f"Way ID: {way_id}")
    print(f"  Lanes: {lanes}")

print('THE END BRUH')
"""

#Attempt 2
"""
import osmium

class WayDataCollector(osmium.SimpleHandler):
    def __init__(self):
        super().__init__()
        self.roads = {}
        print("Bruh")

    def way(self, w):
        tags = w.tags

        if 'ref' in tags and tags['ref'] == 'E11':
            way_id = w.id
            lanes = tags.get('lanes', None)
            refs = tags.get('Refs', None)  # New tag "Refs"
            self.roads[way_id] = {
                'lanes': lanes,
                'Refs': refs
            }

    def node(self, n):
        pass

    def area(self, a):
        pass

    def relation(self, r):
        pass

if __name__ == "__main__":
    osm_file_path = 'C:\\Users\\AhmedA9\\Downloads\\Map.osm'  # Replace with the actual path to your OSM file
    collector = WayDataCollector()
    collector.apply_file(osm_file_path)

    for way_id, road_info in collector.roads.items():
        print(f"Way ID: {way_id}")
        print(f"  Lanes: {road_info['lanes']}")
    print('The end bruh ;)')

"""


#Take 3
import osmium

class WayDataCollector(osmium.SimpleHandler):
    def __init__(self):
        osmium.SimpleHandler.__init__(self)
        self.roads = {}
        print("Bruh")

    def way(self, w):
        tags = w.tags
        
        if 'ref' in tags and tags['ref'] == 'E11':
            print('enter')
            way_id = w.id
            lanes = tags.get('lanes', None)
            refs = tags.get('Refs', None)  # New tag "Refs"
            self.roads[way_id] = {
                'lanes': lanes,
                'Refs': refs
            }
            print('exit')

osm_file_path = "map.osm"  # Replace with the actual path to your OSM file
collector = WayDataCollector()
collector.apply_file(osm_file_path)


print(collector.roads.items())

for way_id, road_info in collector.roads.items():
    print(f"Way ID: {way_id}")
    print(f"  Lanes: {road_info['lanes']}")
    #print(f"  Refs: {road_info['Refs']}")  # Print the new tag "Refs"

print('1')    