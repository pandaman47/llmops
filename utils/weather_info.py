import requests

class WeatherForecastTool:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5"
        #self.base_url = http://api.openweathermap.org/geo/1.0/direct?q={city name},{state code},{country code}&limit={limit}&appid={API key}
    
    def get_lat_lon(self, city_name, api_key):
        url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=5&appid={api_key}"
        response = requests.get(url)
        
        if response.status_code == 200:
            return response.json()
    
    def get_current_weather(self, place:str):
        """Get current weather of a place"""
        try:
            url = f"{self.base_url}/weather"
            params = {
                "q": place,
                "appid": self.api_key,
            }
            response = requests.get(url, params=params)
            return response.json() if response.status_code == 200 else {}
        except Exception as e:
            raise e
    
#    def get_current_weather(self, city: str):
#        """Fetch the current weather for a given city."""
#        try:
#            #url = f"{self.base_url}/geo/1.0/direct?q={city},&limit={limit}&appid={API key}"
#            url = f"{self.base_url}/geo/1.0/direct?q={city}&limit=5&appid={self.api_key}"
#            params = {
#                "q": city,
#                "appid": self.api_key,
#                "units": "metric"
#            }
#            response = requests.get(url, params=params)
#            return response.json() if response.status_code == 200 else {}
#        except Exception as e:
#            print(f"Error fetching current weather: {e}")
#            raise e
        
    def get_weather_forecast(self, city: str):
        """Fetch the weather forecast for a given city."""
        try:
            url = f"{self.base_url}/forecast"
            params = {
                "q": city,
                "appid": self.api_key,
                "cnt": 5,
                "units": "metric"
            }
            response = requests.get(url, params=params)
            return response.json() if response.status_code == 200 else {}
        except Exception as e:
            print(f"Error fetching weather forecast: {e}")
            raise e