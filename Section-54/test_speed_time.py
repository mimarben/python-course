import time


# Write your code below 👇

def speed_calc_decorator(function):
    def chrono():
        start_time = time.time()
        function()
        end_time = time.time()
        execution_time = end_time - start_time  # Calculate execution time
        print("----------------------------------------------------------------")
        print(f"{function.__name__} run speed: {execution_time}s")
    return chrono


@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i
    
@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i

# Print current time
current_time = time.time()
print(current_time)

# Run the functions
fast_function()
slow_function()