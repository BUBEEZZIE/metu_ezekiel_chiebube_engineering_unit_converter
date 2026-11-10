
# ENGINEERING UNIT CONVERTER

# Function that performs unit conversions
def convert_units():

    # Ask the user to enter a unit
    unit = input(
        "\nEnter unit (mm, inches, °C, °F, kg, lb, km/h, m/s): "
    ).strip()

    # Check if the unit entered is valid
    if unit not in ["mm", "inches", "°C", "°F", "kg", "lb", "km/h", "m/s"]:
        print("Invalid unit! Please enter a valid unit.")
        return

    # Ask the user to enter the value
    try:
        value = float(input("Enter the value: "))
    except ValueError:
        print("Invalid number! Please enter a numeric value.")
        return

    # Convert the measurement based on the unit
    if unit == "mm":
        result = value / 25.4
        print(value, "mm =", round(result, 3), "inches")

    elif unit == "inches":
        result = value * 25.4
        print(value, "inches =", round(result, 3), "mm")

    elif unit == "°C":
        result = (value * 9/5) + 32
        print(value, "°C =", round(result, 2), "°F")

    elif unit == "°F":
        result = (value - 32) * 5/9
        print(value, "°F =", round(result, 2), "°C")

    elif unit == "kg":
        result = value * 2.20462
        print(value, "kg =", round(result, 3), "lb")

    elif unit == "lb":
        result = value / 2.20462
        print(value, "lb =", round(result, 3), "kg")

    elif unit == "km/h":
        result = value / 3.6
        print(value, "km/h =", round(result, 3), "m/s")

    elif unit == "m/s":
        result = value * 3.6
        print(value, "m/s =", round(result, 3), "km/h")


# Main program loop
while True:

    # Display the program title
    print("\n===== ENGINEERING UNIT CONVERTER =====")

    # Call the conversion function
    convert_units()

    # Ask if the user wants another conversion
    choice = input("\nDo you want to convert again? (yes/no): ").strip().lower()

    # Stop the program if the user chooses no
    if choice == "no":
        print("Thank you for using the Engineering Unit Converter!")
        break

    # Continue if the user chooses yes
    elif choice == "yes":
        continue

    # Handle an invalid response
    else:
        print("Invalid choice! The program will close.")
        break
