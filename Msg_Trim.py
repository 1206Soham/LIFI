
import subprocess

CDMA_CODES = {
    "01100001": "A",
    "01100010": "B",
    "01100011": "C"
}

PASSWORDS = {
    "A": "alpha123",
    "B": "bravo456",
    "C": "charlie789"
}

def extract_message(data, expected_rx):
    start_idx = 0
    while start_idx < len(data) and data[start_idx] == 0:
        start_idx += 1
    end_idx = len(data) - 1
    while end_idx >= 0 and data[end_idx] == 0:
        end_idx -= 1
    if start_idx > end_idx:
        return "❌ No valid data found."
    trimmed_data = data[start_idx:end_idx + 1]
    if trimmed_data[0:4] != [1, 1, 0, 0]:
        return "❌ Start bits not found."
    if len(trimmed_data) < 28:
        return "❌ Frame too short."

    cdma_rx = trimmed_data[4:12]
    cdma_tx = trimmed_data[12:20]
    msg_len_bits = trimmed_data[20:28]
    msg_len = int(''.join(map(str, msg_len_bits)), 2)
    msg_bits = trimmed_data[28:28+msg_len]

    if trimmed_data[28+msg_len:28+msg_len+4] != [0, 0, 1, 1]:
        return "❌ End bits not found."

    rx_id = CDMA_CODES.get(''.join(map(str, cdma_rx)), "Unknown")
    tx_id = CDMA_CODES.get(''.join(map(str, cdma_tx)), "Unknown")

    if rx_id != expected_rx:
        return f"❌ Receiver mismatch. Expected: {expected_rx}, Found: {rx_id}"

    print(f"✅ Message from: {tx_id}")
    print(f"💡 Message Bits: {msg_bits}")
    return msg_bits

try:
    binary_data = eval(input("📥 Enter binary list: "))
    if not isinstance(binary_data, list) or not all(b in [0, 1] for b in binary_data):
        raise ValueError("List must contain only 0s and 1s.")

    expected_rx = input("🧾 Confirm receiver ID (A/B/C): ").strip().upper()
    if expected_rx not in PASSWORDS:
        raise ValueError("Invalid receiver ID.")
    pwd = input(f"🔐 Enter password for {expected_rx}: ").strip()
    if pwd != PASSWORDS[expected_rx]:
        raise ValueError("Authentication failed.")

    bits = extract_message(binary_data, expected_rx)
    if isinstance(bits, str) and bits.startswith("❌"):
        print(bits)
        exit()

    with open("msg_bits_temp.txt", "w") as f:
        f.write(str(bits))

    while True:
        print("\n📌 What would you like to do next?")
        print("1. Decode message (binary_to_text.py)")
        print("2. Send ACK to transmitter (ACK.py)")
        choice = input("Enter 1 or 2: ").strip()

        if choice == "1":
            subprocess.run(["python", "binary_to_text.py"])
            follow_up = input("\n🔁 Do you want to send ACK now? (yes/no): ").strip().lower()
            if follow_up in ["yes", "y"]:
                subprocess.run(["python", "ACK.py"])
            break
        elif choice == "2":
            subprocess.run(["python", "ACK.py"])
            break
        else:
            print("⚠️ Invalid input. Try again.")
except Exception as e:
    print(f"⚠️ Error: {e}")
