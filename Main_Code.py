from Energymeter_Checking import Energymeter_Reading
from COD_Checking import COD_Reading
from BOD_Checking import BOD_Reading
from Temperature_Checking import Temperature_Reading
from TSS_Checking import TSS_Reading
from Ph_Checking import Ph_Reading
from TDS_Checking import TDS_Reading
from Simulated_Datas import Water_Level_Reading, Flowmeter_Reading
from Common_Functions import Log_File_Messages, Local_Time
from Iot_Connection import Iothub_Client_Telemetry_Sample_Run
from Configurations import Device_Id, Variable_Header, Command_Type

if __name__ == '__main__':
    print("<<< Waste Water Management >>>")

#    while True:

    print("<<< Energymeter Reading >>>")
    energymeter = Energymeter_Reading()
    print(energymeter)

    print("<<< COD Reading >>>")
    cod = COD_Reading()
    print(cod)

    print("<<< BOD Reading >>>")
    bod = BOD_Reading()
    print(bod)

    print("<<< Temperature Reading >>>")
    temperature = Temperature_Reading()
    print(temperature)

    print("<<< TSS Reading >>>")
    tss = TSS_Reading()
    print(tss)

    print("<<< Ph Reading >>>")
    ph = Ph_Reading()
    print(ph)

    print("<<< TDS Reading >>>")
    tds = TDS_Reading()
    print(tds)

    print("<<< Water Level Reading >>>")
    water_level = Water_Level_Reading()
    print(water_level)

    print("<<< Flowmeter Reading >>>")
    flowmeter = Flowmeter_Reading()
    print(flowmeter)

    print("<<< Local Time >>>")
    time = {"Time": Local_Time()}
    print(time)

    print("<<< Complete Sensor Datas >>>")
    sensor_data = str(Device_Id | time | energymeter | cod |
                      bod | temperature | tss | ph | tds | water_level | flowmeter)
    MQTT_Message = Variable_Header + \
        format(len(sensor_data), "04x") + sensor_data
    Total_Length = format(len(MQTT_Message), "04x")
    real_data = Command_Type + Total_Length + MQTT_Message

    Iothub_Client_Telemetry_Sample_Run(real_data)
    Log_File_Messages(real_data)
