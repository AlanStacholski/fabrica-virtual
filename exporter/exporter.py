import json
from paho.mqtt.client import Client
from prometheus_client import start_http_server, Gauge

# Métricas Prometheus
temperature = Gauge('machine_temperature_celsius', 'Temperatura da máquina')
vibration = Gauge('machine_vibration_level', 'Vibração da máquina')

BROKER = "localhost"
TOPIC = "factory/machine1"

def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())
    temperature.set(data["temperature"])
    vibration.set(data["vibration"])
    print("📊 Métricas atualizadas:", data)

client = Client()
client.on_message = on_message
client.connect(BROKER, 1883, 60)
client.subscribe(TOPIC)

# Servidor Prometheus
start_http_server(8000)
print("📡 Exporter rodando em http://localhost:8000/metrics")

client.loop_forever()
