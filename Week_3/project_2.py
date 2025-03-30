def calculate_atr(experience, age):
    """Calculate the Annual Tax Revenue (ATR) based on experience and age."""
    if experience > 25 and age >= 55:
        return 5_600_000
    elif experience > 20 and age >= 45:
        return 4_480_000
    elif experience > 10 and age >= 35:
        return 1_500_000
    else:
        return 550_000

print("Welcome to Izifin Technology's ATR Calculator \n")

while True:
    option = int(input("""
Choose an action:
1. Calculate staff Annual Tax Revenue (ATR)
2. End program
"""))

    if option == 2:
        print("Exiting program. Goodbye!")
        break

    years_of_exp = int(input("Enter staff years of experience: "))
    age = int(input("Enter staff age: "))

    atr = calculate_atr(years_of_exp, age)

    print(f"Staff with {years_of_exp} year(s) of experience and aged {age} has N{atr:,} ATR\n")