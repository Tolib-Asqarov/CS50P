"""
x= float(input("Enter a number: "))   
y= float(input("Enter another number: "))
#x= input("Enter a number: ")
#y= input("Enter another number: ")   
#z= int(x)+int(y)
#print(round(x+y)) 

#z= round(x+y)
#print(f"{z:,}")          

z=x/y
print(f"{z:.3f}")

"""

from numpy import square


def main():
    x=int(input("Enter a number: "))
    print( x, "squared is", square(x))

main()  