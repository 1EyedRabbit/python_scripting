# Imports re module for regular expression operations.
import re

def find_urls(text):
  """
  Finds all legal URLs in a given string.

  Args:
    text: The input string to search.

  Returns:
    A list of all matched URLs.
  """
  # The regex matches a legal URL.
  # It covers http/https protocols, optional 'www' subdomain,
  # and various top-level domains and paths.
  #
  # r"" for creating a raw string
  # (?i)           - This is a flag that makes the entire pattern case-insensitive.
  # (?:https?://)  - Non-capturing group for the protocol.
  #                  https?: The 's' is optional, matching both http and https.
  #                  ://: Matches the literal characters.
  # (?:www\.)?     - Non-capturing group for the optional 'www.' subdomain.
  #                  ?: The '?' makes the entire group optional.
  # [a-zA-Z0-9.-]+ - Matches the main domain name. It allows for letters, digits,
  #                  dots, and hyphens, and requires at least one character.
  # \.[a-zA-Z]{2,6}- Matches the top-level domain (e.g., .com, .org, .net).
  #                  \.: Matches a literal dot.
  #                  [a-zA-Z]{2,6}: Matches 2 to 6 letters.
  # (?:/[^\s]*)?   - An optional, non-capturing group for the rest of the URL path.
  #                  /: Matches a literal forward slash.
  #                  [^\s]*: Matches any character that is NOT a whitespace character,
  #                  zero or more times.
  #                  ?: The '?' makes this entire group optional.
  pattern = re.compile(r'(?i)\b(?:https?://|www\.)[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/[^\s]*)?\b')

  # Find all matches in the input string. Returns them as a list.
  return pattern.findall(text)

sample_text = """
Visit my website at https://www.example.com.
You can also check out http://blog.mysite.net and our support page: https://support.app.org/help?q=regex.
A simple one is www.google.com.
This is not a URL: example.com (no protocol or www.).
Another non-URL: https://local-host:8080 (no proper TLD).
Also invalid is https://this is not a url.
Here is a good one https://www.google.com/search?q=python+regex&oq=python+regex&aqs=chrome..69i57j0l5j69i60l2.1235j0j7&sourceid=chrome&ie=UTF-8
"""

found_urls = find_urls(sample_text)

if found_urls:
  print("Found URLs:")
  for url in found_urls:
    print(url.strip()) # .strip() removes potential leading/trailing whitespace
else:
  print("No URLs found.")

