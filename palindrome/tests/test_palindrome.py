from palindrome import is_palindrome
import unittest

class TestPalindrome(unittest.TestCase):
    def test_palindrome(self):
        self.assertAlmostEqual(is_palindrome("A man a plan a canal Panama"), "✅ Success: The input is a palindrome")
        self.assertEqual(is_palindrome("Madam In Eden, I'm Adam"), "✅ Success: The input is a palindrome")
        self.assertEqual(is_palindrome("racecar"), "✅ Success: The input is a palindrome")
        
    def test_non_palindrome(self):
        # Test cases where the input is not a palindrome
        self.assertEqual(is_palindrome("Hello World"), "❌ Reject: The input is not a palindrome")
        self.assertEqual(is_palindrome("Python"), "❌ Reject: The input is not a palindrome")
    
    def test_empty_string(self):
        # Test case where the input is an empty string
        self.assertEqual(is_palindrome(""), "✅ Success: The input is a palindrome")  # Empty string is considered a palindrome
    
    def test_special_characters(self):
        # Test case with special characters
        self.assertEqual(is_palindrome("!@#$$#@!"), "✅ Success: The input is a palindrome")  # Special chars should be ignored

if __name__ == '__main__':
    unittest.main()