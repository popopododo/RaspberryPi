import paho.mqtt.client as mqtt
import time


broker= '192.168.0.6'
websocket_port = 9001

# Create Log Callbacks
def on_log(client, userdata,level,buf):
    print('log:' +buf)

# Create Websocket MQTT Client
client = mqtt.Client('websocket_client',transport='websockets')
client.on_log= on_log

print('Connecting to Broker ',broker, 'on port', websocket_port)
client.connect(broker,websocket_port)
client.loop_start()

try:
    # Subscribe test/+
    client.subscribe('test/+')
    
    for x in range(3):
        # Publish topic message test/+
        client.publish('test/websocket_client','Hello MQTT') 
        time.sleep(1)
        
except KeyboardInterrupt:
    print("Terminating Client...")

finally:
    client.loop_stop() # End Callback
    client.disconnect() # Disconnect with Broker