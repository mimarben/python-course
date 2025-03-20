# TODO: Create the logging_decorator() function 👇
def logging_decorator(function):
    def wrapper(*args, **kwargs):
        # Log the arguments passed to the function
        print(f"You called {function.__name__}({', '.join(map(str, args))})")
        
        # Call the original function and store the result
        result = function(*args, **kwargs)
        
        # Log the return value
        print(f"It returned: {result}")
        
        return result  # Return the result of the original function
    return wrapper

# Use the decorator 👇
@logging_decorator
def a_function(*args):
    return sum(args)

# Call the decorated function
a_function(1, 2, 3, 4)