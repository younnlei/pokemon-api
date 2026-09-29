import requests


def get_pokemon(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"

    response = requests.get(url)

    print(f"Status Code: {response.status_code}")

    return response.json()