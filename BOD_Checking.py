from Configurations import BOD_Device_Id, BOD_Start_Address, BOD_Register_Counts, Modbus_Error_Message, Connection_Error_Message
from Common_Functions import Gateway_Connect, Parse_Raw_Data


def BOD_Reading():
    """
    BOD Reading
    """
    Connection_Checking_Count = 0
    while True:
        BOD_Reading = Gateway_Connect().read_holding_registers(count=BOD_Register_Counts,
                                                               address=BOD_Start_Address, unit=BOD_Device_Id)
        BOD_Reading_check = str(BOD_Reading)
        if BOD_Reading_check != Modbus_Error_Message:
            bod_data = Parse_Raw_Data(BOD_Reading.registers, 4, 5)
            return {"BOD_Device_Id": BOD_Device_Id, "BOD_Data": bod_data}
        else:
            print(BOD_Reading_check)
            Connection_Checking_Count = Connection_Checking_Count+1
            if Connection_Checking_Count == 10:
                return Connection_Error_Message
