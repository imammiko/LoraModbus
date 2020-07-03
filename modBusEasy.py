import time
import serial


class ModBusRTU:
    def __init__(self,addres,status,port):
        self.dictData= ""
        self.add=addres
        self.port=port
        self.status=status
        self.ser = serial.Serial(
        port=self.port,
        baudrate = 9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
        )

    def modSent(self,dictDatax):
        self.dictData=dictDatax
        data="{0}/t:{1}/h:{2}/mq:{3}/la:{4}/lo:{5}/id:{6}/\n"
        data=data.format(self.add, self.dictData["temperature"], self.dictData["humadity"],self.dictData["mq"],self.dictData["latitude"],self.dictData["longititude"],self.dictData["id"])
        print(self.dictData)
        self.ser.write(data.encode())
        time.sleep(0.05)
        
        
        

