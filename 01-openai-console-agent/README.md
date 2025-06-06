```markdown
## Getting Started with the AI Assistant

This guide will help you set up and run the AI assistant.

**1. Prerequisites**

* Python 3.10+ installed on your system.
* `uv` installed. You can install it using pip:
    ```bash
    pip install uv
    ```
* A valid Gemini API Key from Google.

**2. Create Virtual Environment (with uv)**

```bash
uv venv
source .venv/bin/activate    # For Linux / MacOS
.venv\Scripts\activate       # For Windows
```

**3. Install Dependencies**

```bash
uv pip install -r requirements.txt
```

**4. Environment Variables**

Create a `.env` file in the project root directory and add your Gemini API Key:

```bash
GEMINI_API_KEY=your-gemini-api-key-here
```

**🛠️ How to Run**

Simply execute the following command in your terminal:

```bash
python main.py
```

You will then see the following prompt:

```
Enter your message. Type 'exit' to quit:
```

Type your messages and interact with the AI assistant. To end the conversation, type `exit`.

**🧩 Tech Stack**

* Python
* OpenAI Agents SDK
* `uv` (for environment and package management)
* Google Gemini 1.5 Flash API
* `dotenv` (for environment variables)

**📁 Project Structure**

```
.
├── main.py          # Main console chat agent code
├── .env             # Environment variables (Not included in repo)
├── requirements.txt # Dependencies list
├── pyproject.toml   # (Generated by uv init)
└── README.md        # Project documentation
```

**📋 Requirements**

* Python 3.10+
* `uv` installed (`pip install uv`)
* Valid Gemini API Key from Google

**⚡ Notes**

* `set_tracing_disabled(True)` disables OpenAI's internal tracing for privacy.
* The conversation memory is stored in-memory during the current session.
* The project utilizes `AsyncOpenAI` and `OpenAIChatCompletionsModel` to establish a connection with the Gemini API through the OpenAI SDK structure.
```