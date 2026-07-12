
# Ask user for their name
name = input("What's your name? ").strip().title()

#Split the name into first and last name
first, last = name.split()

#Remove whitespace from the name and uppercase the first letter of each word in the name
#name = name.strip().title()

#Uppercase the first letter of the name
#name = name.capitalize()

#Uppercase the first letter of each word in the name
#name = name.title()

#Say hello to the user
print(f"Hello, {first}! ")

