from Common_Functions import Gateway_Connect
from Configurations import Modbus_Error_Message, Modbus_Error, Power_Error_Message, Power_Error, Ethernet_Network_Error
from Configurations import Energymeter_Register_Counts, Energymeter_Start_Address, Energymeter_Device_Id


def Energymeter_Reading():
    """
    Energymeter Reading
    """
    Connection_Checking_Count = 0
    try:
        while True:
            Energymeter_Reading = Gateway_Connect().read_holding_registers(count=Energymeter_Register_Counts,
                                                                           address=Energymeter_Start_Address, unit=Energymeter_Device_Id)
            Energymeter_Reading_check = str(Energymeter_Reading)
            if Energymeter_Reading_check == Modbus_Error_Message:
                Connection_Checking_Count = Connection_Checking_Count+1
                if Connection_Checking_Count == 10:
                    return Modbus_Error

            elif Energymeter_Reading_check == Power_Error_Message:
                return Power_Error

            else:
                energymeter_data = Parse_Raw_Data_Energymeter(
                    Energymeter_Reading.registers)
                return energymeter_data
    except Exception as e:
        return Ethernet_Network_Error


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
