import RPi.GPIO as GPIO
import time
import sys
import Adafruit_DHT
import paho.mqtt.client as mqtt
import uuid
import http.client, urllib

conn = http.client.HTTPSConnection("pushsafer.com:443")

#print(response.status, response.reason)
#data = response.read()
#print(data)

client = mqtt.Client(str(uuid.uuid1()))
client.tls_set()
client.username_pw_set('idd', 'device@theFarm')

client.connect(
    'farlab.infosci.cornell.edu',
    port=8883)

topic_soil = 'IDD/Garden/Soil/Moisture'
topic_hum = 'IDD/Garden/Environment/Humidity'
topic_temp = 'IDD/Garden/Environment/Temperature'

temp_low = 5
temp_high = 30

channel = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

def callback(channel):
    if GPIO.input(channel):
        print("Garden soil moisture level sufficient")
    else:
        print("Soil needs watering")
        client.publish(topic_soil, "Be sure to water the garden!")
        conn.request("POST", "/api",
          urllib.parse.urlencode({
            "k": "Z0QkLsSdJhDgvu4cxd2X",                # Your Private or Alias Key
            "m": "Garden soil moisture too low",                   # Message Text
            "t": "Pi The Gardener",                     # Title of message
            "i": "<2>",                      # Icon number 1-98
            "s": "<2>",                     # Sound number 0-28
            "v": "<2>",                 # Vibration number 0-3
            #"p": "<PICTURE>",                   # Picture Data URL with Base64-encoded string
          }), { "Content-type": "application/x-www-form-urlencoded" })
        response = conn.getresponse()
        
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime = 300)
GPIO.add_event_callback(channel, callback)

while True:
    time.sleep(1)
    humidity, temperature = Adafruit_DHT.read_retry(11, 4)
    print('Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity))
    if temperature > temp_high or temperature < temp_low:
        print('Temperature out of set range! Might be harmful for plants.')
        client.publish(topic_temp, "Temperature out of range!")
        conn.request("POST", "/api",
          urllib.parse.urlencode({
            "k": "Z0QkLsSdJhDgvu4cxd2X",                # Your Private or Alias Key
            "m": "Garden temperature out of range",                   # Message Text
            "t": "Pi The Gardener",                     # Title of message
            "i": "<2>",                      # Icon number 1-98
            "s": "<2>",                     # Sound number 0-28
            "v": "<2>",                 # Vibration number 0-3
            #"p": "<PICTURE>",                   # Picture Data URL with Base64-encoded string
          }), { "Content-type": "application/x-www-form-urlencoded" })
        response = conn.getresponse()