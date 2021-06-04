import paho.mqtt.client as mqtt
import time

# on_log callback
def on_log(client, userdata,level,buf):
    print('log:' +buf)

# Create New MQTT Client
client1 = mqtt.Client('mqtt_client1')

client1.on_log = on_log

# Connecting w/ Broker
client1.connect('192.168.0.6',1883)

client1.loop_start()

try:
    # Subscribe test/+
    client1.subscribe('test/+')
    
    while True:
        # Publish topic message test/client1 in 5 seconds term
        client1.publish('test/client1','Hello, MQTT') # Publishing its Topic Filter
        time.sleep(5)
except KeyboardInterrupt:
    print("Terminating Client...")

finally:
    client1.loop_stop() # End Callback
    client1.disconnect() # Disconnect with Broker
    