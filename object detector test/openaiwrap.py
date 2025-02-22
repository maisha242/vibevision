import requests
import json

def openai_sound(item):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer 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"
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
        #print("Assistant's reply:", assistant_reply)
        return assistant_reply

    else:
        print(f"Request failed with status code {response.status_code}")
        print("Response:", response.text)

if __name__ == "__main__":
    openai_chat_completion("lilac")
