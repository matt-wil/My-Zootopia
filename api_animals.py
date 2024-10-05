import requests


def api_animal_data_retrieval():
    animal = "Fox"
    api_url = 'https://api.api-ninjas.com/v1/animals?name={}'.format(animal)
    response = requests.get(api_url, headers={'X-Api-Key': '4+qFsSd2+FiI+V2iNh0mPg==2lkmSf7gmfeaB4ZJ'})
    if response.status_code == requests.codes.ok:
        return response.json()
    else:
        return "Error:", response.status_code, response.text


print(api_animal_data_retrieval())