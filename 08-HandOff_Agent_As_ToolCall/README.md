# HandOff - Triage Agent - Agent As Tolls use
# 🤖 Multi-Agent Developer Assistant with Gemini (Web, Mobile, DevOps & Agentic AI)

This project showcases a multi-agent AI assistant system powered by **Google Gemini (via OpenAI-compatible API)** that dynamically routes user queries to specialized agents: Web Developer, Mobile App Developer, DevOps Engineer, or Agentic AI Developer.

It demonstrates intelligent **triage + handoff logic**, enabling AI to route user queries without needing additional user clarification.

---

## 🧠 Key Features

- 🧑‍💻 **Web Agent** – Handles full-stack web development queries  
- 📱 **Mobile Agent** – Expert in mobile application development  
- 🔧 **DevOps Agent** – Solves DevOps-related questions and CI/CD tasks  
- 🧬 **Agentic AI Agent** – Uses other agents (DevOps, OpenAI Agent) as tools  
- 🔁 **Triage Agent** – Auto-routes user queries to the correct specialized agent without asking the user

---

## 🛠️ Tech Stack

- Python
- [agents](https://github.com/langchain-ai/langgraph) agentic framework
- Gemini 2.0 Flash (OpenAI-compatible endpoint)
- dotenv for secure environment management

---

## 📁 Project Structure

```

.
├── main.py               # Main script with agent logic
├── .env                  # Contains API key
└── README.md

````

---

## 🔐 Environment Setup

Create a `.env` file in the root directory:

```env
GOOGLE_API_KEY=your_google_gemini_api_key
````

---

## 🚀 Running the Agent System

Install dependencies and run:

```bash
pip install -r requirements.txt
python main.py
```

---

## 🧪 Sample Output

**Input Prompt:**

```text
Give Road map of devops engineer
```

**Output:**

```text
<DevOps roadmap with actionable advice...>  
Handled by agent: devops
```

---

## 💡 How It Works

1. The **Triage Agent** receives the user input.
2. It identifies the most suitable agent based on the query context.
3. If applicable, the **Agentic AI** uses **DevOps** or **OpenAI Agent** as tools.
4. Final output is returned with info on which agent handled the request.

---

## 📜 License

MIT License. Use freely with attribution.

---

## 🙌 Acknowledgements

* [Google Gemini API](https://ai.google.dev/gemini-api/docs/openai)
* [LangGraph Agents](https://github.com/langchain-ai/langgraph)

