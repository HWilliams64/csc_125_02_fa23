import requests

data = {"number":1}
while True:
    response = requests.get('https://dogapi.dog/api/facts',data=data)

    print(response.json()['facts'][0])

    ui = input("Do you want to continue? (y/n) ")
    if ui == "n":
        break
