# This seems to be an outdated method. Gives error.

from openai import OpenAI



# client = OpenAI(
#   organization='org-fRuq2NS5LxeF05ZB8ovUuJHU',
# )

import requests

# MAKE an API request
headers = {
    "Authorization": "Bearer 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", # Replace YOUR_API_KEY with your actual OpenAI API key
    "Content-Type": "application/json",
}

data = {
    "model": "gpt-3.5-turbo-0125",  # specify the model you want to use
    "prompt": "Translate the following English text to French: 'Hello, world!'",
    "temperature": 0.7, # between 0 and 1, while 1 is very creative and 0 is very preciese and repetitive. 0.7 is balanced.
    "max_tokens": 60, # for cost control, also: less length in the answer leads to more precision.
}

response = requests.post("https://api.openai.com/v1/chat/completions", json=data, headers=headers)


# HANDLE the response from the API request
if response.status_code == 200:
    # Request was successful
    print(response.json())
else:
    # There was an error
    print(f"Error: {response.status_code}")
    print(response.text)


