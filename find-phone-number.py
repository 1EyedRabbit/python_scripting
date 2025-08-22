import re

def find_phone_numbers(text):

  # The regular expression to match a 10-digit phone number with hyphens.
  # r"" creates a raw string, which is the best practice for regex in Python.
  # \d{3} matches exactly three digits.
  # - matches a literal hyphen.
  # \d{4} matches exactly four digits.
  # The entire pattern is grouped by parentheses.

  pattern = re.compile(r'\d{3}-\d{3}-\d{4}')

  return pattern.findall(text)

sample_text = "My phone number is 444-555-5555. Please call me. Alternate number is 222-333-4444."

found_numbers = find_phone_numbers(sample_text)

if found_numbers:
  print("Found the following phone numbers in your text:")
  for number in found_numbers:
    print(number)
else:
  print("No phone numbers found...")
