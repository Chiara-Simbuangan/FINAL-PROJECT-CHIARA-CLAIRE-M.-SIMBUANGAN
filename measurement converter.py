def display_menu():
    print("Unit Conversion Menu:")
    print("1. Millimeters to Centimeters")
    print("2. Feet to Meters")
    print("3. Inches to Centimeters")
    print("4. Pounds to Kilograms")
    print("5. Gallons to Liters")
    print("6. Exit")

def mm_to_cm(mm):
    return mm / 10

def ft_to_m(ft):
    return ft * 0.3048

def in_to_cm(inches):
    return inches * 2.54

def lb_to_kg(lb):
    return lb * 0.453592

def gal_to_l(gallons):
    return gallons * 3.78541

def unit_conversion():
    while True:
        display_menu()
        choice = input("Choose a conversion option (1-6): ")
        
        if choice == '6':
            print("Exiting the program. Goodbye!")
            break

        if choice not in ['1', '2', '3', '4', '5']:
            print("Invalid choice. Please select a valid option.")
            continue
        
        try:
            value = float(input("Enter the value to be converted: "))
        except ValueError:
            print("Invalid input. Please enter a numerical value.")
            continue

        if choice == '1':
            result = mm_to_cm(value)
            print(f"{value} mm is {result} cm")
        elif choice == '2':
            result = ft_to_m(value)
            print(f"{value} ft is {result} m")
        elif choice == '3':
            result = in_to_cm(value)
            print(f"{value} inches is {result} cm")
        elif choice == '4':
            result = lb_to_kg(value)
            print(f"{value} lb is {result} kg")
        elif choice == '5':
            result = gal_to_l(value)
            print(f"{value} gallons is {result} liters")

if __name__ == "__main__":
    unit_conversion()
