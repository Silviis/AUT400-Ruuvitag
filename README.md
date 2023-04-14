# AUT400-Ruuvitag

Major part of the program is implemented in Node-RED (use with node version >= 15). Only the mock RuuviTag TCP socket client & the mock OPC UA server are implemented in small python scripts.

## Installing dependencies

[node-red-dashboard](https://flows.nodered.org/node/node-red-dashboard) and [node-red-contrib-opcua](https://flows.nodered.org/node/node-red-contrib-opcua) has to be installed in order for this project to work properly. To install mentioned packages run:

```npm install node-red-contrib-opcua && npm install node-red-dashboard ```

Python3 is required to run the mock TCP client & OPC UA server. OPC UA server requires [OPC-UA library for python](https://python-opcua.readthedocs.io/en/latest/) which you can install by running:

```python3 -m pip install opcua```

## Running the project

Start Node-RED by issuing command: ```node-red```. Now you can view the Node-RED environment by going to http://127.0.0.1:1880/ . From there you can import the flows.json file and deploy it.

**Remember to toggle on the data sending in the UI**! (UI's address is http://127.0.0.1:1880/ui/)

Next start the ocpua mock server by running the opcua-server.py in another terminal by issuing command: 
```python3 opcua-server.py```

Then you can start the TCP socket client by running following command in another terminal:
```python3  ruuvitag_mock_tcp_server.py```.
In that terminal window you can start manually inputing mock values that normally would be gotten from the RuuviTag-sensor. If everything works correctly those same values should also be displayed in the terminal you launched the OPC UA (as they get sent through the node-red environment).
