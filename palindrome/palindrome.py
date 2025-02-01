import re

# Main function to get user input and call the palindrome check function
def main():
    word = input("What's your word/sentence: ")  # Get input from the user
    print(is_palindrome(word))  # Check if the input is a palindrome


# Function to check if a given text is a palindrome
def is_palindrome(text):
    
    # Remove all non-alphanumeric characters and convert to lowercase
    text = re.sub(r'[^a-zA-Z0-9]', '', text).lower()
    
    # Remove any spaces from the text (though not really necessary as the text is already clean)
    result = "".join(text.split())

    # Compare the original text with its reversed version
    if text == result[::-1]: 
        return "✅ Success: The input is a palindrome"  # If they match, it's a palindrome
    else:
        return "❌ Reject: The input is not a palindrome"  # If they don't match, it's not a palindrome


# Run the main function
if __name__ == "__main__":
    main()

