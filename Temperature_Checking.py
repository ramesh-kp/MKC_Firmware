from Configurations import Temperature_Device_Id, Temperature_Start_Address, Temperature_Register_Counts, Modbus_Error_Message, Connection_Error_Message
from Common_Functions import Gateway_Connect, Parse_Raw_Data


def Temperature_Reading():
    """
    Temperature Reading
    """
    Connection_Checking_Count = 0
    while True:
        Temperature_Reading = Gateway_Connect().read_holding_registers(count=Temperature_Register_Counts,
                                                                       address=Temperature_Start_Address, unit=Temperature_Device_Id)
        Temperature_Reading_check = str(Temperature_Reading)
        if Temperature_Reading_check != Modbus_Error_Message:
            temperature_data = Parse_Raw_Data(
                Temperature_Reading.registers, 0, 1)
            return {"Temperature_Device_Id": Temperature_Device_Id, "Temperature_Data": temperature_data}
        else:
            print(Temperature_Reading_check)
            Connection_Checking_Count = Connection_Checking_Count+1
            if Connection_Checking_Count == 10:
                return Connection_Error_Message
