import re

# Open and read the text file
with open("data.txt", "r") as file:
    text = file.read()

# Extract names
names = re.findall(r"Name:\s*(\w+)", text)

# Extract email addresses
emails = re.findall(r"[\w.-]+@[\w.-]+\.\w+", text)

# Extract phone numbers
phones = re.findall(r"\b\d{10}\b", text)

# Display extracted information
print("Names:", names)
print("Email addresses:", emails)
print("Phone numbers:", phones)
