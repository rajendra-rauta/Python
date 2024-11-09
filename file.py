# Initialize variables
largest = None
smallest = None

# Start the loop
while True:
    user_input = input("Enter a number (or 'done' to finish): ")
    
    # Exit the loop if 'done' is entered
    if user_input == 'done':
        break
    
    try:
        # Try converting the input to an integer
        num = int(user_input)
        
        # Update largest and smallest values
        if largest is None or num > largest:
            largest = num
        if smallest is None or num < smallest: 
            smallest = num
    except ValueError:
        # Handle invalid input (non-integer values)
        print("Invalid input")

# After the loop ends, print the results
if largest is not None and smallest is not None:
    print(f"Maximum is {largest}")
    print(f"Minimum is {smallest}")
else:
    print("No valid numbers were entered.")
