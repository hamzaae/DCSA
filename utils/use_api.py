import requests
import os



def query(payload, API_URL, headers):
    response = requests.post(API_URL, headers=headers, json=payload).json()
    max_prediction = max(response[0], key=lambda x: x['score'])
    hg_label = 1 if max_prediction['label']=='negative' else 0
    hg_score = float(max_prediction['score'])
    return hg_label, hg_score
	
# output = query(payload, HG_URL, headers)
# print(output)