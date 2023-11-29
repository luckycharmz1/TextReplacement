def replace_text(filename, old_string, new_string):
    try:
        with open(filename, 'r') as file:
            original_content = file.read()

        updated_content = original_content.replace(old_string, new_string)

        with open(filename, 'w') as file:
            file.write(updated_content)

        print("Text replacement completed successfully.")

    except FileNotFoundError:
        print("File not found. Please enter a valid filename.")
    except Exception as e:
        print("An error occurred:", str(e))


# Prompting the user for inputs
file_name = input("Enter the file name: ")
old_text = input("Enter the text to replace: ")
new_text = input("Enter the new text: ")

replace_text(file_name, old_text, new_text)
