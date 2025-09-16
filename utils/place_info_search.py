import os
import json
from langchain_tavily import TavilySearch
from langchain_google_community import GooglePlacesTool, GooglePlacesAPIWrapper


class GooglePlaceSearchTool:
    
    def __init__(self, api_key: str = None):
        self.gplaces_wrapper = GooglePlacesAPIWrapper(gplaces_api_key=api_key)
        self.gplaces_tool = GooglePlacesTool(api_wrapper=self.gplaces_wrapper)
        
    def google_search_attractions(self, place:str) -> dict:

        
        """
        Searches for attractions in a given place using Google Places API.

        Args:
            place (str): The location to search for attractions.

        Returns:
            dict: A dictionary containing the search results.
        """
        try:
            result = self.gplaces_tool.run(f"top attractive places in and around {place}")
            return json.loads(result)
        except Exception as e:
            return {"error": str(e)}
    
    def google_search_restaurants(self, place:str) -> dict:
        """
        Searches for restaurants in a given place using Google Places API.

        Args:
            place (str): The location to search for restaurants.

        Returns:
            dict: A dictionary containing the search results.
        """
        try:
            result = self.gplaces_tool.run(f"top restaurants in and around {place}")
            return json.loads(result)
        except Exception as e:
            return {"error": str(e)}

    def google_search_activity(self, place:str) -> dict:
        """
        Searches for popular activities in a given place using Google Places API.

        Args:
            place (str): The location to search for activities.

        Returns:
            dict: A dictionary containing the search results.
        """
        try:
            result = self.gplaces_tool.run(f"top activities in and around {place}")
            return json.loads(result)
        except Exception as e:
            return {"error": str(e)}

    def google_search_transport(self, place:str) -> dict:
        """
        Searches for transportation options in a given place using Google Places API.

        Args:
            place (str): The location to search for transportation options.

        Returns:
            dict: A dictionary containing the search results.
        """
        try:
            result = self.gplaces_tool.run(f"what are the different modes of transportations available in {place}")
            return json.loads(result)
        except Exception as e:
            return {"error": str(e)}    
class TavilyPlaceSearchTool:
    def __init__(self, api_key: str = None):
        self.tavily_search = TavilySearch(api_key=api_key)
        
    def tavily_search_attractions(self, place:str) -> dict:
        """
        Searches for attractions in a given place using Tavily API.

        Args:
            place (str): The location to search for attractions.

        Returns:
            dict: A dictionary containing the search results.
        """
        try:
            tavily_tool = TavilySearch(topic="general", include_answer=True)
            result = tavily_tool.invoke({"query": f"top attractive places in and around {place}"})
            return result
        except Exception as e:
            return {"error": str(e)}

    def tavily_search_restaurants(self, place:str) -> dict:
        """
        Searches for restaurants in a given place using Tavily API.

        Args:
            place (str): The location to search for restaurants.

        Returns:
            dict: A dictionary containing the search results.
        """
        try:
            tavily_tool = TavilySearch(topic="general", include_answer=True)
            result = tavily_tool.invoke({"query": f"what are the top 10 restaurants and eateries in and around {place}"})
            return result
        except Exception as e:
            return {"error": str(e)}
    
    def tavily_search_activity(self, place:str) -> dict:
        """
        Searches for popular activities in a given place using Tavily API.

        Args:
            place (str): The location to search for activities.

        Returns:
            dict: A dictionary containing the search results.
        """
        try:
            tavily_tool = TavilySearch(topic="general", include_answer=True)
            result = tavily_tool.invoke({"query": f"what are the popular activities in and around {place}"})
            return result
        except Exception as e:
            return {"error": str(e)}

    def tavily_search_transport(self, place:str) -> dict:
        """
        Searches for transportation options in a given place using Tavily API.

        Args:
            place (str): The location to search for transportation options.

        Returns:
            dict: A dictionary containing the search results.
        """
        try:
            tavily_tool = TavilySearch(topic="general", include_answer=True)
            result = tavily_tool.invoke({"query": f"what are the different modes of transportations available in {place}"})
            return result
        except Exception as e:
            return {"error": str(e)}
    