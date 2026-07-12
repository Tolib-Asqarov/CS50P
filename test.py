def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return None
    return x / y

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def get_operation():
    valid_ops = ["+", "-", "/", "*", "add", "subtract", "multiply", "divide"]
    while True:
        op = input("What operation? (+,-,*,/,): ").strip().lower()
        if op in valid_ops:
            return op
        print("Invalid operation! Please use +, -, *, or /.")

def main():
    print("Welcome to the calculator!")
    name = input("What's your name? ").strip().title()  
    print(f"Hello, {name}!")

    x = get_number("Enter a number: ")
    y = get_number("Enter another number: ")
    operation = get_operation()

    if operation in ["+", "add"]:
        result = add(x, y)
        symbol = "+"
    elif operation in ["-", "subtract"]:
        result = subtract(x, y)
        symbol = "-"
    elif operation in ["*", "multiply"]:
        result = multiply(x, y)
        symbol = "*"
    elif operation in ["/", "divide"]:
        if y == 0:
            print("Error: Cannot divide by zero!")
            return
        result = divide(x, y)
        symbol = "/"
    else:
        print("Unexpected error!")
        return
    
    print(f"{x} {symbol} {y} = {result:.2f}")

if __name__ == "__main__":
    main()