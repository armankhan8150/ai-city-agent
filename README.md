# City Agent

A human-in-the-loop AI assistant that provides real-time **weather** and **news** for any city. Built with [LangChain](https://www.langchain.com/), [Mistral AI](https://mistral.ai/), and [Tavily](https://tavily.com/).

## Features

- **Real-time weather** via OpenWeatherMap API
- **Latest city news** via Tavily search
- **Human-in-the-loop approval** — you confirm every tool call before it runs
- **Honest AI** — the agent never fabricates data; if a tool is denied, it says so

## Demo

`
City Agent | Type exit to quit

You: What's the weather and latest news in Tokyo?

Agent wants to call 'get_weather'. Approve? (yes/no): yes
Agent wants to call 'get_news'. Approve? (yes/no): yes

Bot: Here's the update for Tokyo:

Weather: clear sky, 28°C

Latest news:
- Tokyo hosts record-breaking summer festival ...
`

## Tech Stack

| Component | Technology |
|-----------|-----------|
| LLM | Mistral AI (mistral-small-2506) |
| Agent Framework | LangChain |
| Weather | OpenWeatherMap API |
| News Search | Tavily |
| CLI Output | Rich |

## Project Structure

`
city-agent/
  main.py          # Agent, tools, and chat loop
  requirements.txt # Python dependencies
  .env.example     # Environment variable template
  .gitignore       # Files excluded from Git
  README.md        # This file
`

## Setup

### 1. Clone the repository

`ash
git clone https://github.com/<your-username>/city-agent.git
cd city-agent
`

### 2. Create a virtual environment

`ash
python -m venv venv
source venv/bin/activate        # macOS / Linux
venv\Scripts\activate           # Windows
`

### 3. Install dependencies

`ash
pip install -r requirements.txt
`

### 4. Configure environment variables

Copy .env.example to .env and fill in your API keys:

`ash
cp .env.example .env
`

`env
OPENWEATHER_API_KEY=your_openweathermap_key
TAVILY_API_KEY=your_tavily_key
MISTRAL_API_KEY=your_mistral_key
`

| Variable | Where to get it |
|----------|----------------|
| OPENWEATHER_API_KEY | [openweathermap.org/api](https://openweathermap.org/api) |
| TAVILY_API_KEY | [app.tavily.com](https://app.tavily.com) |
| MISTRAL_API_KEY | [console.mistral.ai](https://console.mistral.ai) |

### 5. Run

`ash
python main.py
`

## How It Works

1. You type a city-related question.
2. The LLM decides which tools to call (get_weather, get_news, or both).
3. **Before each tool runs**, the middleware pauses and asks for your approval.
4. The tool result is returned to the LLM, which formulates a final response.

## License

MIT
