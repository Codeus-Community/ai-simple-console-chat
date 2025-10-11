# AI Chat Completion - Hard Mode 🔥

A minimalist implementation challenge for building a chat application using AI APIs with **zero scaffolding**.

## 🎓 Learning Outcomes

By completing this challenge, you will:
- Understand that LLM APIs are just HTTP endpoints
- Learn to parse streaming responses (SSE format)
- Handle async operations in Python
- Design your own API client architecture
- Debug raw HTTP requests/responses
- Appreciate what SDKs actually do

## 🎯 The Challenge

You get 3 files and nothing else. Build a fully functional chat application that communicates with OpenAI and Anthropic APIs. No predefined classes, no structure, no safety nets.

**Your playground:**
```
├── requirements.txt   # Dependencies
├── app.py             # Your entire implementation
├── constants.py       # API keys and endpoints
└── README.md          
```

## 🏆 Final Goal

Create a command-line chat application that:

1. **Supports both OpenAI and Anthropic APIs**
    - User can choose which provider to use
    - Both use raw HTTP requests (no SDK required, but allowed as bonus)

2. **Implements two modes:**
    - **Regular mode**: Send message → get complete response
    - **Streaming mode**: Send message → stream response word-by-word

3. **Maintains conversation history**
    - AI remembers previous messages in the conversation
    - System prompt is included in every request

4. **Provides smooth UX**
    - Clear prompts and instructions
    - Streaming output appears in real-time in console
    - Clean exit mechanism

## 📋 Requirements

### Functional Requirements

**Must Have:**
- ✅ Chat loop that accepts user input continuously
- ✅ Support for OpenAI `/chat/completions` endpoint
- ✅ Support for Anthropic `/messages` endpoint
- ✅ Both regular and streaming responses
- ✅ Conversation history (AI sees previous messages)
- ✅ System prompt configuration
- ✅ Visual streaming in console (text appears progressively)

**Should Have:**
- Provider selection at startup (OpenAI/Anthropic)
- Mode selection at startup (streaming/regular)
- Graceful error handling
- API key validation
- Both raw HTTP AND SDK implementations

**Nice to Have:**
- Support for switching providers mid-conversation
- Conversation export/save
- Token usage tracking

### Technical Constraints

- **Python 3.13+**
- **Use `requests` for synchronous HTTP calls**
- **Use `aiohttp` for asynchronous streaming**
- **Environment variables for API keys**
- **No frameworks** (Flask, FastAPI, etc.)
- **No pre-built chat libraries**

## 🔧 Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set API keys as environment variables:**
   ```bash
   export OPENAI_API_KEY='your-key-here'
   export ANTHROPIC_API_KEY='your-key-here'
   ```

3. **Run:**
   ```bash
   python app.py
   ```

## 📚 API Quick Reference

### OpenAI Chat Completions

**Endpoint:** `https://api.openai.com/v1/chat/completions`

**Headers:**
```
Authorization: Bearer {YOUR_API_KEY}
Content-Type: application/json
```

**Request Body:**
```json
{
  "model": "gpt-4o-mini",
  "messages": [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
  ],
  "stream": false
}
```

**Key Response Fields:**
- Regular: `response.choices[0].message.content`
- Streaming: Each chunk contains `choices[0].delta.content`
- Streaming chunks start with `"data: "` (6 characters)
- Streaming ends with `"data: [DONE]"`

**Docs:** https://platform.openai.com/docs/api-reference/chat

---

### Anthropic Messages

**Endpoint:** `https://api.anthropic.com/v1/messages`

**Headers:**
```
x-api-key: {YOUR_API_KEY}
anthropic-version: 2023-06-01
Content-Type: application/json
```

**Request Body:**
```json
{
  "model": "claude-sonnet-4-20250514",
  "max_tokens": 1024,
  "system": "You are a helpful assistant.",
  "messages": [
    {"role": "user", "content": "Hello!"}
  ],
  "stream": false
}
```

**Key Response Fields:**
- Regular: `response.content[0].text`
- Streaming: Look for `content_block_delta` events with `delta.text`
- Streaming chunks start with `"data: "` (6 characters)
- Streaming ends with event type `"message_stop"`

**Docs:** https://docs.anthropic.com/en/api/messages

---

## 🧠 Design Considerations

Think about:

1. **Architecture**
    - How will you structure your code?
    - Do you need classes or will functions suffice?
    - How to avoid code duplication between providers?

2. **State Management**
    - How to store conversation history?
    - How to format messages for each API?
    - System prompt: separate message vs. special field?

3. **Streaming**
    - Parsing Server-Sent Events (SSE) format
    - Handling partial JSON chunks
    - Real-time console output without buffering

4. **Error Handling**
    - Network failures
    - Invalid API keys
    - Rate limits
    - Malformed responses

## ✅ Success Criteria

Your application passes if:

1. **OpenAI streaming works:**
    - Text appears word-by-word in console
    - AI responds contextually to conversation history

2. **Anthropic streaming works:**
    - Text appears progressively in console
    - AI responds contextually to conversation history

3. **Regular mode works for both:**
    - Complete response appears at once
    - Conversation history maintained

4. **Clean UX:**
    - No crashes on typical user input
    - Clear indication of what's happening
    - Easy to exit

## 💡 Hints

<details>
<summary>Stuck on streaming? Click here</summary>

Streaming responses use Server-Sent Events (SSE) format:
```python
async with aiohttp.ClientSession() as session:
    async with session.post(url, headers=headers, json=data) as resp:
        async for line in resp.content:
            if line.startswith(b'data: '):
                chunk_data = line[6:].decode('utf-8')
                # Parse JSON and extract content
```
</details>

<details>
<summary>Conversation history not working?</summary>

For OpenAI: System message is in the `messages` array
```python
messages = [
    {"role": "system", "content": "System prompt"},
    {"role": "user", "content": "First message"},
    {"role": "assistant", "content": "First response"},
    {"role": "user", "content": "Second message"}
]
```

For Anthropic: System prompt is separate, messages array has no system role
```python
{
    "system": "System prompt",
    "messages": [
        {"role": "user", "content": "First message"},
        {"role": "assistant", "content": "First response"},
        {"role": "user", "content": "Second message"}
    ]
}
```
</details>

---

**Good luck! Remember: If you can build this from scratch, you truly understand how to work with LLM APIs.** 🚀