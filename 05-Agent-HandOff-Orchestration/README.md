
#  Agents Handoff with OpenAI Agents SDK + Gemini

This project demonstrates how to implement **automatic agent handoff** based on language detection using the [OpenAI Agents SDK](https://github.com/openai/agents) and the Gemini model via an OpenAI-compatible API.

##  Overview

The app includes three agents:

-  **Urdu Agent** – Responds to users in Urdu.
- 🇬🇧 **English Agent** – Responds to users in English.
- **Triage Agent** – Detects the input language and hands off the query to the appropriate agent.

### Example Input:
```

ٓاپ کیسے ہیں؟

````

### Expected Output:
Handled by Urdu Agent (with response in Urdu).

## 🏗️ Tech Stack

- Python 3.12+
- OpenAI Agents SDK
- Gemini API (OpenAI-compatible endpoint)
- dotenv for environment management

## 🔧 Setup Instructions
### 2. Create a Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Add Your API Key

Create a `.env` file in the root directory with the following content:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

### 5. Run the Application

```bash
python main.py
```

## 🧠 Concept

This project uses the `handoffs` feature of the OpenAI Agents SDK to route user messages to the correct agent based on the message content (e.g., language). It's a simple but powerful pattern to support multilingual or multi-domain conversational systems.

## 📎 Output Example

```bash
ٓاپ کیسے ہیں؟
→ Routed to: Urdu agent
→ Response: میں ٹھیک ہوں، شکریہ! آپ کیسے ہیں؟
```

## 📄 License

MIT License – free to use, modify, and distribute.

---

## 🔮 Future Ideas

* Add more language agents (e.g., French, Arabic)
* Use a language detection model before handoff
* Build a web interface using Streamlit or FastAPI

```

Let me know if you'd like this as a downloadable file or if you want a version tailored for deployment (e.g., on Streamlit Cloud or Hugging Face Spaces).
```
