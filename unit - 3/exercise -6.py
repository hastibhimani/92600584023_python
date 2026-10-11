import os
import sys

# Display current directory
print("Current directory:", os.getcwd())

# List files and folders
print("Files and folders:")
print(os.listdir())

# Create a directory
if not os.path.exists("TestFolder"):
    os.mkdir("TestFolder")
    print("Directory created.")

# Display Python version
print("Python version:", sys.version)
