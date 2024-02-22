import osmium as osm
import pandas as pd
import re
class OSMHandler(osm.SimpleHandler):
    def __init__(self):
        osm.SimpleHandler.__init__(self)
        self.osm_data = []
osmhandler = OSMHandler()
osmhandler.apply_file("15.osm")
# df = pd.read_xml("15.osm")
#  data_colnames = ['type', 'id', 'version', 'visible', 'ts', 'uid',
#                   'user', 'chgset', 'ntags', 'tagkey', 'tagvalue']
# df_osm = pd.DataFrame(osmhandler.osm_data, columns=data_colnames)
# df_osm = tag_genome.sort_values(by=['type', 'id', 'ts'])