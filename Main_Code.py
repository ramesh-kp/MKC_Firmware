from Energymeter_Checking import Energymeter_Reading
from COD_Checking import COD_Reading
from BOD_Checking import BOD_Reading
from Temperature_Checking import Temperature_Reading
from TSS_Checking import TSS_Reading
from Ph_Checking import Ph_Reading
from Pressure_Checking import Pressure_Reading
from Simulated_Datas import Water_Level_Reading, Flowmeter_Reading
from Common_Functions import Log_File_Messages, Local_Time

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

    print("<<< Pressure Reading >>>")
    pressure = Pressure_Reading()
    print(pressure)

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
    sensor_data = str(time | energymeter | cod |
                      bod | temperature | tss | ph | pressure | water_level | flowmeter)
    print(sensor_data)
    # # Iothub_Client_Telemetry_Sample_Run(sensor_data)
    Log_File_Messages(sensor_data)
