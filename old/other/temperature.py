print("Please type F or Fahrenheit to convert fahrenheit to celsius")
print("Please type C or Celsius to convert celsius to fahrenheit")

answer = input()

array_f=["f","F","fahrenheit","Fahrenheit","Fah","fah","fuck"]
array_c=["c","C","celsius","Celsius","Cel","cel"]

if answer in array_f:
    in_temperature=float(input("Please type temperature: "))

    out_temperature = (in_temperature-32)*(5/9)

    print(f"{in_temperature}F is {out_temperature}C")

elif answer in array_c:

    in_temperature=float(input("Please type temperature: "))

    out_temperature = (in_temperature*(9/5))+32

    print(f"{in_temperature}C is {out_temperature}F")
