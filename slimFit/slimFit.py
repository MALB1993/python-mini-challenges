# Main function that executes BMI calculation and categorization
def main():
    # Get user input for height (in cm) and weight (in kg)
    height = float(input("What's your height (cm): "))
    weight = float(input("What's your weight (kg): "))    
    
    # Calculate BMI using the body_calculation function
    bmi = body_calculation(height, weight)
    
    # Display the result with BMI category
    print(f"You have {bmi} kg weight, so your BMI category is: {categorize_bmi(bmi)}")

# Function to calculate BMI
def body_calculation(height, weight):
    # Calculate the square of the height (height should be converted to meters, but here we are using cm directly)
    pow_height = pow(height, 2)  
    # Calculate BMI and round the result to two decimal places
    return round(weight / pow_height, 2)

# Function to categorize BMI based on different ranges
def categorize_bmi(checked_body):
    # Categorize based on the BMI value
    if checked_body > 40:
        return "Obesity Class 3"  # Obesity Class 3
    elif 40 >= checked_body > 35:
        return "Obesity Class 2"  # Obesity Class 2
    elif 35 >= checked_body > 30:
        return "Obesity Class 1"  # Obesity Class 1
    elif 30 >= checked_body > 25:
        return "Overweight"  # Overweight
    elif 25 >= checked_body > 18.5:
        return "Normal weight"  # Normal weight
    elif checked_body <= 18.5:
        return "Underweight"  # Underweight
    else:
        return "Something went wrong!"  # Error message (this should rarely happen)

# Call the main function to execute the program
main()
