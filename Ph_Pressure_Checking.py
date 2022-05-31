# Made an Assumption
# import time
import struct

from Common_Functions import Gateway_Connect
from Configurations import Ph_Register_Counts, Ph_Start_Address, Ph_Device_Id, Modbus_Error_Message, Connection_Error_Message


def Ph_Reading():
    """
    Ph Reading
    """
    Connection_Checking_Count = 0
    while True:
        Ph_Reading = Gateway_Connect().read_holding_registers(count=Ph_Register_Counts,
                                                              address=Ph_Start_Address, unit=Ph_Device_Id)
        # time.sleep(2)
        Ph_Reading_check = str(Ph_Reading)
        if Ph_Reading_check != Modbus_Error_Message:
            raw_data = Ph_Reading.registers
            return raw_data
        else:
            print(Ph_Reading_check)
            Connection_Checking_Count = Connection_Checking_Count+1
            if Connection_Checking_Count == 10:
                return Connection_Error_Message


def little(string):
    t = bytearray.fromhex(string)
    t.reverse()
    return ''.join(format(x, '02x') for x in t).upper()


def Parse_Raw_Data_Ph(Ph_Reading_Raw):
    List_1 = hex(Ph_Reading_Raw[0]).replace('0x', '').zfill(4)
    List_2 = hex(Ph_Reading_Raw[1]).replace('0x', '').zfill(4)
    List_3 = hex(Ph_Reading_Raw[2]).replace('0x', '').zfill(4)
    List_4 = hex(Ph_Reading_Raw[3]).replace('0x', '').zfill(4)
    First_Post_Hex = little(List_1 + List_2)
    Second_Post_Hex = little(List_3 + List_4)
    Pressure = round(struct.unpack(
        '!f', bytes.fromhex(First_Post_Hex))[0], 2)
    Ph_Data = round(struct.unpack(
        '!f', bytes.fromhex(Second_Post_Hex))[0], 2)
    Pressure_Ph_Data = {"Pressure": Pressure, "Ph Data": Ph_Data}
    return Pressure_Ph_Data
