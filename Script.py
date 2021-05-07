# Import the necessary python modules 
import serial, time 

# Declaration and initialization of the serial port     
ser = serial.Serial ( port='COM12', 
                      baudrate=9600,
                      parity=serial.PARITY_NONE,
                      stopbits=serial.STOPBITS_ONE,
                      bytesize=serial.EIGHTBITS,
                      timeout=1
                     )

# An infinite loop
while(1): 
    if ( ser.in_waiting > 0 ):
        Data_Serial = ser.readline() # Read data from serial port 
        Data = str(Data_Serial[1:len(Data_Serial)]) # Remove the first character, which is the message ID 
        print("Received message : ",Data) # Print the received message
        time.sleep(0.05) # Wait for 50 ms
        if ( Data == "b'Hello Dorji'" ): # If the message is 'Hello Dorji', send hello back to Heltec CubeCell dev_board 
            ser.write(str.encode("Hello Heltec CubeCell")) 
            print("Hello back has been sent to Heltec CubeCell")
