import requests

response = requests.get('http://example.com')
print(response)
print(response.text)