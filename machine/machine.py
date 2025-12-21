import time
import random
import json
import paho.mqtt.client as mqtt

BROKER = "localhost"
PORT = 1883
TOPIC = "factory/machine1"

client = mqtt.Client()
client.connect(BROKER, PORT, 60)

print(" !! Máquina industrial iniciada...")

while True:
    data = {
        "temperature": round(random.uniform(60, 95), 2),
        "vibration": round(random.uniform(0.2, 1.5), 2),
        "status": "ON"
    }

    client.publish(TOPIC, json.dumps(data))
    print(" !! Enviado:", data)

    time.sleep(5)
