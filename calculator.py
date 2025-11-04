# simple calculator
def add(x,y):
    return x + y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    if y != 0:
        return x/y
    else:
        return "Error: Cannot divide by zero"

def calculator():
   

    while True:
        print("\nOptions: add | subtract | multiply | divide | quite")  
        choice = input("Choose an operation").lower()

        if choice == "quite":
            print("Goodbye!")
            break
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))  
        
        if choice == "add":
            print("Result: ", add(x,y))
        elif choice == "subtract":
            print("Result: ", subtract(x,y))
        elif choice == "multiply":
            print("Result: ", multiply(x,y))
        elif choice == "divide":
            print("Result: ", divide(x,y))
        else:
            print("Invalid option")      
           

calculator()



