def hello(to="World"):    
    print("Hello,", to + "!")

hello() 
name = input("What's your name? ").strip().title()
hello(name)
