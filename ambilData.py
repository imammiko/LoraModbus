
from time import sleep
from SX127x.LoRa import *
from SX127x.board_config import BOARD

BOARD.setup()

class LoRaRcvCont(LoRa):
    def __init__(self, verbose=False):
        super(LoRaRcvCont, self).__init__(verbose)
        self.set_mode(MODE.SLEEP)
        self.set_dio_mapping([0] * 6)
        self.hasil=""

    def getPay(self):
        bytes(payload).decode("utf-8",'ignore')
    
    def start(self):
        self.reset_ptr_rx()
        self.set_mode(MODE.RXCONT)
        while True:
            sleep(.5)
            rssi_value = self.get_rssi_value()
            status = self.get_modem_status()
            sys.stdout.flush()
            #print("cc")
            
            #print(self.getter())
            #print(self.setter(value=""))
    
            

    def on_rx_done(self):
        #print("\nReceived: ")
        self.clear_irq_flags(RxDone=1)
        payload = self.read_payload(nocheck=True)
        #print(bytes(payload).decode("utf-8",'ignore'))
        hasilRc=bytes(payload).decode("utf-8",'ignore')
        self.setter(hasilRc)
        self.set_mode(MODE.SLEEP)
        self.reset_ptr_rx()
        self.set_mode(MODE.RXCONT)
        #return bytes(payload).decode("utf-8",'ignore')
        #self.getPay()
#awal program
    def initialStart(self):
        self.reset_ptr_rx()
        self.set_mode(MODE.RXCONT)
#dimasukan dalam while
    def pengulanganFungsi(self):
        sleep(.5)
        rssi_value = self.get_rssi_value()
        status = self.get_modem_status()
        sys.stdout.flush()
        #print("cc")
            
        #print(self.getter())
        #print(self.setter(value=""))
#data dapat diambil
    def hasil(self):
        self.dataHasil=self.getter()
        self.setter(value="")
        return self.dataHasil
        
    def setter(self,value):
        self.hasil=value
    def getter(self):
        return self.hasil

"""
lora = LoRaRcvCont(verbose=False)
lora.set_mode(MODE.STDBY)


lora.set_pa_config(pa_select=1)

try:
    #lora.start()
    lora = LoRaRcvCont(verbose=False)
    lora.set_mode(MODE.STDBY)
    lora.set_pa_config(pa_select=1)
    lora.initialStart()
    while True:
        lora.pengulanganFungsi()
        print(lora.getter())
        lora.setter(value="")

except KeyboardInterrupt:
    sys.stdout.flush()
    print("")
    sys.stderr.write("KeyboardInterrupt\n")
finally:
    sys.stdout.flush()
    print("")
    lora.set_mode(MODE.SLEEP)
    BOARD.teardown()
"""
