def add(a, b):
    answer = a + b
    print(str(a) + "+" + str(b) + "=" + str(answer) + "\n")

def sub(a, b):
    answer = a - b
    print(str(a) + "-" + str(b) + "=" + str(answer) + "\n")

def mul(a, b):
    answer = a * b
    print(str(a) + "*" + str(b) + "=" + str(answer) + "\n")

def div(a, b):
    answer = a / b
    print(str(a) + "/" + str(b) + "=" + str(answer) + "\n")


while True:
    print("A. Addition")
    print("B. Substraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit")

    choice = input("Input your choice: ")

    if choice == "A" or "a":
        print("Addition")
        a = int(input("Input first number: "))
        b = int(input("input second number: "))
        add(a, b)
    elif choice == "B" or "b":
        print("Substraction")
        a = int(input("Input first number: "))
        b = int(input("Input second number: "))
        sub(a, b)
    elif choice == "C" or "c":
        print("Multiplication")
        a = int(input("Input first number: "))
        b = int(input("Input secoond number: "))
        mul(a, b)
    elif choice == "D" or "d":
        print("Division")
        a = int(input("Input first number: "))
        b = int(input("Input second number: "))
        div(a, b)
    elif choice == "E" or "e":
        print("Program ended")
        quit()




     


#print options to the user
#ask for values
#call the functions
#w while loop to continue the program untill the user wants to exit

