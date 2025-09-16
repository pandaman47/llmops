import os
from typing import List
from langchain_core.tools import tool
from dotenv import load_dotenv

from utils.place_info_search import GooglePlaceSearchTool, TavilyPlaceSearchTool

class PlaceSearchTool:
    def __init__(self):
        load_dotenv()
        self.google_api_key = os.getenv("GOOGLE_API_KEY")
        self.tavily_api_key = os.getenv("TAVILY_API_KEY")
        self.google_place_search = GooglePlaceSearchTool(api_key=self.google_api_key)
        self.tavily_place_search = TavilyPlaceSearchTool(api_key=self.tavily_api_key)
        self.place_search_tool_list = self._setup_tools()

    def _setup_tools(self) -> List:
        """ setup all the place search tools """
        @tool
        def search_attractions(place: str) -> dict:
            """ 
            Search for attractions in a given place 
            
            args:
                place (str) : The location to search for attractions.
                
            Returns:
                dict : A dictionary containing the search results.
            """
            try:
                google_results = self.google_place_search.google_search_attractions(place)
                if google_results:
                    return f"Google Places Results for attractions in {place}: {google_results}"
            except Exception as e:
                tavily_results = self.tavily_place_search.tavily_search_attractions(place)
                return f"Tavily Results for attractions in {place}: {tavily_results}"
        
        @tool
        def search_restaurants(place: str) -> dict:
            """ 
            Search for restaurants in a given place 
            
            args:
                place (str) : The location to search for restaurants.
                
            Returns:
                dict : A dictionary containing the search results.
            """
            try:
                google_results = self.google_place_search.google_search_restaurants(place)
                if google_results:
                    return f"Google Places Results for restaurants in {place}: {google_results}"
            except Exception as e:
                tavily_results = self.tavily_place_search.tavily_search_restaurants(place)
                return f"Tavily Results for restaurants in {place}: {tavily_results}"
            
        @tool
        def search_activities(place: str) -> dict:
            """ 
            Search for activities in a given place 
            
            args:
                place (str) : The location to search for activities.
                
            Returns:
                dict : A dictionary containing the search results.
            """
            try:
                google_results = self.google_place_search.google_search_activity(place)
                if google_results:
                    return f"Google Places Results for activities in {place}: {google_results}"
            except Exception as e:
                tavily_results = self.tavily_place_search.tavily_search_activities(place)
                return f"Tavily Results for activities in {place}: {tavily_results}"

        @tool
        def search_transportation(place: str) -> dict:
            """ 
            Search for transportation options in a given place 
            
            args:
                place (str) : The location to search for transportation options.
                
            Returns:
                dict : A dictionary containing the search results.
            """
            try:
                google_results = self.google_place_search.google_search_transport(place)
                if google_results:
                    return f"Google Places Results for transport in {place}: {google_results}"
            except Exception as e:
                tavily_results = self.tavily_place_search.tavily_search_transport(place)
                return f"Tavily Results for transport in {place}: {tavily_results}"
            
        return [search_attractions, search_restaurants, search_activities, search_transportation]

        
