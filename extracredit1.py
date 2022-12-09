
# Get the input from the user
name = input("Enter your first and last name: ")

# Use string methods to parse the input
first_name, last_name = name.strip().split()

# Print the name in the desired format
print(f"{last_name}, {first_name[0]}.")






