import pyperclip
import re

# Function to check if copied text is a KSA phone number


def Checknumber():

    # Paste the copied text from clipboard to a string
    text = pyperclip.paste()

    # Use Regex to filter phone numbers from the text string
    filteredtext = re.findall("((\+)?(966( |-)?|0)5[0-9]{8})", text)

    # Create a new array to save the numbers
    numbers = []

    # Itrate through the filtered text and save them to the array
    for phonenumber in filteredtext:
        numbers.append(phonenumber[0])

    # Use the join function to put a new line between every number in the array, Then copy that to the clipboard
    result = '\n'.join(numbers)
    pyperclip.copy(result)
    print("Done. Paste the numbers anywehre you want!")


# Call the function
Checknumber()
