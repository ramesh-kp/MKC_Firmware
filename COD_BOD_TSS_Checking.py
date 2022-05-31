# import time
import struct

from Common_Functions import Gateway_Connect, Little_To_Big_Endian
from Configurations import COD_BOD_TSS_Register_Counts, COD_BOD_TSS_Start_Address, COD_BOD_TSS_Device_Id, Modbus_Error_Message, Connection_Error_Message


def COD_BOD_TSS_Reading():
    """
    COD, BOD and TSS Reading
    """
    Connection_Checking_Count = 0
    while True:
        COD_BOD_TSS_Reading = Gateway_Connect().read_holding_registers(count=COD_BOD_TSS_Register_Counts,
                                                                       address=COD_BOD_TSS_Start_Address, unit=COD_BOD_TSS_Device_Id)
        # time.sleep(2)
        COD_BOD_TSS_Reading_check = str(COD_BOD_TSS_Reading)
        if COD_BOD_TSS_Reading_check != Modbus_Error_Message:
            raw_data = COD_BOD_TSS_Reading.registers
            return raw_data
        else:
            print(COD_BOD_TSS_Reading_check)
            Connection_Checking_Count = Connection_Checking_Count+1
            if Connection_Checking_Count == 10:
                return Connection_Error_Message


def Parse_Raw_Data_COD_BOD_TSS(COD_BOD_TSS_Reading_Raw):
    List_1 = hex(COD_BOD_TSS_Reading_Raw[0]).replace('0x', '').zfill(4)
    List_2 = hex(COD_BOD_TSS_Reading_Raw[1]).replace('0x', '').zfill(4)
    List_3 = hex(COD_BOD_TSS_Reading_Raw[2]).replace('0x', '').zfill(4)
    List_4 = hex(COD_BOD_TSS_Reading_Raw[3]).replace('0x', '').zfill(4)
    List_5 = hex(COD_BOD_TSS_Reading_Raw[4]).replace('0x', '').zfill(4)
    List_6 = hex(COD_BOD_TSS_Reading_Raw[5]).replace('0x', '').zfill(4)
    First_Post_Hex = Little_To_Big_Endian(List_1 + List_2)
    Second_Post_Hex = Little_To_Big_Endian(List_3 + List_4)
    Third_Post_Hex = Little_To_Big_Endian(List_5 + List_6)
    Temperature = round(struct.unpack(
        '!f', bytes.fromhex(First_Post_Hex))[0], 2)
    COD = round(struct.unpack(
        '!f', bytes.fromhex(Second_Post_Hex))[0], 2)
    BOD = round(struct.unpack(
        '!f', bytes.fromhex(Third_Post_Hex))[0], 2)
    COD_BOD_Temperature_Data = {"COD": COD,
                                "BOD": BOD, "Temperature": Temperature}
    return COD_BOD_Temperature_Data
