import opcua
from time import sleep


s = opcua.Server()
s.set_server_name("OpcUa Test Server")
s.set_endpoint("opc.tcp://127.0.0.1:4841")

idx = s.register_namespace("http://127.0.0.1:4841")
s.start()

objects = s.get_objects_node()
ruuvitag = objects.add_object(idx, "Station")
temperature = ruuvitag.add_variable(idx, "Temperature", 0)
temperature.set_writable(writable=True)
prevtemp = 0
while True:
    temp = temperature.get_value()
    if temp != prevtemp:
        print(temperature.get_value())

    prevtemp = temp
