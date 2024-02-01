#fib.py
import time
from functools import lru_cache
import matplotlib.pyplot as plt


#empty lists for x and y plot values
x = []
y = []


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.process_time() #log start time
        result = func(*args, **kwargs) #call fib
        stop = time.process_time() #log end time
        elapsed = stop - start #elapsed time (difference between stop and start)

        x.append(args[0]) #append n (args) to x value list
        y.append(elapsed) #append elapsed time to y value list

        print(f"Finished in {elapsed:.8f}s: f({args[0]}) -> {result}") ##print time elapsed, f(n), and fibonacci number
        
        return result
    
    return wrapper


@lru_cache
@timer
#recursive fibonacci function
def fib(n: int) -> int:
    if n <= 1: #n is 0 or 1
        result = n #fibonacci number equals n
    else:
        result = fib(n-1) + fib(n-2) #fibonacci number equals sum of previous two numbers
    
    return result


if __name__ == "__main__":
    fib(100)


#plot
plt.plot(x, y)

plt.show()
