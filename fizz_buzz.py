"""Prints the numbers 1 - 100. If divisible by 3, prints Fizz.
If divisible by 5, prints Buzz. If divisible by both, prints
FizzBuzz"""

for count in range(1,101):

    if count % 3 ==0 and count % 5 == 0:
        print("FizzBuzz")
    elif count % 3 == 0:
        print("Fizz")
    elif count % 5 == 0:
        print("Buzz")
    else:
        print(str(count))