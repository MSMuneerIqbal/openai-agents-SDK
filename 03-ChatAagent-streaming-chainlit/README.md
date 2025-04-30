
---

##  AI Assistant Bot with Chainlit & Gemini API

This project is an interactive AI assistant bot powered by [Chainlit](https://www.chainlit.io/) and Google's Gemini API. The assistant supports real-time streaming responses and maintains chat history across sessions.

###  Features

-  **Streaming Responses**: Real-time token-by-token message rendering.
-  **Context-Aware Conversations**: Maintains conversation history.
- **Gemini API Integration**: Uses Gemini 2.0 Flash model via OpenAI-compatible API.
- **Custom Agent Configuration** using `RunConfig`.

---

### 📂 Project Structure

```
.
├── agents/
│   ├── __init__.py
│   ├── run.py               # Contains RunConfig and Runner logic
│   └── other agent classes
├── .env                     # Contains your GEMINI_API_KEY
├── main.py                  # Main application logic
├── requirements.txt
└── README.md
```

---

###  Setup Instructions

#### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ai-agent-bot.git
cd ai-agent-bot
```

#### 2. Create and Configure `.env`

Create a `.env` file in the root directory with your Gemini API key:

```
GEMINI_API_KEY=your_gemini_api_key_here
```

#### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

#### 4. Run the Bot

```bash
chainlit run main.py
```

Access your assistant at: [http://localhost:8000](http://localhost:8000)

---

### How It Works

- On chat start, a `RunConfig` is created with a Gemini-backed model.
- A custom agent is initialized and saved in session.
- Incoming messages are processed and streamed back using `Runner.run_streamed`.
- The assistant’s response is streamed token-by-token to the user.

---

###  Requirements

- Python 3.9+
- Chainlit
- `openai`, `python-dotenv`

---

### 📸 Demo

*(Add a screenshot or GIF if available)*

---

### 🙏 Acknowledgments

- [Chainlit](https://www.chainlit.io/)
- [Gemini API](https://ai.google.dev/gemini-api/)
- OpenAI-compatible SDKs

---