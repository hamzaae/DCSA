import urllib.request
import json
import os
import ssl
from dotenv import load_dotenv

def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

def predict_api(text):
    allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.

    # Request data goes here
    data = {
    "inputs": {
        "text": [text]
    }
    }


    body = str.encode(json.dumps(data))

    url = 'https://dcsa-llm-api.francecentral.inference.ml.azure.com/score'

    # Replace this with the primary/secondary key or AMLToken for the endpoint
    load_dotenv()
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise Exception("A key should be provided to invoke the endpoint")

    # The azureml-model-deployment header will force the request to go to a specific deployment.
    # Remove this header to have the request observe the endpoint traffic rules
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key), 'azureml-model-deployment': 'dcsa-llm-api' }

    req = urllib.request.Request(url, body, headers)

    try:
        response = urllib.request.urlopen(req)

        result = response.read()
        # Decode the bytes object to a string
        response_str = result.decode('utf-8')

        # Parse the JSON string into a dictionary
        response_dict = json.loads(response_str)

        # Extract the label and score
        label = response_dict.get('label')
        score = response_dict.get('score')

        # Return the extracted values
        return label, score
    except urllib.error.HTTPError as error:
        print("The request failed with status code: " + str(error.code))

        # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        print(error.info())
        print(error.read().decode("utf8", 'ignore'))


# print(predict_api("مبروك عليك رجوع الأغنية"))
