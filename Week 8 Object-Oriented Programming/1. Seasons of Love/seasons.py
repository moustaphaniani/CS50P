import inflect
from datetime import date, datetime
import sys

p = inflect.engine()


def main():
    #birth = input("Whats your birth date? (YYYY-MM-DD) ")
    print(calculate(input("Whats your birth date? (YYYY-MM-DD) ")).capitalize(), 'minutes')


def calculate(day):
    try:
        if date.fromisoformat(day):
            now = date.today()
            day = datetime.strptime(day, '%Y-%m-%d').date()
            if day < now:
                timedelta = now - day
                return p.number_to_words(24*60*timedelta.days, andword="")
            else:
                sys.exit(1)
        else:
            sys.exit(1)
    except:
        sys.exit(1)


if __name__ == "__main__":
    main()
