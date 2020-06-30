import ambilData as lrx
from pemisahCode import PemisahData
from time import sleep
from SX127x.LoRa import *
from SX127x.board_config import BOARD


lora=lrx.LoRaRcvCont(verbose=False)
pemisah=PemisahData("slave1")
lora.set_mode(MODE.STDBY)
lora.set_pa_config(pa_select=1)
lora.initialStart()
while True:
    lora.pengulanganFungsi()
    dataLoraRx=lora.getter()
    #print((dataLoraRX))
    lora.setter(value="")
    dicPemisah=pemisah.pisahKata(dataLoraRx)
    print(dicPemisah)
    
    


