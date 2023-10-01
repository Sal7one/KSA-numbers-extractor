import pyperclip
import re

# Function to check if copied text is a KSA phone number

def Checknumber():

    # Paste the copied text from clipboard to a string
    text = pyperclip.paste()

    # Use Regex to filter phone numbers from the text string
    regex = re.compile(r'(((009665|9665|\+9665|05|5)(5|0|3|6|4|9|1|8|7))|((0096601|96601|\+96601|01)(1|2|3|4|6|7)))([0-9]{7})')

    filteredtext = regex.findall(text)

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
