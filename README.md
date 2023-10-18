# Ollama Server 

This repository automatically install Ollama for you on linux and set-up's a publicly accessible IP that can be used further for integration into various use-cases.

# Instructions

To install the Ollama Server on your Linux machine, copy and paste this code and enter your preferred model to install 

```
git clone https://github.com/AyushDhimann/OllamaServer/ && cd OllamaServer && chmod +x install.sh && sudo ./install.sh
```

# How to use

1. Get your server IP Address.

2. Either use it with cURL (replace 0.0.0.0 with your server IP Address)

```
curl -X POST http://0.0.0.0:11434/api/generate -d '{
  "model": "mistral",
  "prompt":"Who was the president of United States in 1984?"
}'
```

OR

use the sample python code provided in the repo [here](https://github.com/AyushDhimann/OllamaServer/blob/main/client-sample.py)

# FAQ

### 1. How to stop the server?
A. Run this command ``` service ollama stop ```

### 2. How to start a stopped server?
A. Run this command ``` service ollama start ```

### 3. How to install any other model in Ollama?
A. Run this command ``` ollama pull "MODEL_NAME" ```
