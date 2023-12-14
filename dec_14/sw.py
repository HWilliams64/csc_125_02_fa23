import requests

for i in range(1, 5):
    r = requests.get('https://swapi.dev/api/starships/', params={'page': i})
    print(r.json())