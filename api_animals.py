import requests
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("ANIMALS_API_KEY")


def api_animal_data_retrieval():
    animal = input("Enter a animal name\n>>> ").strip()
    if not animal:
        return "Error: No animal name provided"

    api_url = 'https://api.api-ninjas.com/v1/animals?name={}'.format(animal)
    response = requests.get(api_url, headers={'X-Api-Key': api_key})
    if response.status_code == requests.codes.ok:
        return response.json()
    else:
        return "Error:", response.status_code, response.text
