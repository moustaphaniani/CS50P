def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    # TODO
    dollars = round(float(d.replace('$', '')), 2)
    return dollars

def percent_to_float(p):
    # TODO
    percent = round(float(p.replace('%', ''))/100, 2)
    return percent

main()
