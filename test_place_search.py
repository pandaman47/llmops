import os
import logging
import json

from utils.place_info_search import TavilyPlaceSearchTool
#from utils.place_info_search import GooglePlaceSearchTool
#from tools.place_search_tool import PlaceSearchTool
from dotenv import load_dotenv
from langchain_core.tools import tool

load_dotenv()  # Load environment variables from .env file

logging.basicConfig(
    level=logging.DEBUG,
    format= "%(asctime)s - %(levelname)s - %(message)s",
    filename="test_place_search.log",
    filemode="w")

def test_place_search():
    load_dotenv()
    #google_api_key = os.getenv("GOOGLE_API_KEY")
    tavily_api_key = os.getenv("TAVILY_API_KEY")
    #google_place_search = GooglePlaceSearchTool(api_key=self.google_api_key)
    tavily_place_search = TavilyPlaceSearchTool(api_key=tavily_api_key)
    #place_search = PlaceSearchTool()
    place = "New York"
    """List all initialized tools"""
    #for index, tool in enumerate(place_search.place_search_tool_list):
    #    logging.debug(f"Tool {index}: {tool.name}")

    input_data = {
        "place": place
    }
    tavily_results = tavily_place_search.tavily_search_restaurants(place)
    keys_list = list(tavily_results.keys())
    keys = []
    for key in tavily_results["results"]:
        keys.append(key)

    print(f"keys in results are {keys}")
    logging.debug(f"Tavily Results for restaurants in {place}: {tavily_results}")
    #print(f"Tavily Results for restaurants in {place}: {tavily_results}")
    #print(tavily_results['results'].keys())
    #search_attractions_tool = place_search.place_search_tool_list[0]
    #logging.debug(f"attempting to call {search_attractions_tool.name} tool")
    #attractions = search_attractions_tool.invoke(input=input_data)
    #print(f"attractions in {place} are {attractions}")
    #logging.debug(f"success")

if __name__ == "__main__":
    test_place_search()