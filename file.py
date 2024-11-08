# import os
# f= open("demo.txt", "w")

# # data =f.write("hello i am rajendra rauta i am doing  java now")
# data = f.read()
# new_data=data.replace("java", "python")
# print(new_data) 
      

# print(data) 
# print(type(data))
# f.close()


# Prompt the user for hours worked and rate per hour
hours = input("Enter Hours: ")
rate = input("Enter Rate per Hour: ")

# Convert input to float
hours = float(hours)
rate = float(rate)

# Calculate gross pay
if hours > 40:
    # Calculate overtime pay for hours above 40
    overtime_hours = hours - 40
    overtime_pay = overtime_hours * (rate * 1.5)
    regular_pay = 40 * rate
    total_pay = regular_pay + overtime_pay
else:
    # No overtime, just regular pay
    total_pay = hours * rate

# Display the result
print("Pay:", total_pay)

