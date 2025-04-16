
import serial
import time
import subprocess

# Serial setup
esp = serial.Serial('COM5', 9600)
time.sleep(2)

CDMA_CODES = {
    "A": "01100001",
    "B": "01100010",
    "C": "01100011"
}

PASSWORDS = {
    "A": "alpha123",
    "B": "bravo456",
    "C": "charlie789"
}

START_BITS = "1100"
END_BITS = "0011"

print("🟢 Secure ESP32 LED Text-to-Binary Transmitter")

# Sender Authentication
sender = input("✉️ Who is sending? (A/B/C): ").strip().upper()
if sender not in CDMA_CODES:
    print("❌ Invalid sender.")
    exit()

password = input(f"🔑 Enter password for {sender}: ").strip()
if password != PASSWORDS[sender]:
    print("❌ Authentication failed.")
    exit()

while True:
    receiver = input("📡 Who is the receiver? (A/B/C): ").strip().upper()
    if receiver not in CDMA_CODES:
        print("❌ Invalid receiver.")
        continue

    message = input("💬 Enter your message: ").strip()
    if not message:
        print("⚠️ Empty message.")
        continue

    msg_bits = ''.join(format(ord(c), '08b') for c in message)
    msg_len = format(len(msg_bits), '08b')
    cdma_rx = CDMA_CODES[receiver]
    cdma_tx = CDMA_CODES[sender]

    bitstream = START_BITS + cdma_rx + cdma_tx + msg_len + msg_bits + END_BITS
    if bitstream[-1] == '1':
        bitstream += '0'

    print(f"📦 Bitstream: {bitstream}")
    input("👉 Press Enter to transmit...")

    for i, bit in enumerate(bitstream):
        esp.write(bit.encode())
        print(f"Bit {i+1}/{len(bitstream)} ➜ {bit}")
        time.sleep(1)

    print("✅ Transmission complete.")

    # Ask to receive ACK
    ask_ack = input("🔁 Do you want to receive ACK now? (yes/no): ").strip().lower()
    if ask_ack in ["yes", "y"]:
        subprocess.run(["python", "ACK_Receiver.py"])

    next_action = input("\n▶️ Do you want to send another message? (yes to continue / no to exit): ").strip().lower()
    if next_action not in ["yes", "y"]:
        break

esp.close()
print("👋 Exiting Transmitter.")
