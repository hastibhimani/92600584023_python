import shutil
import os

# Create a sample file
with open("source.txt", "w") as file:
    file.write("This is a sample file.")

# Copy the file
shutil.copy("source.txt", "copy.txt")
print("File copied successfully.")

# Move the copied file
shutil.move("copy.txt", "moved.txt")
print("File moved successfully.")

# Delete the moved file
os.remove("moved.txt")
print("File deleted successfully.")
