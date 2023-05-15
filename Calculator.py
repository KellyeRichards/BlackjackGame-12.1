# Initialize variables
result = 0
memory = 0

# Define calculation functions


def add(num):
    global result
    result += num


def subtract(num):
    global result
    result -= num


def multiply(num):
    global result
    result *= num


def divide(num):
    global result
    result /= num


# Main program loop
while True:
    # Display menu
    print("Calculator Menu")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Clear")
    print("6. Display Memory")
    print("7. Quit")

    # Get user input
    choice = input("Enter choice (1-7): ")

    # Perform chosen operation
    if choice == '1':
        num = float(input("Enter number to add: "))
        add(num)
        print("Result: ", result)
    elif choice == '2':
        num = float(input("Enter number to subtract: "))
        subtract(num)
        print("Result: ", result)
    elif choice == '3':
        num = float(input("Enter number to multiply: "))
        multiply(num)
        print("Result: ", result)
    elif choice == '4':
        num = float(input("Enter number to divide: "))
        divide(num)
        print("Result: ", result)
    elif choice == '5':
        result = 0
        print("Result: ", result)
    elif choice == '6':
        print("Memory: ", memory)
    elif choice == '7':
        break
    else:
        print("Invalid input")

    # Store result in memory
    memory = result
