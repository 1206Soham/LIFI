
import serial
import time

esp = serial.Serial('COM5', 9600)
time.sleep(2)

CDMA_CODES = {
    "A": "01100001",
    "B": "01100010",
    "C": "01100011"
}

START_ACK = "1111"
END_ACK = "0000"
ACK_MESSAGE = ''.join(format(ord(c), '08b') for c in "ACK")

sender = input("🧾 Who is sending ACK? (A/B/C): ").strip().upper()
receiver = input("📡 Who should receive the ACK? (A/B/C): ").strip().upper()

if sender not in CDMA_CODES or receiver not in CDMA_CODES:
    print("❌ Invalid IDs.")
    esp.close()
    exit()

cdma_tx = CDMA_CODES[sender]
cdma_rx = CDMA_CODES[receiver]

ack_stream = START_ACK + cdma_rx + cdma_tx + ACK_MESSAGE + END_ACK
if ack_stream[-1] == '1':
    ack_stream += '0'

print(f"📤 Sending ACK Bitstream: {ack_stream}")
input("👉 Press Enter to send ACK...")

for i, bit in enumerate(ack_stream):
    esp.write(bit.encode())
    print(f"Bit {i+1}/{len(ack_stream)} ➜ {bit}")
    time.sleep(1)

esp.close()
print("✅ ACK sent successfully.")
