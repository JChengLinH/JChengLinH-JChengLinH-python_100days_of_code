import os
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
clearConsole()
import day10_project_art as art

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

operations = {
    "+": add, 
    '-': sub,
    '*': mul,
    '/': div,
}

def calculator():
    print(art.logo)
    num1 = float(input("What's the first number?: "))
    num2 = float(input("What's the second number?: "))

    for symbol in operations:
        print(symbol)

    operation_symbol = input("Pick an operation from the line above: ")

    answer = operations[operation_symbol](num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    continue_calculation = True
    while continue_calculation:
        user_input = input(f"Type 'y' to continue calculation with {answer}, or type 'n' to start a new calculation.: ")
        if user_input == 'y':
            answer_prev = answer
            num = float(input("What's the next number?: "))
            operation_symbol = input("Pick an operation: ")
            answer = operations[operation_symbol](answer_prev, num)
            
            print(f"{answer_prev} {operation_symbol} {num} = {answer}")
        else:
            continue_calculation = False
            calculator()
        

calculator()