from pymodbus.client.sync import ModbusTcpClient
from datetime import datetime
import pytz
import logging

from Configurations import Gateway_Ip_Address
from Configurations import Gateway_Port
from Configurations import Log_File

# Gateway Configuretion


def Gateway_Connect():
    gateway_client = ModbusTcpClient(Gateway_Ip_Address, Gateway_Port)
    gateway_client.connect()
    # time.sleep(2)
    return gateway_client

# Local Time Configuration


def Local_Time():
    IST = pytz.timezone('Asia/Kolkata')
    datetime_ist = datetime.now(IST).strftime('%Y:%m:%d %H:%M:%S %Z %z')
    return datetime_ist

# Littke Endian to Big Endian


def Little_To_Big_Endian(data):
    t = bytearray.fromhex(data)
    t.reverse()
    return ''.join(format(x, '02x') for x in t).upper()


# Write Log to Files


def Log_File_Messages(data):
    logging.basicConfig(filename=Log_File, filemode='a',
                        format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s', datefmt='%H:%M:%S',  level=logging.DEBUG)
    logging.info(data)
