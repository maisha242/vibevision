import requests
import json
import config

def openai_sound(item):
    print("SENDING OPENAI REQUEST FOR " + item)
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + config.openapi_key
    }

    payload = {
        "model": "gpt-4o-mini",
        "store": True,
        "messages": [
            {"role": "user", "content": "give me a sound (one word) that matches the following item: " + item}
        ]
    }

    # Send the POST request to OpenAI API
    response = requests.post(url, headers=headers, json=payload)

    # Check if the response is successful (status code 200)
    if response.status_code == 200:
        response_data = response.json()
        # Extract the assistant's response from the API result
        assistant_reply = response_data.get('choices', [{}])[0].get('message', {}).get('content', 'No response content')
        # print("Assistant's reply:", assistant_reply)
        return assistant_reply

    else:
        print(f"Request failed with status code {response.status_code}")
        print("Response:", response.text)


def openai_experimental(item):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + config.openapi_key
    }

    payload = {
        "model": "gpt-4o-mini",
        "store": True,
        "messages": [
            {"role": "user", "content": "Give me a text-to-music prompt describing its essence in music in less than 15 words for " + item}
        ]
    }

    # Send the POST request to OpenAI API
    response = requests.post(url, headers=headers, json=payload)

    # Check if the response is successful (status code 200)
    if response.status_code == 200:
        response_data = response.json()
        # Extract the assistant's response from the API result
        assistant_reply = response_data.get('choices', [{}])[0].get('message', {}).get('content', 'No response content')
        # print("Assistant's reply:", assistant_reply)
        return assistant_reply

    else:
        print(f"Request failed with status code {response.status_code}")
        print("Response:", response.text)

if __name__ == "__main__":
    openai_chat_completion("lilac")
