# Program that enables a user to place an order, prompting them for items, one per line,
# until the user inputs control-d (which is a common way of ending one’s input to a program)

felipes_dict = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total = float()

while True:
    try:
        # Prompt the user to place an order
        item = input("Input your chousen item: ").title()
        try:
            if felipes_dict[item]:
                to_add = float(felipes_dict[item])
                total = total + to_add
            print(f"Total: ${total:.2f}")
        except:
            continue
    except EOFError:
        print()
        break

