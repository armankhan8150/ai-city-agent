# AI City Agent

A human-in-the-loop AI assistant that provides real-time **weather** and **news** information for any city.

Built with [LangChain](https://www.langchain.com/), [Mistral AI](https://mistral.ai/), and [Tavily](https://tavily.com/).

## Features

- **Real-time weather** via the OpenWeatherMap API
- **Latest city news** via Tavily Search
- **Human-in-the-loop approval** — you confirm every tool call before it runs
- **Honest AI behavior** — the agent never fabricates tool data; if a tool call is denied, it clearly communicates that to the user
- **Tool-based decision making** — the LLM decides whether to use the weather tool, news tool, or both

## Demo

```text
AI City Agent | Type 'exit' to quit

You: What's the weather and latest news in Tokyo?

Agent wants to call 'get_weather'. Approve? (yes/no): yes

Agent wants to call 'get_news'. Approve? (yes/no): yes

Bot: Here's the update for Tokyo:

Weather: clear sky, 28°C

Latest news:
- Tokyo hosts record-breaking summer festival ...
```

## Tech Stack

| Component | Technology |
|-----------|------------|
| LLM | Mistral AI (`mistral-small-2506`) |
| Agent Framework | LangChain |
| Weather | OpenWeatherMap API |
| News Search | Tavily |
| CLI Output | Rich |
| Language | Python |

## Project Structure

```text
ai-city-agent/
├── main.py              # Agent, tools, and chat loop
├── requirements.txt     # Python dependencies
├── .env.example         # Environment variable template
├── .gitignore           # Files excluded from Git
├── LICENSE              # Project license
└── README.md            # Project documentation
```

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/ai-city-agent.git
cd ai-city-agent
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment:

**macOS / Linux**

```bash
source venv/bin/activate
```

**Windows**

```powershell
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Copy `.env.example` to `.env`:

**macOS / Linux**

```bash
cp .env.example .env
```

**Windows**

```powershell
copy .env.example .env
```

Then add your API keys to `.env`:

```env
OPENWEATHER_API_KEY=your_openweathermap_key
TAVILY_API_KEY=your_tavily_key
MISTRAL_API_KEY=your_mistral_key
```

### API Keys

| Variable | Provider |
|----------|----------|
| `OPENWEATHER_API_KEY` | [OpenWeatherMap](https://openweathermap.org/api) |
| `TAVILY_API_KEY` | [Tavily](https://app.tavily.com/) |
| `MISTRAL_API_KEY` | [Mistral AI](https://console.mistral.ai/) |

> **Important:** Never commit your `.env` file or expose your API keys publicly. The `.env` file is excluded through `.gitignore`.

### 5. Run the application

```bash
python main.py
```

## How It Works

1. You enter a city-related question.
2. The LLM analyzes the request and determines which tool or tools are required.
3. Before each tool executes, the human-in-the-loop middleware pauses and asks for approval.
4. If approved, the requested tool executes.
5. The tool result is returned to the LLM.
6. The LLM uses the tool results to formulate the final response.
7. If a tool call is denied, the agent informs the user instead of fabricating information.

## Example Queries

```text
What's the weather in Tokyo?

What is the latest news from London?

Give me the weather and latest news for New York.

What's happening in Dubai today?
```

## Human-in-the-Loop

The agent uses human approval before executing external tools.

For example:

```text
Agent wants to call 'get_weather'. Approve? (yes/no):
```

This provides an additional layer of control and transparency over external tool execution.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
