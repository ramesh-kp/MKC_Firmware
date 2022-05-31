# Made an Assumption
# import time
import struct

from Common_Functions import Gateway_Connect
from Configurations import Turbidity_Register_Counts, Turbidity_Start_Address, Turbidity_Device_Id, Modbus_Error_Message, Connection_Error_Message


def Turbidity_Reading():
    """
    Turbidity Reading
    """
    Connection_Checking_Count = 0
    while True:
        Turbidity_Reading = Gateway_Connect().read_holding_registers(count=Turbidity_Register_Counts,
                                                                     address=Turbidity_Start_Address, unit=Turbidity_Device_Id)
        # time.sleep(2)
        Turbidity_Reading_check = str(Turbidity_Reading)
        if Turbidity_Reading_check != Modbus_Error_Message:
            raw_data = Turbidity_Reading.registers
            return raw_data
        else:
            print(Turbidity_Reading_check)
            Connection_Checking_Count = Connection_Checking_Count+1
            if Connection_Checking_Count == 10:
                return Connection_Error_Message


def little(string):
    t = bytearray.fromhex(string)
    t.reverse()
    return ''.join(format(x, '02x') for x in t).upper()


def Parse_Raw_Data_Turbidity(Turbidity_Reading_Raw):
    List_1 = hex(Turbidity_Reading_Raw[0]).replace('0x', '').zfill(4)
    List_2 = hex(Turbidity_Reading_Raw[1]).replace('0x', '').zfill(4)
    First_Post_Hex = little(List_1 + List_2)
    Turbidity = round(struct.unpack(
        '!f', bytes.fromhex(First_Post_Hex))[0], 2)
    Turbidity_Data = {"Turbidity": Turbidity}
    return Turbidity_Data
