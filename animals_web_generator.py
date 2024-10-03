import json
import os

FILENAME = "animals_data.json"
HTML = "animals_template.html"
NEW_HTML = "animals.html"


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


def format_the_data(animals_list):
    """
    Sorts through the list of dicts and placing them all into a string for the HTML file writing.
    The Function will skip any Key: Value where the Value == None
    :param animals_list: (list) Nested
    :return: (string)
    """
    stringed_animals = ""
    for animal in animals_list:
        stringed_animals += '<li class="cards__item">\n'
        stringed_animals += f'  <div class="card__title"> {animal["Name"]}<div/>\n'
        stringed_animals += '   <p class="card_text">\n'
        stringed_animals += f'    <strong>Location</strong> {animal["Location"]}<br/>\n'
        if animal.get("Type"):
            stringed_animals += f'    <strong>Type</strong> {animal["Type"]}<br/>\n'
        stringed_animals += f'    <strong>Diet</strong> {animal["Diet"]}<br/>\n'
        stringed_animals += '  </p>\n'
        stringed_animals += '</li>\n'
    return stringed_animals


def read_html_doc(html_file):
    with open(html_file, "r") as file:
        return file.read()


def write_html_doc(new_file, new_string):
    with open(new_file, "w") as file:
        file.write(new_string)
        print(f"{new_file} successfully created and content written.")


"""def write_html_doc(new_file, new_string):
    if os.path.exists(new_file):
        print(f"{new_file} already exists")
        return False
    else:
        with open(new_file, "w") as file:
            file.write(new_string)
            print(f"{new_file} successfully created and content written.")
        return True"""


def main():
    new_animal_data = format_the_data(sort_data(load_data(FILENAME)))
    html_data = read_html_doc(HTML)
    new_html_data = html_data.replace("__REPLACE_ANIMALS_INFO__", new_animal_data)
    write_html_doc(NEW_HTML, new_html_data)


if __name__ == '__main__':
    main()
