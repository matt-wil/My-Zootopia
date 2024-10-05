import json
import api_animals

FILENAME = "animals_data.json"
HTML = "animals_template.html"
NEW_HTML = "animals.html"


"""def load_data(filename):
    #Loads a JSON file#
    with open(filename, "r") as handle:
        return json.load(handle)"""


def sort_data(data, selected_skin_type=None):
    """
    Extracts necessary data from JSON and filters based on skin_type if provided.
    :param data: (list) Nested dictionaries
    :param selected_skin_type: (str) Filter based on this skin_type if provided (or None for all)
    :return: (list) of dictionaries
    """
    new_animal_list = []
    for animal in data:
        skin_type = animal["characteristics"].get("skin_type")
        if selected_skin_type != "All" and skin_type != selected_skin_type:
            continue  # skip animals that don't match selected type
        new_animal_list.append({
            "Name": animal["name"],
            "Scientific Name": animal["taxonomy"].get("scientific_name"),
            "Location": animal["locations"][0],
            "Diet": animal["characteristics"].get("diet"),
            "Type": animal["characteristics"].get("type"),
            "Distinctive Feature": animal["characteristics"].get("distinctive_feature"),
            "Lifespan": animal["characteristics"].get("lifespan"),
            "Skin Type": animal["characteristics"].get("skin_type")
        })
    return new_animal_list


def serialize_data(animal):
    """Serializes a single animal dictionary into an HTML list item"""
    output = '<li class="cards__item">\n'
    output += f'  <div class="card__title"> {animal["Name"]}</div>\n'
    output += '   <p class="card_text">\n'
    output += '      <ul class="inner_ul">\n'

    if animal.get("Scientific Name"):
        output += f'    <li class="inner__list__item"><strong>Scientific Name:</strong> {animal["Scientific Name"]}</li>\n'
    if animal.get("Location"):
        output += f'    <li class="inner__list__item"><strong>Location:</strong> {animal["Location"]}</li>\n'
    if animal.get("Type"):
        output += f'    <li class="inner__list__item"><strong>Type:</strong> {animal["Type"]}</li>\n'
    if animal.get("Diet"):
        output += f'    <li class="inner__list__item"><strong>Diet:</strong> {animal["Diet"]}</li>\n'
    if animal.get("Distinctive Feature"):
        output += f'    <li class="inner__list__item"><strong>Distinctive Feature:</strong> {animal["Distinctive Feature"]}</li>\n'
    if animal.get("Lifespan"):
        output += f'    <li class="inner__list__item"><strong>Lifespan:</strong> {animal["Lifespan"]}</li>\n'
    if animal.get("Skin Type"):
        output += f'    <li class="inner__list__item"><strong>Skin Type:</strong> {animal["Skin Type"]}</li>\n'
    output += '     </ul>\n'
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


def display_skin_types(data):
    """display a list of unique skin types plus 'All' as an option to print all animals."""
    skin_types = list(set(animal["characteristics"].get("skin_type") for animal in data))
    skin_types.append("All")
    return skin_types


def skin_type_input(skin_types_list):
    """print list of skin types and ask user to input a type or 'All' to display all"""
    print(f"Available skin types:", ", ".join(skin_types_list))
    while True:
        user_input = input("Enter one of the skin types or 'All' to display all animals\n>>> ").capitalize()
        if user_input in skin_types_list:
            return user_input
        else:
            print("Invalid input! Please try again.")


def main():
    complete_data = api_animals.api_animal_data_retrieval()

    # display skin types and search user input
    available_skin_types = display_skin_types(complete_data)
    selected_skin_type = skin_type_input(available_skin_types)

    # Sort data based on choice
    filtered_animal_data = format_the_data(sort_data(complete_data, selected_skin_type))

    # read and update html
    html_data = read_html_doc(HTML)
    new_html_data = html_data.replace("__REPLACE_ANIMALS_INFO__", filtered_animal_data)

    # write html file
    write_html_doc(NEW_HTML, new_html_data)


if __name__ == '__main__':
    main()
