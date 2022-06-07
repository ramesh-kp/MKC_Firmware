from Configurations import TSS_Device_Id, TSS_Start_Address, TSS_Register_Counts
from Configurations import Modbus_Error_Message, Modbus_Error, Power_Error_Message, Power_Error, Ethernet_Network_Error
from Common_Functions import Gateway_Connect, Parse_Raw_Data


def TSS_Reading():
    """
    TSS Reading
    """
    Connection_Checking_Count = 0
    try:
        while True:
            TSS_Reading = Gateway_Connect().read_holding_registers(count=TSS_Register_Counts,
                                                                   address=TSS_Start_Address, unit=TSS_Device_Id)
            TSS_Reading_check = str(TSS_Reading)
            if TSS_Reading_check == Modbus_Error_Message:
                Connection_Checking_Count = Connection_Checking_Count+1
                if Connection_Checking_Count == 10:
                    return Modbus_Error

            elif TSS_Reading_check == Power_Error_Message:
                return Power_Error

            else:
                tss_data = Parse_Raw_Data(TSS_Reading.registers, 0, 1)
                return {"TSS_Device_Id": TSS_Device_Id, "TSS_Data": tss_data}
    except Exception as e:
        return Ethernet_Network_Error
