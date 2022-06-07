from azure.iot.device import IoTHubDeviceClient, Message

from Configurations import Iot_Connection_String, Network_Connection_Error
from Common_Functions import Log_File_Messages


def Iothub_Client_Init():
    iothub_client = IoTHubDeviceClient.create_from_connection_string(
        Iot_Connection_String)
    return iothub_client


def Iothub_Client_Telemetry_Sample_Run(reading):
    try:
        iothub_client = Iothub_Client_Init()
        message = Message(reading)
        print("Sending message: {}".format(message))
        iothub_client.send_message(message)
        print("Message successfully sent")

    except Exception as e:
        Log_File_Messages(Network_Connection_Error)
