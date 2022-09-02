cisla = list(range(1,101))

fizz= ()
buzz= ()
fuzzbuzz= ()

for number in cisla:
    if number % 15 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)