import paho.mqtt.client as paho
import time
import json
def on_publish(client, userdata, mid):
    print("mid: "+str(mid))
 
client = paho.Client()
client.on_publish = on_publish
client.connect("mqtt.antares.id", 1883)
client.loop_start()
dictqtt= {
  "m2m:rqp": {
    "fr": "cebbd486fada948b:96f9cf4e193d79f6",
    "to": "/antares-cse/antares-id/testKawanBerli/ch1",
    "op": 1,
    "rqi": 123456,
    "pc": {
      "m2m:cin": {
        "cnf": "message",
        "con": "{\"your-first-data\":the-integer-value,\"your-second-data\":\"the-string-data\"}"
      }
    },
    "ty": 4
  }}
toJsony = json.dumps(dictqtt)
while True:
    #temperature = read_from_imaginary_thermometer()
    (rc, mid) = client.publish("/oneM2M/req/cebbd486fada948b:96f9cf4e193d79f6/antares-cse/json", toJsony, qos=1)
    time.sleep(30)
