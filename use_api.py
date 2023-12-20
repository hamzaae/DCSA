import requests

url = 'https://lfahim.tech/dcsa_api'
text = 'Hello from DCSA'  # Replace with the actual text you want to send

payload = {'text': text}
response = requests.post(url, data=payload)

print(response.json())
