#fib.py
import time
from functools import lru_cache
import matplotlib.pyplot as plt


#empty arrays for x and y plot values
x = []
y = []


#timer decorator is offset by one iteration - kicks in on second call??
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.process_time() #log start time
        result = func(*args, **kwargs) #call fib
        stop = time.process_time() #log end time
        elapsed = stop - start #elapsed time (difference between stop and start)

        y.append(elapsed) #append elapsed time to y value array

        print(f"Finished in {elapsed:.8f}s: f({args[0]}) -> {result}") #print time elapsed
        
        return result
    
    return wrapper


@lru_cache
@timer
#recursive fibonacci function
def fib(n: int) -> int:
    if n <= 1: #n is 0 or 1
        result = n #fibonacci number equals n
    else:
        result = fib(n-1) + fib(n-2) #fibonacci number equals previous two numbers

    x.append(n) #append n to x value array
    
    return result


if __name__ == "__main__":
    fib(100)


#plot
plt.plot(x, y)

plt.show()