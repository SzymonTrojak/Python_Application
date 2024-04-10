import time

def measure_time(unit='seconds'):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.time() if unit == 'seconds' else time.perf_counter()
            result = func(*args, **kwargs)
            end_time = time.time() if unit == 'seconds' else time.perf_counter()
            execution_time = end_time - start_time
            if unit == 'microseconds':
                execution_time *= 1_000_000 
            print(f"Execution time: {execution_time:.6f} {unit}")
            return result
        return wrapper
    return decorator

@measure_time(unit='seconds')
def example_function(n):

    sum = 0
    for i in range(n):
        sum += i
    return sum

result = example_function(1_000_000)