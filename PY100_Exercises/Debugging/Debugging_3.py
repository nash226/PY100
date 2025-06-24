def multiply_by_five(n):
    return n * 5

print("Hello! Which number would you like to multiply by 5?")
number = int(input()) ##need to change variable type

print(f"The result is {multiply_by_five(number)}!")

# The output we see is because our input value is a string and we need to convert that into an int before we can get the proper output