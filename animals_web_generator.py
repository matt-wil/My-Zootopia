import json

FILENAME = "animals_data.json"
HTML = "animals_template.html"
NEW_HTML = "animals.html"


def load_data(filename):
    """Loads a JSON file"""
    with open(filename, "r") as handle:
        return json.load(handle)


def sort_data(data):
    """
    Extracts Name, Location[0], Diet, and Type from JSON data and returns a simplified list.
    :param data: (list) Nested dictionaries
    :return: (list) of dictionaries
    """
    new_animal_list = []
    for animal in data:
        new_animal_list.append({
            "Name": animal["name"],
            "Scientific Name": animal["taxonomy"].get("scientific_name"),
            "Location": animal["locations"][0],
            "Diet": animal["characteristics"].get("diet"),
            "Type": animal["characteristics"].get("type"),
            "Distinctive Feature": animal["characteristics"].get("distinctive_feature"),
            "Lifespan": animal["characteristics"].get("lifespan")
        })
    return new_animal_list


def serialize_data(animal):
    """Serializes a single animal dictionary into an HTML list item"""
    output = '<li class="cards__item">\n'
    output += f'  <div class="card__title"> {animal["Name"]}</div>\n'
    output += '   <p class="card_text">\n'

    if animal.get("Scientific Name"):
        output += f'    <strong>Scientific Name:</strong> {animal["Scientific Name"]}<br/>\n'
    if animal.get("Location"):
        output += f'    <strong>Location:</strong> {animal["Location"]}<br/>\n'
    if animal.get("Type"):
        output += f'    <strong>Type:</strong> {animal["Type"]}<br/>\n'
    if animal.get("Diet"):
        output += f'    <strong>Diet:</strong> {animal["Diet"]}<br/>\n'
    if animal.get("Distinctive Feature"):
        output += f'    <strong>Distinctive Feature:</strong> {animal["Distinctive Feature"]}<br/>\n'
    if animal.get("Lifespan"):
        output += f'    <strong>Lifespan:</strong> {animal["Lifespan"]}<br/>\n'
    output += '  </p>\n'
    output += '</li>\n'
    return output


def format_the_data(animals_list):
    """Formats the list of animals into HTML string"""
    output = ""
    for animal in animals_list:
        output += serialize_data(animal)
    return output


def read_html_doc(html_file):
    with open(html_file, "r") as file:
        return file.read()


def write_html_doc(new_file, new_string):
    with open(new_file, "w") as file:
        file.write(new_string)
        print(f"{new_file} successfully created and content written.")


def main():
    new_animal_data = format_the_data(sort_data(load_data(FILENAME)))
    html_data = read_html_doc(HTML)
    new_html_data = html_data.replace("__REPLACE_ANIMALS_INFO__", new_animal_data)
    write_html_doc(NEW_HTML, new_html_data)


if __name__ == '__main__':
    main()
