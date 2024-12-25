#  Regular expressions are a powerful tool for matching patterns in strings. The re module in Python provides functions to search, match, and manipulate strings based on patterns.
import re
text = "Some sample text with several words starting with s."
pattern = r'\bs\w+'
matches = re.findall(pattern,text)
print(matches)