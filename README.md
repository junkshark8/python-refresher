# python-refresher
### Web Dev Spring24 Assignment 1

#### Part 1
The first part of this assignment was to create an echo function that mimics a real-life echo. The function takes string text and an int number of repetitions. The text is given as user input and the repetition is hard-coded to 3. The function iterates through the repetitions with a while loop and prints the last i characters of the text, based on the number of repetitions left. 
###### Output
<img width="359" style="padding: 25" alt="echo_output1" src="https://github.com/junkshark8/python-refresher/assets/152639308/7cf2370e-6a33-449f-9ec1-a2e51bbdc1ce">
<img width="338" alt="echo_output2" src="https://github.com/junkshark8/python-refresher/assets/152639308/cd491953-d567-42f0-83fc-96b3cb55d23a">

#### Part 2
The second part of the assignment was to create a function that prints every Fibonacci number up to the nth along with the execution time for each number. The function is a recursive Fibonacci formula with a timer decorator that logs the start and stop time for each function call and calculates the elapsed time. Execution time was optimized using lru_cache. The output of the program is plotted in the program using pyplot.
###### Output
<img width="335" alt="fib_output1" src="https://github.com/junkshark8/python-refresher/assets/152639308/b98a99e0-7064-4a52-aa97-a1ed0416da1f">
<img width="427" alt="fib_output2" src="https://github.com/junkshark8/python-refresher/assets/152639308/a035e803-3d16-4467-869d-067590e4eb87">

###### Plot
The y-axis is the time elapsed, while the x-axis is the index in the Fibonacci sequence. The plot shows a direct linear relationship between time elapsed and index in the sequence: as one increases, so does the other.
<br><br>
![Plot](https://github.com/junkshark8/python-refresher/assets/152639308/6a46cf2a-2e7f-4b1e-8672-86acb6809153)
