import serial
import time

# --- Configuration ---
PORT = 'COM5'
BAUD_RATE = 115200

# --- User Input for Duration ---
try:
    DURATION = int(input("⏱️ Enter duration (in seconds) to record voltage readings: "))
except ValueError:
    print("❌ Invalid input! Please enter a valid integer.")
    exit()

readings = []  # Store voltage readings

try:
    ser = serial.Serial(PORT, BAUD_RATE, timeout=1)
    time.sleep(2)  # Give ESP32 time to reset
    print(f"✅ Connected to {PORT} at {BAUD_RATE} baud rate.")
    print(f"📡 Recording voltage for {DURATION} seconds...\n")

    start_time = time.time()

    while time.time() - start_time < DURATION:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8', errors='ignore').strip()
            if line.startswith("Voltage:"):
                print("Received:", line)
                try:
                    voltage_str = line.split(":")[1].strip().replace(" V", "")
                    voltage_val = float(voltage_str)
                    readings.append(voltage_val)
                except ValueError:
                    pass  # Skip invalid lines

    print("\n📊 Final list of voltage readings:")
    print(readings)

except serial.SerialException as e:
    print(f"⚠️ Serial error: {e}")

except KeyboardInterrupt:
    print("\n⛔ Interrupted by user.")

finally:
    if 'ser' in locals() and ser.is_open:
        ser.close()
        print("🔌 Serial connection closed.")
