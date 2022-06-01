from Configurations import Pressure_Device_Id, Pressure_Start_Address, Pressure_Register_Counts, Modbus_Error_Message, Connection_Error_Message
from Common_Functions import Gateway_Connect, Parse_Raw_Data


def Pressure_Reading():
    """
    Pressure Reading
    """
    Connection_Checking_Count = 0
    while True:
        Pressure_Reading = Gateway_Connect().read_holding_registers(count=Pressure_Register_Counts,
                                                                    address=Pressure_Start_Address, unit=Pressure_Device_Id)
        Pressure_Reading_check = str(Pressure_Reading)
        if Pressure_Reading_check != Modbus_Error_Message:
            pressure_data = Parse_Raw_Data(Pressure_Reading.registers, 0, 1)
            return {"Pressure_Device_Id": Pressure_Device_Id, "Pressure_Data": pressure_data}
        else:
            print(Pressure_Reading_check)
            Connection_Checking_Count = Connection_Checking_Count+1
            if Connection_Checking_Count == 10:
                return Connection_Error_Message
