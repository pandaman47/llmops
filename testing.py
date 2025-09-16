import os
import datetime
import requests
import json
from test_get_weather import get_current_weather
from test_get_weather import get_forecast_weather

directory = "./test"
os.makedirs(directory, exist_ok=True)

timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
filename = os.path.join(directory, f"test_{timestamp}.json")
print(filename)

#response = get_current_weather("London","83dbfb20256103927eaadf415ec45f1f")
response = get_forecast_weather("London","83dbfb20256103927eaadf415ec45f1f")
#print(response["weather"][0]["description"])
response_text = json.dumps(response, indent=4)
#print(response_text)
with open(filename, "w") as file:
    #json.dump(response, file)
    file.write(response_text)

    print(f"Response saved to {filename}")

    print(f"response text type: {type(response_text)}")

