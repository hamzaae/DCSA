import requests

url = 'http://localhost:5000/dcsa_api'
text = 'Hello'  # Replace with the actual text you want to send

payload = {'text': text}
response = requests.post(url, data=payload)

print(response.json())
