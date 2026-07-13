name = input("What's your name? ")
"""
if name == "David":
    print("Hi, David!")
elif name == "Alice":
    print("Hi, Alice!")
elif name == "Bob":
    print("Hi, Bob!")
elif name == "Charlie":
    print("Hi, Charlie!")
else:
    print("Who? ")
    """

match name:
    case "David" | "Alice" | "Bob":
        print("Albert")
    case "Charlie":
        print("Holaand!")
    case _:
        print("Who? ")