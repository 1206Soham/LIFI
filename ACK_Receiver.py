
import serial
import time

esp = serial.Serial('COM5', 9600)
time.sleep(2)

print("🟡 Listening for ACK...")
ack_bits = []

while True:
    if esp.in_waiting:
        bit = esp.read().decode()
        if bit in ['0', '1']:
            ack_bits.append(int(bit))
            print(f"Received bit: {bit}")
        if len(ack_bits) >= 48:  # Basic length threshold for ACK frame
            break
    time.sleep(0.1)

esp.close()
print(f"📥 ACK Bitstream: {ack_bits}")
print("✅ ACK reception complete.")
