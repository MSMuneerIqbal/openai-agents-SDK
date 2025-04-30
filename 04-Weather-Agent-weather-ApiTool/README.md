
---

## 🌦️ Weather Agent with Chainlit & OpenAI Agent SDK

This is an AI-powered weather assistant that provides real-time weather information using [WeatherAPI](https://www.weatherapi.com/) and responds in natural language via the [OpenAI Agent SDK](https://github.com/openai/agents).

Built with **Chainlit** for an interactive UI, this agent can tell users the current weather of any city by calling a custom function.

---

### 🚀 Features

- ☁️ **Real-time Weather Data** using WeatherAPI
- 🧠 **AI Natural Language Understanding** via Gemini-powered LLM
- 🔄 **Function Calling** using OpenAI Agent SDK’s `function_tool`
- 💬 **Interactive Web Chat UI** via Chainlit

---

### 🧱 Tech Stack

- `Python`
- `OpenAI Agent SDK`
- `Chainlit`
- `WeatherAPI`
- `Gemini 2.0 Flash Model` (OpenAI-compatible endpoint)

---

### 📂 Project Structure

```
.
├── agents/
│   └── (Your agent toolkit files)
├── .env
├── main.py
├── requirements.txt
└── README.md
```

---

### ⚙️ Setup Instructions

#### 1. Clone the Repository

```bash
git clone https://github.com/your-username/weather-agent.git
cd weather-agent
```

#### 2. Create a `.env` File

```env
GEMINI_API_KEY=your_gemini_api_key
```

#### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

#### 4. Run the Weather Agent

```bash
chainlit run main.py
```

Open [http://localhost:8000](http://localhost:8000) to chat with your Weather Agent.

---

### 💡 Example Commands

- "What's the weather like in Islamabad?"
- "Tell me the current temperature in New York."
- "How’s the weather today in Tokyo?"

---

### 🔐 API Notes

You need a valid [WeatherAPI key](https://www.weatherapi.com/) which is hardcoded for now:
```python
http://api.weatherapi.com/v1/current.json?key=8e3aca2b91dc4342a1162608252604&q={city}
```

➡️ You should move this key to `.env` for better security.

---

### 🛡️ Security Tip

Consider replacing this line:
```python
result=requests.get(f"http://api.weatherapi.com/v1/current.json?key=8e3aca2b91dc4342a1162608252604&q={city}")
```
with:
```python
weather_api_key = get_key(find_dotenv(), "WEATHER_API_KEY")
...
result = requests.get(f"http://api.weatherapi.com/v1/current.json?key={weather_api_key}&q={city}")
```

And update your `.env`:
```
WEATHER_API_KEY=your_weather_api_key
```

---

### 🙏 Acknowledgments

- [Chainlit](https://chainlit.io)
- [WeatherAPI](https://www.weatherapi.com/)
- [OpenAI Agent SDK](https://github.com/openai/agents)
- [Gemini API](https://ai.google.dev/)

---
