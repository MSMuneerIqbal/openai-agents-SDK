# 📄 README.md


# Chainlit UI OpenAI Agent (Gemini Model)

This project is an **AI assistant** built using the **OpenAI Agent SDK** and **Google Gemini 1.5 Flash** model,  
with a beautiful and fast **Chainlit UI** frontend for chatting.

---

##  Project Description

- This agent greets users and continues a conversation through a **Chainlit** web interface.
- Powered by **OpenAI Agent SDK** for building intelligent workflows.
- Runs the **Gemini 1.5 Flash** model via Google's API, wrapped in OpenAI SDK format.
- **Chainlit** is used to create an interactive and real-time frontend without any complex setup.

---

##  Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

---

### 2. Create Virtual Environment (using uv)

```bash
uv venv
source .venv/bin/activate    # Linux / MacOS
.venv\Scripts\activate       # Windows
```

---

### 3. Install Dependencies

```bash
uv pip install -r requirements.txt
```

---

### 4. Add Environment Variables

Create a `.env` file at the project root:

```bash
GEMINI_API_KEY=your-gemini-api-key-here
```

---

## 🧩 How to Run

Run the Chainlit app using:

```bash
chainlit run main.py
```

You will see a local web interface (usually at http://localhost:8000) where you can chat with your AI agent!

---

## 🔥 Tech Stack

- **Python 3.10+**
- **OpenAI Agent SDK** (for building the agent)
- **Google Gemini 1.5 Flash** (as the LLM backend)
- **Chainlit** (for frontend UI)
- **uv** (for package management)
- **dotenv** (for managing environment variables)

---

## 📁 Project Structure

```bash
.
├── main.py            # Main Chainlit + OpenAI Agent code
├── .env               # API Keys (not included in repo)
├── requirements.txt   # Dependencies
├── pyproject.toml     # uv project config
└── README.md          # This file
```

---

## 📋 Requirements

- Python 3.10+
- uv installed (`pip install uv`)
- Gemini API Key (from Google AI Console)
- Chainlit installed (`pip install chainlit` if missing)

---

## 📚 Useful Links

- 🔗 [OpenAI Agent SDK Documentation](https://github.com/openai/agents)
- 🔗 [Chainlit Official Documentation](https://docs.chainlit.io/)
- 🔗 [Google Gemini API Documentation](https://ai.google.dev/)

---

## ⚡ Notes

- `set_tracing_disabled(True)` can be used optionally to disable OpenAI internal tracing (not used here but can be added).
- Conversation history is managed by Chainlit's internal session handling.
- The agent uses `AsyncOpenAI` to properly call Gemini APIs within the OpenAI Agent SDK structure.

---

## ✨ Author

Built by [Muneer Iqbal](https://github.com/MSMuneerIqbal/)

---

```

---

✅ This README is **fully professional**, **GitHub-ready**, and **easy for anyone to understand**.  
✅ I have included **all important links** and **Chainlit-specific** instructions too.

---

Would you also like me to quickly create a `requirements.txt` for this project based on your code?  (includes `chainlit`, `python-dotenv`, `agents` etc.)  
Just say "**yes make requirements**"! 🎯
