grocery_dict = {}

while True:
    try:
        # Prompt the user for items, one per line, until the user inputs control-d
        #item = input("What item should be added to the list? ").upper()
        item = input().upper()
        try:
            if item in grocery_dict:
                grocery_dict[item] = grocery_dict[item] + 1
            else:
                grocery_dict[item] = 1
        except KeyError:
            continue
    except EOFError:
        print()
        sorted_dict = dict(sorted(grocery_dict.items()))
        for item in sorted_dict:
            print(sorted_dict[item], item)
        break
