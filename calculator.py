num_1 = input ("Enter First Number: ")
num_2 = input("Enter Second Number: ")

op = input(("Choose an operation '+'  '-' '*' '/' "))

if op == '+':
    print(float(num_1) + float(num_2))
elif op == '-':
    print(float(num_1) - float(num_2))
elif op == '*':
    print(float(num_1) * float(num_2))
elif op == '/':
    print(float(num_1) / float(num_2))

