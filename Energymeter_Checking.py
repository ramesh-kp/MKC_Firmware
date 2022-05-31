# import time

from Common_Functions import Gateway_Connect
from Configurations import Energymeter_Register_Counts, Energymeter_Start_Address, Energymeter_Device_Id, Modbus_Error_Message, Connection_Error_Message


def Energymeter_Reading():
    """
    Energymeter Reading
    """
    Connection_Checking_Count = 0
    while True:
        Energymeter_Reading = Gateway_Connect().read_holding_registers(count=Energymeter_Register_Counts,
                                                                       address=Energymeter_Start_Address, unit=Energymeter_Device_Id)
        # time.sleep(2)
        Energymeter_Reading_check = str(Energymeter_Reading)
        if Energymeter_Reading_check != Modbus_Error_Message:
            raw_data = Energymeter_Reading.registers
            return raw_data
        else:
            print(Energymeter_Reading_check)
            Connection_Checking_Count = Connection_Checking_Count+1
            if Connection_Checking_Count == 10:
                return Connection_Error_Message


def Parse_Raw_Data_Energymeter(Energymeter_Reading_Raw):
    Slave_Id = Energymeter_Reading_Raw[1]
    Ckwh = Energymeter_Reading_Raw[5]/1000
    Ckah = Energymeter_Reading_Raw[7]/1000
    Voltage = Energymeter_Reading_Raw[9]/10
    Power_Factor_Line_1 = Energymeter_Reading_Raw[33]/100
    Power_Factor_Line_2 = Energymeter_Reading_Raw[35]/100
    Power_Factor_Line_3 = Energymeter_Reading_Raw[37]/100
    Total_Power_Factor = Energymeter_Reading_Raw[43]/100
    Frequency = Energymeter_Reading_Raw[45]/10
    Energymeter_Data = {"Energymeter_Slave_ID": Slave_Id, "Energymeter_Ckwh": Ckwh, "Energymeter_Ckah": Ckah, "Energymeter_Voltage": Voltage, "Energymeter_Power_Factor_Line_1": Power_Factor_Line_1,
                        "Energymeter_Power_Factor_Line_2": Power_Factor_Line_2, "Energymeter_Power_Factor_Line_3": Power_Factor_Line_3, "Energymeter_Total_Power_Factor": Total_Power_Factor, "Energymeter_Frequency": Frequency}
    return Energymeter_Data
