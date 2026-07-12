""" 
x = int(input("Enter a number: "))

# is this number even or odd?
if x % 2 == 0:
    print(f"{x} is even.")
else:
    print(f"{x} is odd.")
"""

def main():
    x = int(input("Enter a number: "))
    if is_even(x):
        print(f"{x} is even.")
    else:
        print(f"{x} is odd.")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

main()