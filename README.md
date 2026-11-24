# Vikie — Conversational AI System

Vikie is a Python-based conversational AI application powered by Large Language Models (LLMs). It integrates the Groq API with the GPT-OSS-20B model to generate real-time responses and maintain context across multiple interactions.

The project focuses on implementing core LLM application concepts, including response streaming, tokenization, context management, conversation summarization, and API usage tracking.

## Overview

Unlike a basic request-response chatbot, Vikie maintains conversational context and manages message history to support more meaningful multi-turn interactions.

The application also incorporates token usage monitoring and automatic conversation summarization to manage the context window efficiently.

## Core Capabilities

**1. LLM Integration**

Integrates the GPT-OSS-20B language model through Groq's OpenAI-compatible API.

**2. Streaming Response Generation**

Implements streaming to display model-generated responses incrementally rather than waiting for the entire response.

**3. Conversation Context Management**

Maintains conversation history by storing user and assistant messages, allowing the model to reference previous interactions.

**4. Automatic Conversation Summarization**

Summarizes earlier conversation messages to reduce context usage while retaining important information.

**5. Tokenization and Usage Tracking**

Uses Hugging Face Transformers for tokenization and tracks input, output, and total token consumption.

**6. API Cost Estimation**

Calculates estimated API usage costs based on recorded token consumption.

## Technology Stack

| Component | Technology |
|---|---|
| Programming Language | Python |
| LLM | GPT-OSS-20B |
| LLM Provider | Groq API |
| LLM Integration | OpenAI Python SDK |
| Tokenization | Hugging Face Transformers |
| Environment Management | Python-dotenv |
| Token Utilities | Tiktoken |

## Architecture

```text
          User Input
              |
              v
       Input Tokenization
              |
              v
      Prompt Validation
              |
              v
      Conversation Manager
              |
              v
         Groq API
              |
              v
         GPT-OSS-20B
              |
              v
      Streaming Response
              |
              v
     Conversation History
              |
              v
     Context Summarization
              |
              v
       Usage & Cost Report
```

## Project Structure

```text
AI-Chatbot/
|
|-- chat_bot.py
|-- requirements.txt
|-- Pipfile
|-- Pipfile.lock
|-- .gitignore
|-- README.md
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/v-Krishna06/AI-Chatbot.git
cd AI-Chatbot
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
```

Obtain an API key from [Groq Console](https://console.groq.com/).

### 5. Execute the application

```bash
python chat_bot.py
```

## Key Learning Outcomes

This project provided practical experience with:

- Integrating and interacting with Large Language Models.
- Understanding tokenization and token budgets.
- Implementing real-time LLM response streaming.
- Managing conversational context and message history.
- Building automatic conversation summarization workflows.
- Monitoring API consumption and estimating inference costs.
- Managing API credentials through environment variables.

## Future Scope

- Persistent memory across application sessions.
- Retrieval-Augmented Generation (RAG).
- Document-based question answering.
- Multi-model support.
- Web-based conversational interface.

## Author

**Krishna Kumar Verma**

B.Tech Biotechnology | AI Engineering & Software Development

- GitHub: [v-Krishna06](https://github.com/v-Krishna06)
- LinkedIn: [Krishna Verma](https://www.linkedin.com/in/krishna-verma-54b008367/)

---

*This project is part of my journey into AI Engineering, exploring the practical foundations of building applications powered by Large Language Models.*
