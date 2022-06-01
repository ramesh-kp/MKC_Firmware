import random


def Water_Level_Reading():
    Water_Level_Reading = {
        "Water_Level_Slave_Id": 150, "Water_Level_Reading": random.randint(150, 200)}
    return Water_Level_Reading


def Flowmeter_Reading():
    Flowmeter_Reading = {"Flowmeter_Slave_Id": 90,
                         "Flowmeter_Reading": random.randint(50, 100)}
    return Flowmeter_Reading
