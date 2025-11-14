Input = int(input("enter a number: "))
Input_1 = int(input("enter a number: "))
button = input("enter the operation you want to perform (+,-,*,/): ")
button = button.strip()

if button == '+':
    print("the sum is", Input + Input_1)
elif button == '-':
    print("the answer is", Input - Input_1)
elif button == '*':
    print("the answeris", Input * Input_1)
elif button == '/':
    print("the answer is", Input / Input_1)
else:
    print("invalid operation")