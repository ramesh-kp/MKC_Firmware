from pymodbus.client.sync import ModbusTcpClient
from datetime import datetime
import pytz
import logging
import struct

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

# Convert Raw Data to Real Value


def Parse_Raw_Data(Raw_Data, Array_Pos_1, Array_Pos_2):
    List_1 = hex(Raw_Data[Array_Pos_1]).replace('0x', '').zfill(4)
    List_2 = hex(Raw_Data[Array_Pos_2]).replace('0x', '').zfill(4)
    First_Post_Hex = Little_To_Big_Endian(List_1 + List_2)
    Reading = round(struct.unpack('!f', bytes.fromhex(First_Post_Hex))[0], 2)
    return Reading


# Write Log to Files


def Log_File_Messages(data):
    logging.basicConfig(filename=Log_File, filemode='a',
                        format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s', datefmt='%H:%M:%S',  level=logging.DEBUG)
    logging.info(data)
