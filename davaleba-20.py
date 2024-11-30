import requests
import json

def get_character_episodes():
    character_url = 'https://rickandmortyapi.com/api/character'
    character_data = {}

    while character_url:
        response = requests.get(character_url)
        response.raise_for_status()
        data = response.json()

        for character in data['results']:
            character_data[character['name']] = []
            for episode_url in character['episode']:
                episode_response = requests.get(episode_url)
                episode_response.raise_for_status()
                episode_data = episode_response.json()
                character_data[character['name']].append(episode_data['name'])

        character_url = data['info']['next']

    return character_data

def save_to_json(data, filename='character_episodes.json'):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

if __name__ == "__main__":
    character_episodes = get_character_episodes()
    save_to_json(character_episodes)
    print("Character episode data saved to character_episodes.json")