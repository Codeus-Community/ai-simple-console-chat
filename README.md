# AI Simple Console Chat Task

A Python implementation task for building a chat application using AI API with both synchronous and streaming completions.

## 🎯 Task Overview

Implement a command-line chat application that communicates with the AI API. You'll need to complete the missing methods in `client.py` and `app.py` following the provided TODO instructions.

## 🎓 Learning Goals

By completing this task, you will learn:
- Work with endpoint to communicate with LLM
- Work with REST requests to LLM
- Handle REST responses from LLM
- Handle stream responses from LLM
- Break down illusions of *magic* and *complication* of working with AI API


## 📋 Requirements

- Python 3.13
- pip
- OPENAI API key
- ANTHROPIC API key
- Basic understanding of HTTP requests and async/await

## 🔧 Setup
1. Move to the directory `ai-chat-completions-api`
   ```bash
   cd ./ai-chat-completions-api/
   ```
2. **Setup venv: (also can be configured via IDE)**
   ```bash
   python -m venv .venv
   ```
3. **Activate venv**
   Mac/Linux
   ```bash
   source venv/bin/activate
   ```   
   Windows
   ```bash
   venv\Scripts\activate.bat
   ```
4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set your API key:**
    - Set OPENAI_API_KEY as env variable, https://platform.openai.com/settings/organization/api-keys
    - Set ANTHROPIC_API_KEY as env variable, https://console.anthropic.com/settings/keys

5. **Project structure:**
   ```
   task/
   ├── models/
   │   ├── conversation.py       ✅ Complete
   │   ├── message.py            ✅ Complete  
   │   └── role.py               ✅ Complete
   ├── clients/              
   │   ├── base.py               ✅ Complete
   │   ├── anthropic/    
   │   │   ├── client.py         🚧 TODO: OPTIONAL Implement methods
   │   │   └── custom_client.py  🚧 TODO: OPTIONAL Implement methods
   │   └── openai/    
   │       ├── base.py/          🚧 TODO: Implement constructor
   │       ├── client.py         🚧 TODO: Implement methods
   │       └── custom_client.py  🚧 TODO: Implement methods
   ├── app.py                    🚧 TODO: Implement main logic
   └── constants.py              🚧 Update API keys
   ```

## 📝 Your Tasks

### 1. Complete [app.py](task/app.py)
Implement the `start()` function:

- Handle user input and conversation flow
- Choose between streaming and regular completion
- Implement clients and test with them with non-streaming and streaming modes

### 2. Complete [OpenAI Client](task/clients/openai/client.py) and test it
### 3. Complete [OpenAI Custom Client](task/clients/openai/custom_client.py) and test it
### 4. Optional: Complete [Anthropic Client](task/clients/anthropic/client.py) and test it
### 5. Optional: Complete [Anthropic Custom Client](task/clients/anthropic/custom_client.py) and test it


## 🔍 API Reference

### OpenAI:

<details> 
<summary>Examples of  API requests</summary>

**Only required fields in request body:**
```json
{
  "messages": [
    {
      "role": "system",
      "content": "You are a helpful assistant."
    },
    {
      "role": "user",
      "content": "What is the capital of France?"
    }
  ]
}
```

Full request:
```
POST https://api.openai.com/v1/chat/completions
Authorization: Bearer {YOUR_API_KEY}
Content-Type: application/json

{
  "model": "gpt-5",
  "messages": [
    {
      "role": "system",
      "content": "You are a helpful assistant."
    },
    {
      "role": "user",
      "content": "What is the capital of France?"
    }
  ],
  "stream": true
}
```

</details> 

<details> 
<summary>Example of API regular REST responses</summary>

```json
{
  "id": "chatcmpl-C4A56QmyOUaHa3OIP16xAWj2HI59x",
  "object": "chat.completion",
  "created": 1755108100,
  "model": "gpt-5-2025-08-07",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Hi! How can I help you today?",
        "refusal": null,
        "annotations": []
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 24,
    "completion_tokens": 82,
    "total_tokens": 106,
    "prompt_tokens_details": {
      "cached_tokens": 0,
      "audio_tokens": 0
    },
    "completion_tokens_details": {
      "reasoning_tokens": 64,
      "audio_tokens": 0,
      "accepted_prediction_tokens": 0,
      "rejected_prediction_tokens": 0
    }
  },
  "service_tier": "default",
  "system_fingerprint": null
}
```

</details> 


<details> 
<summary>Examples of  API responses from streaming</summary>

<b>Pay attention that it starts from 'data: ' (it has 6 chars and then content)</b>

```
data: {
  "id": "chatcmpl-C4A7ZT30FfXfWmUPW4n9nC4jY1Xbl",
  "object": "chat.completion.chunk",
  "created": 1755108253,
  "model": "gpt-5-2025-08-07",
  "service_tier": "default",
  "system_fingerprint": null,
  "choices": [
    {
      "index": 0,
      "delta": {
        "role": "assistant",
        "content": "",
        "refusal": null
      },
      "finish_reason": null
    }
  ],
  "obfuscation": "zjRx6ql"
}
```

```
data: {
  "id": "chatcmpl-C4A7ZT30FfXfWmUPW4n9nC4jY1Xbl",
  "object": "chat.completion.chunk",
  "created": 1755108253,
  "model": "gpt-5-2025-08-07",
  "service_tier": "default",
  "system_fingerprint": null,
  "choices": [
    {
      "index": 0,
      "delta": {
        "content": "Hi"
      },
      "finish_reason": null
    }
  ],
  "obfuscation": "5iKK3Ix"
}
```

```
data: {
  "id": "chatcmpl-C4A7ZT30FfXfWmUPW4n9nC4jY1Xbl",
  "object": "chat.completion.chunk",
  "created": 1755108253,
  "model": "gpt-5-2025-08-07",
  "service_tier": "default",
  "system_fingerprint": null,
  "choices": [
    {
      "index": 0,
      "delta": {
        "content": "!"
      },
      "finish_reason": null
    }
  ],
  "obfuscation": "6RYfHQT2"
}
```

```
data: {
  "id": "chatcmpl-C4A7ZT30FfXfWmUPW4n9nC4jY1Xbl",
  "object": "chat.completion.chunk",
  "created": 1755108253,
  "model": "gpt-5-2025-08-07",
  "service_tier": "default",
  "system_fingerprint": null,
  "choices": [
    {
      "index": 0,
      "delta": {},
      "finish_reason": "stop"
    }
  ],
  "obfuscation": "qfd"
}
```

When streaming is finished it returns `[DONE]`
```
data: [DONE]
```
</details> 

### Anthropic:

<details> 
<summary>Examples of API requests</summary>

**Only required fields in request body:**

```json
{
  "model": "claude-sonnet-4-20250514",
  "max_tokens": 1024,
  "messages": [
    {
      "role": "user",
      "content": "Hello, world"
    }
  ]
}
```

Full request:
```
POST https://api.anthropic.com/v1/messages
x-api-key: {YOUR_API_KEY}
anthropic-version: 2023-06-01
Content-Type: application/json

{
    "model": "claude-sonnet-4-20250514",
    "system": "This is a SYSTEM prompt",
    "max_tokens": 1024,
    "messages": [
        {"role": "user", "content": "Hello, world"}
    ]
}
```
</details> 

<details> 
<summary>Example of API regular REST responses</summary>

```json
{
  "id": "msg_01LZe5JV2gug5qHHubqE7s2A",
  "type": "message",
  "role": "assistant",
  "model": "claude-sonnet-4-20250514",
  "content": [
    {
      "type": "text",
      "text": "Hello! How can I help you today?"
    }
  ],
  "stop_reason": "end_turn",
  "stop_sequence": null,
  "usage": {
    "input_tokens": 21,
    "cache_creation_input_tokens": 0,
    "cache_read_input_tokens": 0,
    "output_tokens": 12,
    "service_tier": "standard"
  }
}
```

</details> 

<details> 
<summary>Examples of API responses from streaming</summary>

<b>Pay attention that it starts from 'data: ' (it has 6 chars and then content)</b>

```
data: {
  "type": "message_start",
  "message": {
    "id": "msg_01VoDNeSvgTZ9us7PbpUSCZn",
    "type": "message",
    "role": "assistant",
    "model": "claude-sonnet-4-20250514",
    "content": [],
    "stop_reason": null,
    "stop_sequence": null,
    "usage": {
      "input_tokens": 21,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 0,
      "output_tokens": 8,
      "service_tier": "standard"
    }
  }
}
```

```
data: {
  "type": "content_block_start",
  "index": 0,
  "content_block": {
    "type": "text",
    "text": ""
  }
}
```

```
data: {
  "type": "ping"
}
```

```
data: {
  "type": "content_block_delta",
  "index": 0,
  "delta": {
    "type": "text_delta",
    "text": "Hello! How can I help you today"
  }
}
```

```
data: {
  "type": "content_block_delta",
  "index": 0,
  "delta": {
    "type": "text_delta",
    "text": "?"
  }
}
```

```
data: {
  "type": "content_block_stop",
  "index": 0
}
```

```
data: {
  "type": "message_delta",
  "delta": {
    "stop_reason": "end_turn",
    "stop_sequence": null
  },
  "usage": {
    "output_tokens": 12
  }
}
```

When streaming is finished it returns json with type `message_stop`
```
data: {
  "type": "message_stop"
}
```
</details> 

## ✅ Main Criteria for Application Functionality:

1. Streaming in Console:
   > Ensure that the application streams output continuously in the console, reflecting real-time interactions or updates.

2. Conversation History Support:
   > The application should support a history of conversations, allowing LLM to see previous interactions.
   