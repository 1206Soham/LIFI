import serial
import time

esp = serial.Serial('COM5', 9600)
time.sleep(2)  # Wait for ESP32 to reset

print("ESP32 LED Text to Binary Blinker")
print("Enter text, and it will be converted to binary for LED blinking.")
print("Type 'EXIT' to quit.")

while True:
    cmd = input("Enter text: ").strip()
    
    if cmd.lower() == "exit":
        print("Exiting...")
        break
    elif cmd:
        binary_data = ''.join(format(ord(char), '08b') for char in cmd)  # Convert text to binary
        print(f"Binary representation: {binary_data}")
        
        start_time = time.time()  # Start timer
        esp.write(binary_data.encode())  # Send entire binary string at once
        end_time = time.time()  # End timer

        duration = end_time - start_time
        bits_sent = len(binary_data)
        if duration > 0:
            datarate = bits_sent / duration
            print(f"Data rate: {datarate:.2f} bits/sec")
        else:
            print("Data sent instantly (duration too short to measure)")

        print("Blinking initiated...")
    else:
        print("Invalid input. Please enter some text or type 'EXIT'.")

esp.close()
