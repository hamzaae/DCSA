import requests

url = 'http://127.0.0.1:5000/dcsa_api'
text = 'slam hani mzyan'  # Replace with the actual text you want to send

payload = {'text': text}
response = requests.post(url, data=payload)

print(response.json())