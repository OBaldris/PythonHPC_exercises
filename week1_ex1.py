# Define the text to write and print
text = "Hello world"

# Write the text to a file
with open("content.txt", "w") as file:
    file.write(text)

# Print the text to the screen
print(text)