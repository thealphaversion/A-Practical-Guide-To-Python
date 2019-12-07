if __name__ == '__main__':
    s = input()
    if(any(string.isalnum() for string in s)):
        print("True")
    else:
        print("False")

    if(any(string.isalpha() for string in s)):
        print("True")
    else:
        print("False")

    if(any(string.isdigit() for string in s)):
        print("True")
    else:
        print("False")

    if(any(string.islower() for string in s)):
        print("True")
    else:
        print("False")

    if(any(string.isupper() for string in s)):
        print("True")
    else:
        print("False")
