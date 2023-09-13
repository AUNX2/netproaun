from pymodbus.client.sync import ModbusTcpClient
import socket
from umodbus import conf
from umodbus.client import tcp as modbus_tcp

# PLC's IP address and Modbus TCP port
PLC_IP = '127.0.0.1'
PLC_PORT = 502
a = 30
b = 90
# Modbus address (register number) to write data to
REGISTER_ADDRESS1 = 2 # Replace with the actual register address
REGISTER_ADDRESS2 = 3

# Data to send to the PLC
data_to_send1 = [round(a)]  # Replace with your data
data_to_send2 = [round(b)]

# Connect to the PLC
client = ModbusTcpClient(PLC_IP, port=PLC_PORT)
if client.connect():
    print("Connected to PLC")

    # Write data to the Modbus register
    try:
        client.write_registers(REGISTER_ADDRESS1, data_to_send1)
        print("Data sent successfully to address 2 :", data_to_send1)
        client.write_registers(REGISTER_ADDRESS2, data_to_send2)
        print("Data sent successfully to address 3 :", data_to_send2)
    except Exception as e:
        print("Error writing data:", e)
    finally:
        # Close the Modbus connection
     client.close()


# Enable values to be signed (default is False).
conf.SIGNED_VALUES = True
### Creating connection
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 502))

data_control = round(a)

# Create a message to write multiple coils
message = modbus_tcp.write_multiple_coils(slave_id=1, starting_address=0, values=[1])
message2 = modbus_tcp.write_multiple_coils(slave_id=1, starting_address=0, values=[0])
# Send the message and get the response
if data_control>30:
    response = modbus_tcp.send_message(message, sock)
    print("send {} to address 0 ".format(response))
else:
   response2 = modbus_tcp.send_message(message2,sock)
   print("send {} to address 0 ".format(response2))

# Close the socket connection
sock.close()
print("Transfer finished")