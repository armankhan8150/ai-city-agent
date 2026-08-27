import os

import requests
from dotenv import load_dotenv

load_dotenv()

from langchain.agents import create_agent
from langchain.agents.middleware import wrap_tool_call
from langchain.tools import tool
from langchain_core.messages import ToolMessage
from langchain_mistralai import ChatMistralAI
from rich import print
from tavily import TavilyClient

# =========================
# Weather Tool
# =========================

@tool
def get_weather(city: str) -> str:
    """Get current weather of a city."""
    url = (
        f"http://api.openweathermap.org/data/2.5/weather"
        f"?q={city}"
        f"&appid={os.getenv('OPENWEATHER_API_KEY')}"
        f"&units=metric"
    )
    response = requests.get(url)
    data = response.json()
    if str(data.get("cod")) != "200":
        return f"Error: {data.get('message', 'Could not fetch weather')}"
    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]
    return f"Weather in {city}: {desc}, {temp}C"


# =========================
# News Tool (Tavily)
# =========================

tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))


@tool
def get_news(city: str) -> str:
    """Get latest news about a city."""
    response = tavily_client.search(
        query=f"latest news in {city}",
        search_depth="basic",
        max_results=3,
    )
    results = response.get("results", [])
    if not results:
        return f"No news found for {city}"
    news_list = []
    for r in results:
        title = r.get("title", "No title")
        url = r.get("url", "")
        snippet = r.get("content", "")
        news_list.append(f"- {title}\n  {url}\n  {snippet[:100]}...")
    return f"Latest news in {city}:\n\n" + "\n\n".join(news_list)


# =========================
# Human-in-the-Loop Middleware
# =========================

@wrap_tool_call
def human_approval(request, handler):
    """Ask for human approval before every tool call."""
    tool_name = request.tool_call["name"]
    confirm = input(f"\nAgent wants to call '{tool_name}'. Approve? (yes/no): ")
    if confirm.lower() != "yes":
        return ToolMessage(
            content="Tool call denied by user.",
            tool_call_id=request.tool_call["id"],
        )
    return handler(request)


# =========================
# Agent Setup
# =========================

llm = ChatMistralAI(model="mistral-small-2506")

agent = create_agent(
    llm,
    tools=[get_weather, get_news],
    system_prompt="""
    You are a helpful city assistant.

    IMPORTANT:
    - Only provide weather information if the get_weather tool successfully returns weather data.
    - If get_weather is denied or fails, clearly tell the user that weather information could not be retrieved.
    - Never guess, invent, or use your own knowledge to provide weather information.
    - Only provide news information from the get_news tool.
    - If a tool call is denied, do not fabricate the missing information.
    """,
    middleware=[human_approval],
)


# =========================
# Chat Loop
# =========================

def main():
    print("City Agent | Type exit to quit\n")
    while True:
        user_input = input("You: ").strip()
        if not user_input:
            continue
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        result = agent.invoke({
            "messages": [{"role": "user", "content": user_input}]
        })
        print(f"\nBot: {result['messages'][-1].content}\n")


if __name__ == "__main__":
    main()
