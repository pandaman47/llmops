import requests
import os
from typing import Any, Dict, Optional, List
from dotenv import load_dotenv

#from utils.weather_info import WeatherForecastTool

from langchain_core.tools import tool

load_dotenv()
        


class WeatherInfoTool:
    
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("WEATHER_API_KEY")
        self.weather_service = WeatherForecastTool(self.api_key)
        self.weather_tool_list = self._setup_tools()

    def _setup_tools(self) -> List:
        """Set up the weather and weather forecast tools."""
        @tool
        def get_current_weather(city: str) -> str:
            """Get current weather for a given city."""
            weather_data = self.weather_service.get_current_weather(city)
            if weather_data:
                temp = weather_data.get('main', {}).get("temp","N/A")
                description = weather_data.get('weather', [{}])[0].get("description", "N/A")
                return f"Current temperature in {city} is {temp}°C with {description}."
            return f"Could not retrieve weather data for {city}."
        
        return [get_current_weather]
    
def get_location_data(city_name, api_key):
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=5&appid={api_key}"
    response = requests.get(url)
    
    if response.status_code == 200:
        print(response.json())  # Return the JSON response if the request was successful
    else:
        print(f"Error: {response.status_code} - {response.text}")

    for key in response:
        print(f"{key}")

def get_current_weather(place:str, api_key:str):
        """Get current weather of a place"""
        base_url = "https://api.openweathermap.org/data/2.5"
        #api_key = os.getenv("WEATHER_API_KEY")
        try:
            url = f"{base_url}/weather"
            params = {
                "q": place,
                "appid": api_key,
            }
            response = requests.get(url, params=params)
            if response.status_code == 200:
                return response.json()  # return the JSON response if the request was successful
            else:
                print(f"Error: {response.status_code} - {response.text}")
        except Exception as e:
            raise e

def get_forecast_weather(place:str, api_key:str):
        """Get weather forecast of a place"""
        base_url = "https://api.openweathermap.org/data/2.5"
        try:
            url = f"{base_url}/forecast"
            params = {
                "q": place,
                "appid": api_key,
                "cnt": 5,
                "units": "metric"
            }
            response = requests.get(url, params=params)
            if response.status_code == 200:
                return response.json()  # Return the JSON response if the request was successful
            else:
                print(f"Error: {response.status_code} - {response.text}")
        except Exception as e:
            raise e

# Example usage
if __name__ == "__main__":
    city_name = "London"  # Replace with your desired city
    api_key = "83dbfb20256103927eaadf415ec45f1f"  # Replace with your actual API key
    #get_location_data(city_name, api_key)
    get_forecast_weather(place=city_name,api_key=api_key)

    #weather_data
    #tools = weather_data.weather_tool_list
    #for tool in tools:
    #    print(f"Tool name: {tool.name}, Description: {tool.description}")
    #input_data = {"city": "New York"}
    #current_weather = tools[0].invoke(input=input_data)
    #print(current_weather)
#
    #location_data = get_location_data(city, api_key)
    #print(location_data)
    
#if __name__ == "__main__":
#    weather_tool = WeatherInfoTool()
#    tools = weather_tool.weather_tool_list
#    for tool in tools:
#        print(f"Tool name: {tool.name}, Description: {tool.description}")
#    input_data = {"city": "New York"}
#    result = requests.get(http://api.openweathermap.org/geo/1.0/direct?q=London&limit=5&appid={83dbfb20256103927eaadf415ec45f1f})
#    print(f"Result: {result}")


