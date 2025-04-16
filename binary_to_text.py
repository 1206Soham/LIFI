
def binary_to_text(binary_data):
    if len(binary_data) % 8 != 0:
        return "❌ Error: Binary length is not a multiple of 8."

    chars = []
    for i in range(0, len(binary_data), 8):
        byte = binary_data[i:i+8]
        byte_str = ''.join(map(str, byte))
        chars.append(chr(int(byte_str, 2)))
    return ''.join(chars)

try:
    with open("msg_bits_temp.txt", "r") as f:
        binary_list = eval(f.read())

    decoded = binary_to_text(binary_list)
    print("\n📤 Decoded Message:")
    print(decoded)

except Exception as e:
    print(f"⚠️ Error: {e}")
