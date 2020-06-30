import ambilData as lrx
from time import sleep
from SX127x.LoRa import *
from SX127x.board_config import BOARD


lora=lrx.LoRaRcvCont(verbose=False)
lora.set_mode(MODE.STDBY)
lora.set_pa_config(pa_select=1)
lora.initialStart()
while True:
    lora.pengulanganFungsi()
    dataLoraRX=lora.getter()
    print(type(dataLoraRX))
    lora.setter(value="")

