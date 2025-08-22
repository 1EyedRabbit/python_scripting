import re

def extract_address(text):

   # The regular expression to match a street address.
  # r"" creates a raw string, which is the best practice for regex in Python.
  #
  # \b           - Matches a word boundary, ensuring the match is a whole word
  #                and not part of a larger string (e.g., "CASTLE" would not match).
  # \d+          - Matches one or more digits (the street number).
  # \s+          - Matches one or more whitespace characters (the space after the number).
  # [A-Za-z\s]+  - Matches the street name. It allows for one or more
  #                uppercase or lowercase letters, and spaces (e.g., "Main Street").
  # \s+          - Matches one or more whitespace characters (the space before the suffix).
  # (?:ST|AVE)   - This is a non-capturing group (?:...) that matches either
  #                "ST" or "AVE". The '|' acts as an OR operator.
  # \b           - Matches another word boundary to end the pattern.
  #
  # re.IGNORECASE - This flag is used to make the matching case-insensitive, so
  #                 "st" and "St" will also match.

  pattern = re.compile(r'\b\d+\s+[A-za-z\s]+\s+\b(?:ST|AVE)', re.IGNORECASE)
  addresses=pattern.findall(text)
  return addresses

sample_text = """
The main office is at 123 Main Street, Suite 400.
The new building is at 456 Oak AVE.
We are located at 789 Maple St.
My old address was 1234 S Elm Road. This should not match.
Also, check for 500 Broad ST.
The address is 100 First ave.
"""

extract_results = extract_address(sample_text)

if extract_results:
  print("Following addresses have been found:")
  for address in extract_results:
    print(address)
else:
  print("No addresses found...")
