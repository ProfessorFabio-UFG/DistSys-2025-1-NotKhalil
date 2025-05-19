import zmq
from constPS import *  #-

context = zmq.Context()
s = context.socket(zmq.SUB)          # create a subscriber socket
p = "tcp://" + HOST + ":" + PORT     # how and where to communicate
s.connect(p)                         # connect to the server
# Subscribe to all topics
s.setsockopt_string(zmq.SUBSCRIBE, "TIME")
s.setsockopt_string(zmq.SUBSCRIBE, "Weather")
s.setsockopt_string(zmq.SUBSCRIBE, "humidity")

for _ in range(5):  # Five iterations
    message = s.recv()               # receive a message
    print(bytes.decode(message))
