import serial

ser = serial.Serial("/dev/ttyS5", baudrate=38400, timeout=1)

def send_command(command):
    ser.write(command.encode())
    response = ser.readline().decode().strip()
    return response

while True:
    data = input("Enter a command: ")
    response = send_command(data)
    print("Response:", response)
