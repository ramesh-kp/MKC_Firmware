from Configurations import Ph_Device_Id, Ph_Start_Address, Ph_Register_Counts
from Configurations import Modbus_Error_Message, Modbus_Error, Power_Error_Message, Power_Error, Ethernet_Network_Error
from Common_Functions import Gateway_Connect, Parse_Raw_Data


def Ph_Reading():
    """
    Ph Reading
    """
    Connection_Checking_Count = 0
    try:
        while True:
            Ph_Reading = Gateway_Connect().read_holding_registers(count=Ph_Register_Counts,
                                                                  address=Ph_Start_Address, unit=Ph_Device_Id)
            Ph_Reading_check = str(Ph_Reading)
            if Ph_Reading_check == Modbus_Error_Message:
                Connection_Checking_Count = Connection_Checking_Count+1
                if Connection_Checking_Count == 10:
                    return Modbus_Error

            elif Ph_Reading_check == Power_Error_Message:
                return Power_Error

            else:
                ph_data = Parse_Raw_Data(Ph_Reading.registers, 2, 3)
                return {"Ph_Device_Id": Ph_Device_Id, "Ph_Data": ph_data}
    except Exception as e:
        return Ethernet_Network_Error
