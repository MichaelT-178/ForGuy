import re

pattern = r"(?:\s*\.)\b(lastname|firstname|value)\b"
pattern = r'(?<=\.)(lastname|firstname|value)'
string = " guy.value"

match = re.search(pattern, string)

if match:
    print("YEET")
else:
    print("No match")
