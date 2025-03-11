import time
import random
import string
def decorator_function(function):
    def wrapper_function(name):
        #do somethin before this function call
        time.sleep(2)
        function(name)
        random_letters = ''.join(random.choices(string.ascii_letters, k=3))
        print(f"Random letters: {random_letters}")  # add this line to show the output in sequence
        name = name + random_letters  # add this line to show the output in sequence
        time.sleep(1)  # add delay here to show the output in sequence
        function(name)
        #do somethin after the function call
    return wrapper_function
@decorator_function
def say_hello(name):
    print(f"Hello, {name}!")
@decorator_function
def say_goodbye(name):    
    print(f"Goodbye, {name}!")
def say_greet(name):
    time.sleep(2)
    print(f"Greetings, {name}!")

say_hello("miguel")

decor_func= decorator_function(say_greet)("Maria")
print(decor_func)