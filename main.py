from data_fetcher import fetch_data

with open ('animals_template.html', 'r') as template:
    animals_template = template.read()

def serialize_animal(animal):
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

def main():
    animal_name = input("What is your animal? ")
    animals_data = fetch_data(animal_name)
    animals_serialized = ''

    if animals_data != []:
        for animal in animals_data:
            animals_serialized += serialize_animal(animal)
            animals_output = animals_template.replace("__REPLACE_ANIMALS_INFO__", animals_serialized)
    else:
        animals_output = animals_template.replace("__REPLACE_ANIMALS_INFO__", f"<h2>The animal {animal_name} doesn't exist.</h2>")

    with open ('animals.html', 'w') as out:
        out.write(animals_output)


if __name__ == '__main__':
    main()
