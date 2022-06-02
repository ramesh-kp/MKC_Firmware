# IoT Configurations
Iot_Connection_String = "HostName=mkc-iot-hub.azure-devices.net;DeviceId=sensors_001;SharedAccessKey=rEp4wNLKN/WybUfQLhLmiWmzcpga68RIGO2nTudNeYU="

# Gateway Configurations
Gateway_Ip_Address = "192.168.1.254"
Gateway_Port = 502

# Energymeter Sensor Configurations
Energymeter_Device_Id = 170
Energymeter_Start_Address = 1
Energymeter_Register_Counts = 46

# # Water Level Sensor Configurations
# Water_Level_Sensor_Device_Id = 1
# Water_Level_Sensor_Start_Address = 1
# Water_Level_Sensor_Register_Counts = 10

# # Flowmeter Sensor Configurations
# Flowmeter_Device_Id = 90
# Flowmeter_Start_Address = 1
# Flowmeter_Register_Counts = 25

# COD Configurations
COD_Device_Id = 100
COD_Start_Address = 9729
COD_Register_Counts = 10

# BOD Configurations
BOD_Device_Id = 100
BOD_Start_Address = 9729
BOD_Register_Counts = 10

# Temperature Configurations
Temperature_Device_Id = 100
Temperature_Start_Address = 9729
Temperature_Register_Counts = 10

# TSS Configurations
TSS_Device_Id = 100
TSS_Start_Address = 4608
TSS_Register_Counts = 4

# Ph Configurations
Ph_Device_Id = 110
Ph_Start_Address = 9729
Ph_Register_Counts = 5

# TDS Configurations
TDS_Device_Id = 120
TDS_Start_Address = 9729
TDS_Register_Counts = 4

# Error Configurations
Modbus_Error_Message = "Exception Response(131, 3, SlaveFailure)"
Connection_Error_Message = "EIC"
Connection_Checking_Count = 0

# Log Configurations
Log_File = "newfile.log"

# Device Configurations
Pi_Id = "PI01"
Router_Id = "RT01"
Gateway_Id = "GW01"
Device_Id = {"Pi_Id": Pi_Id, "Router_Id": Router_Id, "Gateway_Id": Gateway_Id}

# MQTT Configurations
Command_Type = "30"
Topic = "MKCWIRAS"
Variable_Header = format(len(Topic), "04x") + Topic
