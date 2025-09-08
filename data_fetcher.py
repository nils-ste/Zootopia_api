import requests
api_key = '2liTlUsVmStB+RfCg9nxgA==irVQNDJOC7iURQPB'

def fetch_data(animal_name):
  """
  Fetches the animals data for the animal 'animal_name'.
  Returns: a list of animals, each animal is a dictionary:
  {
    'name': ...,
    'taxonomy': {
      ...
    },
    'locations': [
      ...
    ],
    'characteristics': {
      ...
    }
  },
  """
  url = f'https://api.api-ninjas.com/v1/animals?name={animal_name}'
  res = requests.get(url, headers={'X-Api-Key': api_key})
  return res.json()