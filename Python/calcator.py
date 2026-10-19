# how do i do this
symbolThingy = input("Enter a symbol thingmajig (+, -, *,  /, ^): ")
firstNumber = float(input("Put the first number of the calculation buddy: "))
secondNumber = float(input("Second number now!!: "))

if symbolThingy == "+":
     result = firstNumber + secondNumber
     print(result)
elif symbolThingy == "-":
     result = firstNumber - secondNumber
     print(result)
elif symbolThingy == "*":
     result = firstNumber * secondNumber
     print(result)
elif symbolThingy == "/":
     result = firstNumber / secondNumber
     print(result)
elif symbolThingy == "^":
     result = firstNumber ** secondNumber
     print(result)
else:
    print(f"bro what does {symbolThingy} mean that aint valid put something valid please")
