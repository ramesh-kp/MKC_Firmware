from Configurations import TDS_Device_Id, TDS_Start_Address, TDS_Register_Counts
from Configurations import Modbus_Error_Message, Modbus_Error, Power_Error_Message, Power_Error, Ethernet_Network_Error
from Common_Functions import Gateway_Connect, Parse_Raw_Data


def TDS_Reading():
    """
    TDS Reading
    """
    Connection_Checking_Count = 0
    try:
        while True:
            TDS_Reading = Gateway_Connect().read_holding_registers(count=TDS_Register_Counts,
                                                                   address=TDS_Start_Address, unit=TDS_Device_Id)
            TDS_Reading_check = str(TDS_Reading)
            if TDS_Reading_check == Modbus_Error_Message:
                Connection_Checking_Count = Connection_Checking_Count+1
                if Connection_Checking_Count == 10:
                    return Modbus_Error

            elif TDS_Reading_check == Power_Error_Message:
                return Power_Error

            else:
                tds_data = Parse_Raw_Data(TDS_Reading.registers, 2, 3)
                return {"TDS_Device_Id": TDS_Device_Id, "TDS_Data": tds_data}
    except Exception as e:
        return Ethernet_Network_Error
