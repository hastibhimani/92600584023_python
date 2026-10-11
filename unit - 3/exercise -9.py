import re

text = "Python is easy. Python is powerful."

# match()
result = re.match(r"Python", text)
print("match():", result.group() if result else "No match")

# search()
result = re.search(r"easy", text)
print("search():", result.group() if result else "No match")

# findall()
result = re.findall(r"Python", text)
print("findall():", result)
