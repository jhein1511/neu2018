# print welcome to user
print "Welcome to the great Calculator Program!!"
print "="*40

# read user input for operation
operation_symbol = raw_input("Please enter an operation (+,-,*,/): ")
print "You entered " + operation_symbol

# read user input for first value
num1 = float(raw_input("Please enter you first number: "))
print "You entered " + str(num1)

# read user input for second value
num2 = float(raw_input("Please enter you second number: "))
print "You entered " + str(num2)

# calculate
if operation_symbol == "+":
    print num1 + num2
elif operation_symbol == "-":
    print num1 - num2
elif operation_symbol == "*":
    print num1 * num2
elif operation_symbol == "/":
    print num1 / num2
else:
    print "Invalid entry"

# print result

print

