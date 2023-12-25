import requests

url = 'https://lfahim.tech/dcsa_api'
text = 'alo bikhir hamdulillah Cava'  # Replace with the actual text you want to send

payload = {'text': text}
response = requests.post(url, data=payload)

print(response.json())