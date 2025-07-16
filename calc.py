value1 = float(input("Value 1: "))
value2 = float(input("Value 2: "))
op = input("Please enter operator")

try:
    if op == '+':
        ans = value1+value2 
    elif op == '-':
        if value1 > value2:
            ans = value2 -value1
            ans = value1-value2
    elif op == '*':
        ans = value1*value2
    elif op == '/':
        ans = value2 / value1  

    if op in ['+', '-', '*', '/'] and not (op == '/' and value2 == 0):
        print("Answer:", ans)
except ValueError:
    print("Please enter valid numeric values.")
