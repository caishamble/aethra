from operator import itemgetter
def build_map(in_file1, in_file2, data_map):
    in_file1.readline()  # skip the header line
    in_file2.readline()  # skip the header line

    # READ EACH LINE FROM FILE 1
    for line in in_file1:
        # Split the line into two words (based on whitespace)
        continent_list = line.strip().split()

        # Convert to Title case, discard whitespace
        continent = continent_list[0].strip().title()
        country = continent_list[1].strip().title()

        # Ignore empty strings for continent and countries
        if continent and country:
            # If current continent not in map, insert it in the dictionary
            if continent not in data_map:
                data_map[continent] = {}

            # If country is not empty and country not in map, insert it in the dictionary
            # (continent is guaranteed to be in map)
            if country not in data_map[continent]:
                data_map[continent][country] = set()

    # READ EACH LINE FROM FILE 2
    for line in in_file2:
        # Split the line into two words (based on whitespace)
        countries_list = line.strip().split()

        # Convert to Title case, discard whitespace
        country = countries_list[0].strip().title()
        city = countries_list[1].strip().title()

        # Ignore empty strings for countries
        if country and city:
            # insert city (ignore country and city if country not in map)
            for continent in data_map:
                if country in data_map[continent]:
                    # if city is not in the list of cities for the country, add it to the list
                    if city not in data_map[continent][country]:
                        data_map[continent][country].add(city)

    # Close both files
    in_file1.close()
    in_file2.close()

def display_map(data_map):

    # Modify this code to display a sorted nested dictionary
    continents_list = sorted(data_map.keys())  # create a sorted list of the continent keys

    # For each continent
    for continent in continents_list:
        print(f"{continent}:")  # continent in continents_list
        countries_list = sorted(data_map[continent].keys())  # create a sorted list of the countries keys in the continents
        # For each country
        for country in countries_list:
            print(f"{country:>10s} --> ", end='')  # country in countries_list
            cities = sorted(data_map[continent][country])  # create a sorted list of the cities
            # join all cities in the list into a string separated by commas and spaces
            # hint: use join() function
            cities_str = ', '.join(cities)
            # print the created string of cities
            print(cities_str)

def open_file():
    try:
        filename = input("Enter file name: ")
        print()
        in_file = open(filename, "r")

    except IOError:
        print("\n*** unable to open file ***\n")
        in_file = None

    return in_file

def main():
    in_file1 = open_file()  # Continents with countries file: continents.txt
    in_file2 = open_file()  # Countries with cities file: cities.txt

    if in_file1 is not None and in_file2 is not None:
        data_map = {}  # empty dictionary
        build_map(in_file1, in_file2, data_map)  # data_map is a dictionary
        display_map(data_map)

if __name__ == "__main__":
    main()