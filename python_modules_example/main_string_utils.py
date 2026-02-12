import argparse
import string_utils

parser = argparse.ArgumentParser(description="String utilities")

parser.add_argument("text", help="Text to process")

args = parser.parse_args()

print("Reversed:", string_utils.reverse(args.text))
print("Palindrome:", string_utils.is_palindrome(args.text))
