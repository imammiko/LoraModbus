import ambilData as lrx
from pemisahCode import PemisahData
from mqttAntarest import MqttAntares
from time import sleep
from SX127x.LoRa import *
from SX127x.board_config import BOARD


lora=lrx.LoRaRcvCont(verbose=False)
pemisah=PemisahData("slave1")
lora.set_mode(MODE.STDBY)
lora.set_pa_config(pa_select=1)
lora.initialStart()

#mqtt
mqttAnt=MqttAntares("cebbd486fada948b:96f9cf4e193d79f6","testKawanBerli","ch1")


while True:
    lora.pengulanganFungsi()
    dataLoraRx=lora.getter()
    #print((dataLoraRX))
    lora.setter(value="")
    dicPemisah=pemisah.pisahKata(dataLoraRx)
    mqttAnt.addMqtt(dicPemisah)
    print(dicPemisah)
    
    


