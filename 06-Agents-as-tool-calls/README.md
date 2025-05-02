#  Agent-as-Tools with OpenAI Agents SDK + Gemini

This project demonstrates how to build a multi-agent system using the OpenAI Agents SDK, where specialized agents (shopping and support) are converted into tools and used by a triage agent to intelligently delegate user queries.

##  Features

- 🤖 **Shopping Assistant Agent** – Helps users find products and make purchase decisions.
- 🎧 **Support Agent** – Assists users with post-purchase concerns like returns and support.
- 📦 **Triage Agent** – Routes user queries to the correct agent based on intent.
- ⚡ Uses the **Gemini API** (via OpenAI-compatible client) for LLM responses.

##  Concept

This project implements **agent-as-tools**, where specialized agents are wrapped as tools and delegated to by a controller agent (`Triage Agent`). This architecture is ideal for scalable task routing.

## 🏗️ Tech Stack

- Python 3.12+
- OpenAI Agents SDK
- Gemini API (via OpenAI-compatible endpoint)
- dotenv

## 🔧 Setup

### 1. Clone the repo

```bash
git clone https://github.com/your-username/agent-as-tools.git
cd agent-as-tools
````

### 2. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file with the following content:

```env
GEMINI_API_KEY=your_gemini_api_key
```

### 5. Run the app

```bash
python main.py
```

## 📎 Example Output

```
I need help with a recent purchase.
→ Routed to Support Agent
→ Response: Let's help you with your return or support request!
```

## 📝 Notes

* Make sure your tool names follow API conventions: no spaces or special characters; use snake\_case.
* This is a simplified demo – extend it with logging, error handling, or an interactive UI.

## 📄 License

MIT – feel free to use and modify.

```
