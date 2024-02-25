import xml.etree.ElementTree as ET
from collections import defaultdict

def count_fuel_stations(data):
    fuel_stations_by_company = defaultdict(int)
    fuel_stations = []
    flag = False
    for element in data.findall('.//way'):
        tags = element.findall('tag')
        for tag in tags:
            if tag.attrib.get('k') == 'amenity' and tag.attrib.get('v') == 'fuel':
                flag = True
            if tag.attrib.get('k') == 'operator' and flag:
                        name = tag.attrib.get('v')
                        fuel_stations_by_company[name] += 1   
                        fuel_stations.append(name)
                        flag = False

    return fuel_stations_by_company, sorted(set(fuel_stations))

def main():
    with open('C:\\Users\\DarkStell\\Documents\\GitHub\\Python24\\LP8\\file.txt', 'w',encoding='utf-8') as file:
        tree = ET.parse('C:\\Users\\DarkStell\\Documents\\GitHub\\Python24\\LP8\\16 - 2.osm')
        root = tree.getroot()
        fuel_stations_by_company, all_fuel_stations = count_fuel_stations(root)
        
        ##################
        for node in root.findall('.//node'):
            print("Node:", file=file)
            print("  ID:", node.attrib.get('id'), file=file)
            print("  Latitude:", node.attrib.get('lat'), file=file)
            print("  Longitude:", node.attrib.get('lon'), file=file)
            for tag in node.findall('tag'):
                print("  Tag:", file=file)
                print("    Key:", tag.attrib.get('k'), file=file)
                print("    Value:", tag.attrib.get('v'), file=file)

        for way in root.findall('.//way'):
            print("Way:", file=file)
            print("  ID:", way.attrib.get('id'), file=file)
            for tag in way.findall('tag'):
                print("  Tag:", file=file)
                print("    Key:", tag.attrib.get('k'), file=file)
                print("    Value:", tag.attrib.get('v'), file=file)
        ##################
        print("Количество заправок по каждой фирме:")
        for company, count in fuel_stations_by_company.items():
            print(f"{company}: {count}")
        
        print("\nОбщий список заправок в алфавитном порядке:")
        for station in all_fuel_stations:
            print(station)

if __name__ == "__main__":
    main()
