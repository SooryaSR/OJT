  #Write a Python program with a function that converts a string to an integer.
  # Handle exceptions within the function and print appropriate error messages.
def str_int(s):
    try:
        # Attempt to convert the string to an integer
        result = int(s)
        return result
    except ValueError:
        print(f'Error: "{s}" is not a valid integer.')
    except TypeError:
        print(f'Error: "{s}" is not a valid input type.')

# Test cases
print(str_int("123"))  # Should print: 123
print(str_int("abc"))  # Should print: Error: "abc" is not a valid integer.
print(str_int(None))   # Should print: Error: "None" is not a valid input type.

