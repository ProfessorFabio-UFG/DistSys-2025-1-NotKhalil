import zmq, time
from constPS import *  #-

context = zmq.Context()
s = context.socket(zmq.PUB)        # create a publisher socket
p = "tcp://" + HOST + ":" + PORT  # how and where to communicate
s.bind(p)                          # bind socket to the address

while True:
    time.sleep(5)                   # wait every 5 seconds
    # Publish TIME
    msg_time = str.encode("TIME " + time.asctime())
    s.send(msg_time)
    # Publish Weather
    weather_status = "Sunny in Goiânia, Goiás, Brazil"
    msg_weather = str.encode(f"Weather {weather_status}")
    s.send(msg_weather)
    # Publish humidity
    humidity_value = "65% in Goiânia, Goiás, Brazil"
    msg_humidity = str.encode(f"humidity {humidity_value}")
    s.send(msg_humidity)
