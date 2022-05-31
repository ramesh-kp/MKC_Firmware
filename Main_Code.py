# import time

from Energymeter_Checking import Energymeter_Reading, Parse_Raw_Data_Energymeter
from COD_BOD_TSS_Checking import COD_BOD_TSS_Reading, Parse_Raw_Data_COD_BOD_TSS
from Turbidity_Checking import Turbidity_Reading, Parse_Raw_Data_Turbidity
from Ph_Pressure_Checking import Ph_Reading, Parse_Raw_Data_Ph
from Iot_Connection import Iothub_Client_Telemetry_Sample_Run
from Common_Functions import Local_Time, Log_File_Messages

if __name__ == '__main__':
    print("<<< Waste Water Management >>>")

#    while True:

    print("<<< Energymeter Reading >>>")
    energymeter = Parse_Raw_Data_Energymeter(Energymeter_Reading())

    print("<<< COD, BOD and TSS Reading >>>")
    cod_bod_tss = Parse_Raw_Data_COD_BOD_TSS(COD_BOD_TSS_Reading())

    print("<<< Turbidity Reading >>>")
    turbidity = Parse_Raw_Data_Turbidity(Turbidity_Reading())

    print("<<< Ph and Pressure Reading >>>")
    ph_pressure = Parse_Raw_Data_Ph(Ph_Reading())

    time = {"Time": Local_Time()}

    sensor_data = str(time | energymeter | cod_bod_tss |
                      turbidity | ph_pressure)
    Iothub_Client_Telemetry_Sample_Run(sensor_data)
    Log_File_Messages(sensor_data)
