# Main function to drive the program
def main():
    # Get the first number from the user
    num_one = get_number("what's your number_one : ")
    
    # Get the second number from the user
    num_two = get_number("what's your number_two : ")
    
    # Get the operator from the user
    operator = get_operator("what's your operator : ")
    
    # Check the operator and calculate the result
    result = check_operator(operator, num_one, num_two)
    
    # If the result is not None (valid result), print the result
    if result is not None:
        print(f"The result is: {result}")
    
# Function to get a valid number from the user
def get_number(message):
    try:
        # Try to convert the input to an integer
        number = int(input(message))
        return number
    except ValueError:
        # If input is not a valid number, print an error message and ask again
        print("Please enter a valid number")
        return get_number(message)  # Recursively call the function until a valid number is entered

# Function to get the operator from the user
def get_operator(message):
    return input(message)

# Function to check the operator and perform the corresponding operation
def check_operator(operator, number_one, number_two):
    match operator:
        case "+":  # If operator is '+', add the numbers
            return number_one + number_two
        case "-":  # If operator is '-', subtract the numbers
            return number_one - number_two
        case "/":  # If operator is '/', divide the numbers
            if number_two != 0:  # Prevent division by zero
                return number_one / number_two
            else:
                # If the second number is zero, print an error message
                print("You can not use 0 for /")
        case "%":  # If operator is '%', check if the first number is even or odd
            if number_one % 2 == 0:
                return "Your number is even"
            else:
                return "Your number is odd"
        case _:  # If the operator is invalid, print an error message
            print("Invalid operator")
            return None  # Return None for invalid operators

# Call the main function to start the program
main()
