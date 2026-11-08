# AI City Agent

A tool-calling AI assistant that fetches real-time city weather and news with a strict human-in-the-loop (HITL) approval middleware built with LangChain, Mistral AI, Tavily, and OpenWeatherMap.

---

## How It Works

```
User Query ("What's the weather and news in Karachi?")
    │
    ▼
┌──────────────────┐
│   Mistral LLM     │  ──→  Decides which tools to call based on query intent
└──────────────────┘
    │
    ▼
┌──────────────────────────────┐
│  HITL Approval Middleware     │  ──→  Pauses execution, shows planned tool call
│  (Human confirms or denies)   │       User must explicitly approve before any
└──────────────────────────────┘       external API is called
    │
    ├── Approved ──→ Execute tool (Weather API or News Search)
    │
    └── Denied  ──→ LLM reports denial, does not fabricate data
    │
    ▼
┌──────────────────┐
│   Final Response  │  ──→  Synthesized answer from approved tool results only
└──────────────────┘
```

### Key Design Decisions
- **Human-in-the-loop by design**: no external API call happens without explicit user approval
- **Hallucination prevention**: denied tool calls are reported honestly; the LLM never invents data
- **Dynamic tool selection**: LLM autonomously decides whether to call weather, news, or both based on query intent
- **Transparent execution**: every tool call is shown to the user before it runs

---

## 🛠 Tech Stack

| Component | Technology |
|---|---|
| LLM | Mistral AI (`mistral-small-2506`) |
| Agent Framework | LangChain |
| Weather Data | OpenWeatherMap API |
| News Search | Tavily API |
| CLI Output | Rich |
| Language | Python 3.10+ |

---

## Features

- 🔐 **HITL approval gate**: every tool call requires explicit confirmation
- 🌤 **Real-time weather**: current conditions for any city via OpenWeatherMap
- 📰 **Live news search**: latest city news via Tavily
- 🤖 **Autonomous tool selection**: LLM picks the right tool(s) per query
- 🚫 **Safe denial handling**: denied calls reported cleanly, no fabricated output
- 🖥 **Rich CLI interface**: formatted terminal output

---

## Project Structure

```
├── main.py             # Agent, tools, HITL middleware, and chat loop
├── requirements.txt
├── .env.example
├── LICENSE
└── README.md
```

---

## Getting Started

### Prerequisites
- Python 3.10+
- Mistral AI API key → [console.mistral.ai](https://console.mistral.ai)
- Tavily API key → [tavily.com](https://tavily.com)
- OpenWeatherMap API key → [openweathermap.org](https://openweathermap.org/api)

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/armankhan8150/ai-city-agent.git
cd ai-city-agent

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up environment variables
cp .env.example .env
# Add your API keys to .env
```

### Environment Variables

```env
MISTRAL_API_KEY=your_mistral_api_key
TAVILY_API_KEY=your_tavily_api_key
OPENWEATHERMAP_API_KEY=your_openweathermap_api_key
```

### Run

```bash
python main.py
```

---

## Example Interaction

```
You: What's the weather and latest news in Karachi?

Agent wants to call: get_weather(city="Karachi")
Approve? (yes/no): yes

Agent wants to call: get_news(query="Karachi latest news")
Approve? (yes/no): yes

The weather in Karachi is currently 32°C with clear skies...
Latest news: [synthesized from Tavily results]
```

---

## Roadmap

- [ ] Streamlit web UI
- [ ] Support for multiple cities in one query
- [ ] Approval history log
- [ ] Support for additional tools (traffic, air quality)

---

## Author

**Arman Malik** — AI Engineer
[LinkedIn](https://linkedin.com/in/arman-malik) · [GitHub](https://github.com/armankhan8150)

---

## License

MIT License — see [LICENSE](LICENSE) for details.
