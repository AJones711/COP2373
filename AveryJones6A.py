# A program that prompts user to enter a phone number, SSN, and a zip code then tests for validity.
import re

# Create a function to test if entered phone number is valid format.
def isValid_phone(phone):
    pattern = r'\d\d\d[ -]\d\d\d[ -]\d\d\d\d$'
    return re.match(pattern, phone) is not None

# Create a function to test if entered SSN is valid format.
def isValid_ssn(ssn):
    pattern = r'\d\d\d[ -]\d\d[ -]\d\d\d\d$'
    return re.match(pattern, ssn) is not None

# Create a function to test if entered ZIP code is valid format.
def isValid_zip(zip):
    pattern = r'\d\d\d\d\d$'
    return re.match(pattern, zip) is not None

def main():
    # Prompt user to enter a Phone number, SSN, and Zip code.
    phone = input('Enter telephone number (xxx-xxx-xxxx or xxx xxx xxxx): ')
    ssn = input('Enter SSN (xxx-xx-xxxx or xxx xx xxxx): ')
    zip = input('Enter ZIP code:')

    # Check results of the isValid functions if proper format print accepted else print Incorrect.
    if isValid_phone(phone):
        print('Valid Number')
    else:
        print('Incorrect Format')

    if isValid_ssn(ssn):
        print('Valid SSN')
    else:
        print('Incorrect format')

    if isValid_zip(zip):
        print('Valid ZIP code')
    else:
        print('Incorrect format')

main()