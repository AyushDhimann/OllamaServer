import requests, json

url = "http://0.0.0.0:11434/api/generate"
model = "mistral"
prompt = input("Enter your prompt: ")

data = {
    "model": model,
    "prompt": prompt
}

response = requests.post(url, json=data)

if response.status_code == 200:
    responses = [json.loads(line)["response"] for line in response.text.split('\n') if line.strip()]
    concatenated_response = ''.join(responses)

    print("Your Response:")
    print(concatenated_response)
else:
    print("Request failed with status code:", response.status_code)
