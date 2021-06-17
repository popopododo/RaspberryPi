import paho.mqtt.client as mqtt
import time
import bmpsensor

broker = '192.168.0.6'
websocket_port = 9001

def on_log(client, userdata,level,buf):
    print('log[' +str(level)+']',buf)
    
client1=mqtt.Client('websocket_client',transport='websockets')
client1.on_log=on_log

print('Connecting to Broker',broker,'on port',websocket_port)
client1.connect(broker,websocket_port)
client1.loop_start()

try:
    client1.subscribe('test/+')
    while True:
        temp,pressure,altitude=bmpsensor.readBmp180()
        client1.publish('/test/client1temp',temp)
        time.sleep(10)
        
except KeyboardInterrupt:
    print("Exit...")

finally:
    client1.loop_stop()
    client1.disconnect()
    