import paho.mqtt.client as paho
import time
import json



    
class MqttAntares:
    def __init__(self,kunciAkses,namaProjek,Device):
        self.kunci=str(kunciAkses)
        self.Projek=str(namaProjek)
        self.perangkat=str(Device)
        self.client = paho.Client()       
        self.client.connect("mqtt.antares.id", 1883)
        self.client.loop_start()
        
       
       
    def addMqtt(self,dictMqtt):
        dictMqttJson= json.dumps(dictMqtt)
        to="/antares-cse/antares-id/{}/{}"
        to=to.format( self.Projek, self.perangkat)
        topik="/oneM2M/req/{}/antares-cse/json"
        topik=topik.format( self.kunci)
        self.dictMqttSend= {
  "m2m:rqp": {
    "fr": self.kunci,
    "to": to,
    "op": 1,
    "rqi": 123456,
    "pc": {
      "m2m:cin": {
        "cnf": "message",
        "con": dictMqttJson
      }
    },
    "ty": 4
  }}
        self.mqttSend=json.dumps(self.dictMqttSend)
        self.client.publish(topik, self.mqttSend, qos=1)
        
        #time.sleep(30)
