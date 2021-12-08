import paho.mqtt.client as mqtt
import time
from pymodbus.client.sync import ModbusSerialClient
from pymodbus.client.sync import ModbusTcpClient as ModbusClient

# Parameters for Serial Communication
#client = ModbusSerialClient(
#    method='rtu',
#    port='/dev/ttyp0',
#    baudrate=115200,
#    timeout=5,
#    parity='E',
#    stopbits=1,
#    bytesize=8
#)
Modbus_client = ModbusClient('127.0.0.1', port=502)
while True: # This While loop makes the code runs repeatedly with a time gap given at the end of the code.
    Modbus_client.connect()
    if Modbus_client.connect():  # Trying for connect to Modbus Server/Slave
    #Reading from a holding register with the below content.
        res = Modbus_client.read_holding_registers(address=0, count=1, unit=1)

    #Reading from a discrete register with the below content.'''
    # res = client.read_discrete_inputs(address=1, count=, unit=1)

        if not res.isError(): # This generates error
            print(res.registers)
        else:
            print(res)

    else:
         print('Cannot connect to the Modbus Server/Slave')
    
  
    res1 = res.registers # registers gives the data in a list
    print (type(res1)) 
    def on_message (client, userdata, message):
	    print ("message received", str(message.payload.decode("utf-8")))
	    print ("message topic", message.topic)
	    print ("message qos", message.qos)
	    print ("message retain flag", message.retain)


    client = mqtt.Client ("P1")
    client.on_message = on_message
    print ("connecting to the broker")
    client.connect ("broker.mqttdashboard.com", 1883, 60)
    client.loop_start()
    client.subscribe("Shaswoti/Home/Automation")
    client.publish ("Shaswoti/Home/Automation", res1[0])
    time.sleep(2)
    client.loop_stop()
    time.sleep(3)