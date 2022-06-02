from Configurations import TSS_Device_Id, TSS_Start_Address, TSS_Register_Counts, Modbus_Error_Message, Connection_Error_Message
from Common_Functions import Gateway_Connect, Parse_Raw_Data


def TSS_Reading():
    """
    TSS Reading
    """
    Connection_Checking_Count = 0
    while True:
        TSS_Reading = Gateway_Connect().read_holding_registers(count=TSS_Register_Counts,
                                                               address=TSS_Start_Address, unit=TSS_Device_Id)
        TSS_Reading_check = str(TSS_Reading)
        if TSS_Reading_check != Modbus_Error_Message:
            tss_data = Parse_Raw_Data(
                TSS_Reading.registers, 0, 1)
            return {"TSS_Device_Id": TSS_Device_Id, "TSS_Data": tss_data}
        else:
            print(TSS_Reading_check)
            Connection_Checking_Count = Connection_Checking_Count+1
            if Connection_Checking_Count == 10:
                return Connection_Error_Message
