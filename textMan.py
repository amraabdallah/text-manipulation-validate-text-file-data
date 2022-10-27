import re
import sys


def open_file(filename):
    try:
        return open(filename,"r")
    except IOError:
        print('There was an error opening the file!')
        sys.exit()

def is_valid_email(email):
    EMAIL_REGEX = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if(re.fullmatch(EMAIL_REGEX,email)):
        return True
    else:
        return False 

def is_valid_id(id):
    if (id.strip().isnumeric()):
        return True
    else:
        return False

def check_if_the_id_is_even_or_odd():
    file = open_file("file.txt")
    for line in file:
        fields_array = line.split()
        input_email = fields_array[1]
        input_id = fields_array[-1]
        
        if is_valid_email(input_email) and is_valid_id(input_id):
                id = int(input_id)
                if (id %2) == 0:
                    print(f"The id {id} of the email {input_email} is even.")
                else:
                    print(f"The id {id} of the email {input_email} is odd.")


check_if_the_id_is_even_or_odd()