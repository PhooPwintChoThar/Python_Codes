import os
def replace_text_in_file():
    filename = input("Enter a filename: ")
    
    #if not os.path.exists(filename):
        #print(f"Error: {filename} does not exist.")
        #ttreturn
    
    try:
        with open(filename, 'r') as file:
            content = file.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return
    
    old_string = input("Enter the old string to be replaced: ")
    new_string = input("Enter the new string: ")
    
    if old_string == new_string:
        print("Error: The old and new strings are the same.")
        return

    if old_string not in content:
        print(f"Error: '{old_string}' not found in the file.")
        return

    updated_content = content.replace(old_string, new_string)
    
    try:
        with open(filename, 'w') as file:
            file.write(updated_content)
        print("Text replaced successfully.")
    except Exception as e:
        print(f"Error writing to file: {e}")

def main():
    replace_text_in_file()
main()