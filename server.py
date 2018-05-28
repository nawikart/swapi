import json, requests
from pprint import pprint

apiUrl = 'https://swapi.co/api'

def get_id(url):
    return url.split('/')[-2]
    
def get_response(url):
    response = requests.get(url)
    return json.loads(response.text)

def get_count_of_all(key):
    people = get_response('{}/{}'.format(apiUrl, key))
    return people['count']
    
def get_person(person_id):
    return get_response('{}/people/{}'.format(apiUrl, person_id))

def get_homeworld(homeworld_id):
    return get_response('{}/planets/{}'.format(apiUrl, homeworld_id))

def get_starship(starship_id):
    return get_response('{}/starships/{}'.format(apiUrl, starship_id))

def get_vehicle(vehicle_id):
    return get_response('{}/vehicles/{}'.format(apiUrl, vehicle_id))

def all_person():

    no = 1
    for p in range(1, get_count_of_all('people')+1):

        try:
            person = get_person(p)
            pprint(no)
            pprint(person['name'])
            pprint(person['birth_year'])
            pprint(person['gender'])

            # pprint('________')

            homeworld_id = get_id(person['homeworld'])
            homeworld = get_homeworld(homeworld_id)
            pprint('H - {}'.format(homeworld['name']))
            pprint('  - {}'.format(homeworld['climate']))
            pprint('  - {}'.format(homeworld['terrain']))

            # pprint('________')

            if(len(person['starships']) > 0):
                for s in person['starships']:
                    starship = get_starship(get_id(s))
                    pprint('S - {}'.format(starship['name']))
                    pprint('  - {}'.format(starship['model']))
                    pprint('  - {}'.format(starship['manufacturer']))

            if(len(person['vehicles']) > 0):
                for v in person['vehicles']:
                    vehicle = get_vehicle(get_id(v))
                    pprint('V - {}'.format(vehicle['name']))
                    pprint('  - {}'.format(vehicle['model']))
                    pprint('  - {}'.format(vehicle['manufacturer']))
                # pprint('________')

            pprint('=============================================')

    
        except:
            pprint('=====error on person_id: {}'.format(p))

        no = no + 1


all_person()

# pprint(get_count_of_all('people'))