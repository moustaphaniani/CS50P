def calculation(text):
    expresion = text.split('/')
    if int(expresion[1]) >= int(expresion[0]):
        compute = int(expresion[0]) / int(expresion[1])
        if compute <= 0.01:
            result = "E"
        elif compute >= 0.99:
            result = "F"
        else:
            diposit = int(100 * compute)
            result = str(diposit) + '%'
        return result
    else:
        raise ValueError


while True:
    try:
        # Prompt the user for a fraction, formatted as X/Y
        fraction = input("Input the fraction: ")
        if '/' in fraction:
            print(calculation(fraction))
            break
    except (ValueError, ZeroDivisionError):
        True
