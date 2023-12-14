import requests
url = "https://ide-wss-3g9g762.workspace.graderthan.com/?folder=/home/developer/Documents/code"
response = requests.get(url)
print(response.text)