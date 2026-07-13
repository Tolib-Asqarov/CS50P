#def get_age for ask 
def get_age():
    while True:
        try:
            return int(input("How old are you? "))
        except ValueError:
            print("Please, enter a number only")


def get_ticket_price(age,category):
    if age <= 12:
        if category == "horror":
            return "Not allowed"
        return 5.0
    
    elif age <= 60:
        match category:
            case "action":
                return 12.0
            case "comedy":
                return 10.0
            case "horror":
                return 15.0
            case _:
                return "Unknown category"
            
    else:
        match category:
            case "action":
                return 12.0 * 0.5
            case "comedy":
                return 10 * 0.5
            case "horror":
                return 15 * 0.5
            case _:
                return "Unknown category"
            

def main():
    print("Welcome to our cinema")
    name = input("What's your name? ").strip().title()
    print(f"Hello, {name}!")
    age = get_age()
    category = input("Choose a movie genre(horror/comedy/action): ").strip().lower()

    price = get_ticket_price(age, category)


    print("\n" + "-" * 40)
    print("TICKET INFORMATION:")
    print(f"    Name:        {name}")
    print(f"    Age:         {age}")
    print(f"    Movie genre: {category.capitalize()}")
    print("-" * 40)

    if price == "Not allowed":
        print("Sorry, children are not allowed in ""horror"" movies")
    elif price == "Unknown category":
        print("This type of movie doesn't exist.")
    else:
        print(f"TICKET PRICE: ${price:.2f}")

    

if __name__ == "__main__":
    main()