def main():
    try:
        # Prompt the user for a fraction, formatted as X/Y
        fraction = input("Input the fraction: ")
        if '/' in fraction:
            print(fraction, type(fraction))
            fraction_value = convert(fraction)
            print(fraction_value, type(fraction_value))
            print(gauge(fraction_value))
            exit()
        else:
            raise ValueError
    except (ValueError, ZeroDivisionError):
        True


def convert(text):
    try:
        expresion = text.split('/')
        if int(expresion[1]) == 0:
            raise ZeroDivisionError
        elif int(expresion[1]) >= int(expresion[0]):
            compute = int(expresion[0]) / int(expresion[1])
            return int(compute * 100)
        raise ValueError
    except:
        exit()

def gauge(compute):
        if compute <= 1:
            result = "E"
        elif compute >= 99:
            result = "F"
        else:
            result = str(compute) + '%'
        return result


if __name__ == "__main__":
    main()
