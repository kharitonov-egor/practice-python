keys = {3: "Fizz", 5: "Buzz"}

for number in range(1,101):
    output = ""
    for divisor in keys:
        if number % divisor == 0:
            output += keys[divisor]
    print(output or number)
