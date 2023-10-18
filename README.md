# Ollama Server 

[Ollama](https://www.ollama.ai/) offers the flexibility of running renowned large language models(LLM) both locally and through its API. However, the potential of a consumer PC has its limitations.

In this repository, we provide a streamlined solution for effortlessly installing Ollama on a Linux web server with a single command. This enables you to access a public IP address, facilitating quicker and smoother utilization of your large language models in various applications.


# Installation

To install the Ollama Server on your Linux machine, copy and paste this one-liner code and enter your preferred model to install 

```
git clone https://github.com/AyushDhimann/OllamaServer/ && cd OllamaServer && chmod +x install.sh && sudo ./install.sh
```

# Usage

1. Get your server IP Address and replace it accordingly in the next step.

2. Either use it with cURL

```
curl -X POST http://0.0.0.0:11434/api/generate -d '{
  "model": "mistral",
  "prompt":"Who was the president of United States in 1984?"
}'
```

OR

use the sample python code provided in the repo [here](https://github.com/AyushDhimann/OllamaServer/blob/main/client-sample.py).

# FAQ

### 1. How to stop the server?
A. Run this command ``` service ollama stop ```

### 2. How to start a stopped server?
A. Run this command ``` service ollama start ```

### 3. How to install any other model in Ollama?
A. Run this command ``` ollama pull "MODEL_NAME" ``` and then edit the model name in your request too.
