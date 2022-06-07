from Configurations import COD_Device_Id, COD_Start_Address, COD_Register_Counts
from Configurations import Modbus_Error_Message, Modbus_Error, Power_Error_Message, Power_Error, Ethernet_Network_Error
from Common_Functions import Gateway_Connect, Parse_Raw_Data


def COD_Reading():
    """
    COD Reading
    """
    Connection_Checking_Count = 0
    try:
        while True:
            COD_Reading = Gateway_Connect().read_holding_registers(count=COD_Register_Counts,
                                                                   address=COD_Start_Address, unit=COD_Device_Id)
            COD_Reading_check = str(COD_Reading)
            if COD_Reading_check == Modbus_Error_Message:
                Connection_Checking_Count = Connection_Checking_Count+1
                if Connection_Checking_Count == 10:
                    return Modbus_Error

            elif COD_Reading_check == Power_Error_Message:
                return Power_Error

            else:
                cod_data = Parse_Raw_Data(COD_Reading.registers, 2, 3)
                return {"COD_Device_Id": COD_Device_Id, "COD_Data": cod_data}
    except Exception as e:
        return Ethernet_Network_Error
