import json

FILENAME = "animals_data.json"


def load_data(filename):
    """Loads a JSON file"""
    with open(filename, "r") as handle:
        return json.load(handle)


def sort_data(data):
    """
    Sorts through the JSON data extracting only the data we need Name, Location[0], Diet and Type.
    The Function takes a list of dictionaries and searches through the data for the specific keys needed.
    and places the data into a new list of animal dictionaries with only the needed data.
    :param data: (list) Nested with dictionaries and list
    :return: (list) of dictionaries
    """
    new_animal_list = []
    for animal in data:
        new_animal_dict = {}
        names = animal["name"]
        location = animal["locations"]
        diet = animal["characteristics"]["diet"]
        types = animal["characteristics"].get("type")
        new_animal_dict["Name"] = names
        new_animal_dict["Location"] = location[0]
        new_animal_dict["Diet"] = diet
        new_animal_dict["Type"] = types
        new_animal_list.append(new_animal_dict)
    return new_animal_list


def print_the_data(animals_list):
    """printing out the data from the sort_data() function in the correct format"""
    for animal in animals_list:
        for key, val in animal.items():
            if val is None:
                continue
            print(f"{key}: {val}")
        print()


def main():
    print_the_data(sort_data(load_data(FILENAME)))


if __name__ == '__main__':
    main()
