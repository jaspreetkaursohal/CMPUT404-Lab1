import requests

response = requests.get('https://raw.githubusercontent.com/jaspreetkaursohal/CMPUT404-Lab1/main/version.py')
print(response._content)