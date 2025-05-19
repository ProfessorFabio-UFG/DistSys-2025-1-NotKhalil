import zmq
import time
import requests
from constPS import *

context = zmq.Context()
s = context.socket(zmq.PUB)
s.bind(f"tcp://{HOST}:{PORT}")

def get_weather():
    try:
        # Fetch data for Goiânia, Brazil
        response = requests.get("https://wttr.in/Goiânia?format=%C+%t+%h&m")
        weather, temp, humidity = response.text.strip().split()
        return {
            'temp': temp,
            'humidity': humidity.replace('%', ''),
            'weather': weather
        }
    except Exception as e:
        print(f"Error: {e}")
        return None

while True:
    time.sleep(20)
    data = get_weather()
    
    # Publish TIME
    s.send_string(f"TIME {time.ctime()}")
    
    if data:
        # Publish Weather
        s.send_string(f"Weather {data['weather']}, {data['temp']} in Goiânia")
        # Publish humidity
        s.send_string(f"humidity {data['humidity']}% in Goiânia")
