# check for different types of string validations

# this function checks if the given string contains any alphanumeric characters or not
def contains_alphanumeric(string):
    if(any(character.isalnum() for character in string)):
        return True
    else:
        return False


# this function checks if the given string contains any alphabetical characters or not
def contains_alphabets(string):
    if(any(character.isalpha() for character in string)):
        return True
    else:
        return False


# this function checks if the given string contains any numbers or not
def contains_digits(string):
    if(any(character.isdigit() for character in string)):
        return True
    else:
        return False

# this function checks if the given string contains lowercase letters or not
def contains_lowercase(string):
    if(any(character.islower() for character in string)):
        return True
    else:
        return False

# this function checks if the given string contains uppercase letters or not
def contains_uppercase(string):
    if(any(character.isupper() for character in string)):
        return True
    else:
        return False


if __name__ == '__main__':
    string_to_be_validated = "This Is A String 1234"
    check = contains_lowercase(string_to_be_validated)

    # similarly you can try out the other validation functions
    
    if(check):
        print("String is validated!")
    else:
        print("String is invalid!")