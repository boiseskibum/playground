import serial
import pyudev

# Create a Pyudev context
context = pyudev.Context()

# Get a list of serial devices
serial_devices = [device for device in context.list_devices(subsystem='tty')]

# Iterate over the serial devices
for device in serial_devices:
    device_name = device.device_node

    # Open the serial port
    try:
        ser = serial.Serial(device_name)
    except serial.SerialException:
        continue

    # Print device information
    print("Serial Port:", device_name)
    print("Device ID:", device['ID_SERIAL_SHORT'])
    print("Manufacturer:", ser.name)
    print()

    # Close the serial port
    ser.close()

