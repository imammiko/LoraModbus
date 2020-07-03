#!/usr/bin/env python
'''
Pymodbus Server With Callbacks
--------------------------------------------------------------------------
This is an example of adding callbacks to a running modbus server
when a value is written to it. In order for this to work, it needs
a device-mapping file.
'''
# ---------------------------------------------------------------------------#
# import the modbus libraries we need
# ---------------------------------------------------------------------------#
from pymodbus.server.asynchronous import StartTcpServer
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSparseDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
from pymodbus.transaction import ModbusRtuFramer, ModbusAsciiFramer

import psutil

# ---------------------------------------------------------------------------#
# import the python libraries we need
# ---------------------------------------------------------------------------#
from multiprocessing import Queue, Process

# ---------------------------------------------------------------------------#
# configure the service logging
# ---------------------------------------------------------------------------#
import logging

logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)


class Device(object):
    def __init__(self, path, devicetype, callback):
        self.path = path
        self.devicetype = devicetype
        self.callback = callback
        self.value = 0

    def update(self):
        self.value = self.callback(self.path)




# ---------------------------------------------------------------------------#
# create your custom data block with callbacks
# ---------------------------------------------------------------------------#
class CallbackDataBlock(ModbusSparseDataBlock):
    ''' A datablock that stores the new value in memory
    and passes the operation to a message queue for further
    processing.
    '''

    def __init__(self, devices):
        self.devices = devices
        self.devices[0xbeef] = len(self.devices)  # the number of devices
      
        # values = [k:0 ]
        self.values = {k: 0 for k in self.devices.iterkeys()}
        super(CallbackDataBlock, self).__init__(self.values)

   


# ---------------------------------------------------------------------------#
# initialize your device map
# ---------------------------------------------------------------------------#
def read_device_map():
    rootpath = '/sys/bus/w1/devices/'
    devices = {
        0x0001: Device(rootpath + '28-0116002c7fff', 'ds18b20', 1231)
        # 0x0001: Device(rootpath + '28-000004662b96', 'ds18b20', temperatureFromW1File)
        # 0x0002: Device(rootpath + '28-000004665b23', 'ds18b20', temperatureFromW1File),
        # 0x0003: Device(rootpath + '28-0116002edeff', 'ds18b20', temperatureFromW1File),
        # 0x0004: Device(rootpath + '28-0216001876ff', 'ds18b20', temperatureFromW1File),
        # 0x0005: Device(rootpath + '28-0216002d88ff', 'ds18b20', temperatureFromW1File),
        # 0x0006: Device(rootpath + '28-0216002fc6ff', 'ds18b20', temperatureFromW1File),
    }
    return devices


# ---------------------------------------------------------------------------#
# initialize your data store
# ---------------------------------------------------------------------------#
devices = read_device_map()

context = ModbusServerContext(slaves=store, single=True)

# ---------------------------------------------------------------------------#
# run the server you want
# ---------------------------------------------------------------------------#
StartTcpServer(context, address=("0.0.0.0", 5020))
