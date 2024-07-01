import re  # Importing the regular expression module
import os  # Importing the os module for file path checking

# Define the file paths
input_file_path = 'D:\\Users\\mikep\\Obsidian\\Obsidian\\Blog Page\\DAILY NOTES\\2024-07-01.md'
output_file_path = 'D:\\Users\\mikep\\Obsidian\\Obsidian\\Blog Page\\DAILY NOTES\\2024-07-01_modified.md'

# Step 1: Check if the input file exists
if not os.path.exists(input_file_path):
    print(f"Error: The input file '{input_file_path}' does not exist.")
else:
    # Read the file content
    with open(input_file_path, 'r') as file:
        content = file.read()  # Reading the entire content of the file

    # Step 2: Use re.sub() to insert newlines before "Ch " followed by a number, only if it's not already on a new line
    # The pattern ensures we only add newlines where needed without repeating
    # (?<!\n) asserts that "Ch " is not preceded by a newline
    # (Ch \d+) captures "Ch " followed by one or more digits
    modified_content = re.sub(r'(?<!\n)(?<!\r\n)(Ch \d+)', r'\n\1', content)

    # Step 3: Write the modified content back to a file
    with open(output_file_path, 'w') as file:
        file.write(modified_content)  # Writing the modified content to a new file

    print(f"Modified content written to '{output_file_path}'.")
