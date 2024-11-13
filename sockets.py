import socketio
sio = socketio.Client()

@sio.event
def connect():
    print("Connected to the server.")
    sio.emit('PingTest', 'Hello from the Python client!')

#"Obstacles":[{"x":0, "y":0, "tipo":1},{"x":0, "y":10, "tipo":1}]}'
@sio.on('status')
def response(data):
    coordinates = tuple(data.items())
    print("Response from the server:", data)

# Connect to the Socket.IO server
#Change IP to connect while we dont have a domain
sio.connect("http://10.72.59.25:3000")


try:
    sio.wait()
except KeyboardInterrupt:
    print("Disconnecting...")
    sio.disconnect()
