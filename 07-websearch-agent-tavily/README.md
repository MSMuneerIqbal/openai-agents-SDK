
# 🔎 Web-Integrated AI Agent using Gemini & Tavily

This project demonstrates an AI Agent powered by **Google's Gemini LLM** and **Tavily Web Search API** to fetch real-time data from the internet. The agent can intelligently decide whether to respond using its own knowledge or search online to retrieve current information.

## 🚀 Features

- 🌐 Real-time web search using **Tavily API**
- 🧠 Language understanding and reasoning powered by **Gemini 2.0 Flash**
- 🔧 Function-tool integration for dynamic tool use
- 🤖 Natural and emoji-enhanced responses
- ✅ Works with queries like:  
  `"Call search tool and tell what is the today's dollar to PKR price rate"`

---

## 🛠️ Tech Stack

- Python
- [agents](https://github.com/langchain-ai/langgraph) (agentic framework)
- Gemini via OpenAI-compatible API
- Tavily Web Search API
- LangChain-style tool wrapping
- `dotenv` for secure API key management

---

## 📁 Project Structure

```

.
├── agents/
│   └── tool.py       # Function tool wrapper
├── main.py           # Entry point for the AI agent
├── .env              # Contains API keys
└── README.md

````

---

## 🔐 Environment Variables

Create a `.env` file in the root directory with the following keys:

```env
GEMINI_API_KEY=your_gemini_api_key
TAVILY_API_KEY=your_tavily_api_key
````

---

## 🧠 How It Works

1. **Gemini** is initialized using the OpenAI-compatible endpoint.
2. A `function_tool` wraps the Tavily search function.
3. An `Agent` is defined with search capabilities and emoji-enhanced responses.
4. The agent runs a query and intelligently decides to search or respond directly.

---

## ▶️ Running the Project

```bash
pip install -r requirements.txt
python main.py
```

---

## 🧪 Example Output

**Input:**

> Call search tool and tell what is the today's dollar to PKR price rate

**Output:**

> The current USD to PKR exchange rate is 278.35 💵

---

## 📜 License

This project is licensed under the MIT License.

---

## 🙌 Acknowledgements

* [Google Gemini API](https://ai.google.dev/gemini-api/docs/openai)
* [Tavily](https://www.tavily.com/)
* [LangChain Agents Toolkit](https://www.langchain.com/)

---
