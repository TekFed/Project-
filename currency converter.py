print("This is a currency converter program. Pls select an option below.")
print()
conv_opt = input("A. USD ~ NGN or B. NGN ~ USD: ")

def to_USD():
    
    naira = eval(input("Enter amount in naira: "))
    dollars = convert_to_usd(naira)

    print("That is", dollars, "dollars.")

convert_to_usd = lambda naira: naira * 0.0022

def to_naira():

    dollars = eval(input("Enter amount in dollars: "))
    naira = convert_to_naira(dollars)

    print("That is", naira, "naira.")

convert_to_naira = lambda dollars: dollars * 460.42

if conv_opt == "A".lower():
    to_naira()
elif conv_opt == "B".lower():
    to_USD()
else:
    print("Invalid option.")
    quit()
