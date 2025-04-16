def voltage_to_binary(user_input):
    binary_output = []
    for voltage in user_input:
        if round(voltage, 2) == 0.00:
            binary_output.append(0)
        else:
            binary_output.append(1)
    return binary_output

# === Example: User provides the input ===
user_voltage_list = input("Enter the voltage readings as a list (e.g., [0.4, 0.0, 0.3]):\n")

try:
    # Safely evaluate the string input into a list
    voltage_list = eval(user_voltage_list)

    if isinstance(voltage_list, list) and all(isinstance(v, (int, float)) for v in voltage_list):
        binary_result = voltage_to_binary(voltage_list)
        print("\nBinary interpretation:")
        print(binary_result)
    else:
        print("Invalid input. Please enter a list of numbers.")

except Exception as e:
    print(f"Error processing input: {e}")
