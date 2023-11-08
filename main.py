##########################################1
# Initialize an empty set to store all the new  names
new_names = set()

while True:
    name = input("Enter a name (or press Enter to stop): ")

    # If the user enters an empty string, exit the loop
    if name == "":
        break

    # Check if the name is already in the list
    if name in new_names:
        print("Existing name")
    else:
        print("New name")
        # Add the new name to the set
        new_names.add(name)

# Print all the new names entered by the user
print("\nList of new names:")
for name in new_names:
    print(name)


##################################2
# Dictionary to store airport data (ICAO)
airport_data = {}

# Function to add a new airport to the dictionary
def add_new_airport():
    icao_code = input("Enter the ICAO code of the airport: ")
    airport_name = input("Enter the name of the airport: ")
    airport_data[icao_code] = airport_name
    print(f"A new airport of your choice with ICAO code {icao_code} and name {airport_name} has been added .")

# Function to fetch airport information based on ICAO code
def fetch_airport_info():
    icao_code = input("Enter the ICAO code of the airport you want to fetch: ")
    if icao_code in airport_data:
        print(f"The airport with ICAO code {icao_code} is: {airport_data[icao_code]}")
    else:
        print(f"Airport with ICAO code {icao_code} not found.")

# Main program loop
while True:
    print("\nOptions:")
    print("1. Enter a new airport")
    print("2. Fetch airport information")
    print("3. Quit")
    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == "1":
        add_new_airport()
    elif choice == "2":
        fetch_airport_info()
    elif choice == "3":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
