from google.adk.agents import Agent

def get_weather(city: str) -> dict:
    """Retrieves the current weather report for a specified city.

    Returns:
        dict: A dictionary containing the weather information with a 'status' key ('success' or 'error') and a 'report' key with the weather details if successful, or an 'error_message' if an error occurred.
    """
    if city.lower() == "new york":
        return {"status": "success",
                "report": "The weather in New York is sunny with a temperature of 25 degrees Celsius (77 degrees Fahrenheit)."}
    elif city.lower() == "Singapore":
        return {"status": "success",
                "report": "The weather in Singapore is Humid with a temperature of 30 degrees Celsius (100 degrees Fahrenheit)."}
    else:
        return {"status": "error",
                "error_message": f"Weather information for '{city}' is not available."}

def get_current_time(city:str) -> dict:
    """Returns the current time in a specified city.

    Args:
        dict: A dictionary containing the current time for a specified city information with a 'status' key ('success' or 'error') and a 'report' key with the current time details in a city if successful, or an 'error_message' if an error occurred.
    """
    import datetime
    from zoneinfo import ZoneInfo

    if city.lower() == "new york":
        tz_identifier = "America/New_York"
    elif city.lower() == "singapore":
        tz_identifier = "Asia/singapore"
    else:
        return {"status": "error",
                "error_message": f"Sorry, I don't have timezone information for {city}."}

    tz = ZoneInfo(tz_identifier)
    now = datetime.datetime.now(tz)
    return {"status": "success",
            "report": f"""The current time in {city} is {now.strftime("%Y-%m-%d %H:%M:%S %Z%z")}"""}

root_agent = Agent(
    name="weather_time_agent",
    model="gemini-2.0-flash",
    description="Agent to answer general knowledge questions. In addtion, it can answer weather and time information.",
    instruction="You can answer general knowledge conversation questions, and weather and time information.",
    tools=[get_weather, get_current_time]
)