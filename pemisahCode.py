
class PemisahData:
    def __init__(self,codeAwal):
        self.dataSensorArduino = {
        "temperature": 0 ,
        "humadity": 0,
        "mq": 0,
        "latitude":0,
        "longititude":0,
        "id":0
        }
        self.code=codeAwal
    
    def pisahKata(self,arduinoDataMasuk):

        arduinoData = arduinoDataMasuk
        startString=0
        endString=0
        stepString=""
        nampungKalimat=""


        if(arduinoData.rfind("slave1")==0):
        #print(arduinoData)
            if (arduinoData.rfind('/t')>0):
                #print (arduinoData.rfind('/t:'))
                startString=arduinoData.rfind('/t:')
                for x in arduinoData[startString+len("/t:"):]:
                    if (x=="/"):
                        break
                    nampungKalimat+=x
                
                self.dataSensorArduino["temperature"]=float(nampungKalimat)
                
            nampungKalimat=""

            if (arduinoData.rfind('/h')>0):
                #print (arduinoData.rfind('/h:'))
                startString=arduinoData.rfind('/h:')
                for x in arduinoData[startString+len("/h:"):]:
                    if (x=="/"):
                        break
                    nampungKalimat+=x;
                
                self.dataSensorArduino["humadity"]=float(nampungKalimat)
                
                nampungKalimat=""

            if (arduinoData.rfind('/h')>0):
                #print (arduinoData.rfind('/h:'))
                startString=arduinoData.rfind('/h:')
                for x in arduinoData[startString+len("/h:"):]:
                    if (x=="/"):
                        break
                    nampungKalimat+=x;
                            
                self.dataSensorArduino["humadity"]=float(nampungKalimat)
                
                nampungKalimat=""


            if (arduinoData.rfind('/mq')>0):
                #print (arduinoData.rfind('/mq:'))
                startString=arduinoData.rfind('/mq:')
                for x in arduinoData[startString+len("/mq:"):]:
                    if (x=="/"):
                        break
                    nampungKalimat+=x;
                
                self.dataSensorArduino["mq"]=float(nampungKalimat)
                
                nampungKalimat=""

            if (arduinoData.rfind('/la')>0):
                #print (arduinoData.rfind('/mq:'))
                startString=arduinoData.rfind('/la:')
                for x in arduinoData[startString+len("/la:"):]:
                    if (x=="/"):
                        break
                    nampungKalimat+=x;
                
                self.dataSensorArduino["latitude"]=float(nampungKalimat)
                
                nampungKalimat=""

            if (arduinoData.rfind('/lo')>0):
                #print (arduinoData.rfind('/mq:'))
                startString=arduinoData.rfind('/lo:')
                for x in arduinoData[startString+len("/lo:"):]:
                    if (x=="/"):
                        break
                    nampungKalimat+=x;
                
                self.dataSensorArduino["longititude"]=float(nampungKalimat)
                
                nampungKalimat=""

            if (arduinoData.rfind('/id')>0):
                #print (arduinoData.rfind('/mq:'))
                startString=arduinoData.rfind('/id:')
                for x in arduinoData[startString+len("/id:"):]:
                    if (x=="/"):
                        break
                    nampungKalimat+=x;
                
                self.dataSensorArduino["id"]=int(nampungKalimat)
                
                nampungKalimat=""
                

        return self.dataSensorArduino
        

