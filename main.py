import json
import requests

api_key = '2liTlUsVmStB+RfCg9nxgA==irVQNDJOC7iURQPB'



with open ('animals_template.html', 'r') as template:
    animals_template = template.read()


def load_data(file_path):
  """ Loads data from api """
  animal_name = input("What is your animal? ")
  url = f'https://api.api-ninjas.com/v1/animals?name={animal_name}'
  res = requests.get(url, headers={'X-Api-Key': api_key})
  return res.json()


animals_data = load_data('animals_data.json')


def serialize_animal(animal_obj):
    output = ''
    name_animal = animal['name']
    diet_animal = animal['characteristics']['diet']
    location_animal = animal['locations'][0]
    try:
        type_animal = animal['characteristics']['type']
        has_type = True
    except KeyError:
        has_type = False

    if has_type:
        # append information to each string
        output += '<li class="cards__item">'
        output += (f"<div class = 'card__title'>{name_animal}</div>"
                   f"<p class = 'card__text'>"
                   f"<strong>Diet:</strong> {diet_animal}<br/>\n"
                   f"<strong>Location:</strong> {location_animal}<br/>\n"
                   f"<strong>Type:</strong> {type_animal}<br/>\n"
                   f"</p>")

        output += '</li>'
    else:
        output += '<li class="cards__item">'
        output += (f"<div class = 'card__title'>{name_animal}</div>"
                   f"<p class = 'card__text'>"
                   f"<strong>Diet:</strong> {diet_animal}<br/>\n"
                   f"<strong>Location:</strong> {location_animal}<br/>\n"
                   f"</p>")

        output += '</li>'
    return output


output = ''
for animal in animals_data:
    output += serialize_animal(animal)

animals_output = animals_template.replace("__REPLACE_ANIMALS_INFO__", output)

with open ('animals.html', 'w') as out:
    out.write(animals_output)