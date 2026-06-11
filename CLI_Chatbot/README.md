# CLI Chatbot

A simple command-line chatbot built with the OpenAI API. This project demonstrates how to create a conversational AI application that maintains chat history, handles user input, and tracks token usage.

## Features

* Multi-turn conversations with context retention
* Custom system prompt support
* Token usage tracking

## Tech Stack

* Python
* OpenAI API
* python-dotenv

## Installation

```bash
pip install openai python-dotenv
```

Add your API key to the `.env` file:

```env
OPENAI_API_KEY=your_api_key_here
```

## Usage

Run the chatbot:

```bash
python chatbot.py
```

Start chatting directly from the terminal. The chatbot maintains conversation history during the session to provide context-aware responses.

## What I Learned

* Integrating the OpenAI Chat Completions API
* Managing conversation history in chat applications
* Understanding how stateless LLMs achieve contextual conversations
* Working with environment variables using `python-dotenv`
* Tracking token usage and API costs
* Implementing basic error handling in Python applications

## Future Improvements

* Save chat history between sessions
* Add response streaming
* Support multiple AI models
* Export conversations to a file
