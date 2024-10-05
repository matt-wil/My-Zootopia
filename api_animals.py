import requests
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("ANIMALS_API_KEY")


def api_animal_data_retrieval():
    animal = input("Enter a animal name\n>>> ").strip()
    if not animal:
        return "Error: No animal name provided"
    if not api_key:
        return "Error: API key not found"

    api_url = f'https://api.api-ninjas.com/v1/animals?name={animal}'
    headers = {'X-Api-Key': api_key}
    try:
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        return f"HTTP error: {e}"
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"
