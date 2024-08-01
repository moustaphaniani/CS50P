def convert(time):

    if time.endswith('a.m.') or time.endswith('p.m.'):
        user_hour, meridian = time.split(' ')
        hours, minutes = user_hour.split(':')

        if meridian == 'p.m.':
            time_to_add = 12
        else:
            time_to_add = 0

        conversion = time_to_add + int(hours) + int(minutes)/60
        return conversion

    else:
        hours, minutes = time.split(':')
        conversion = int(hours) + int(minutes)/60
        return conversion

def main():

    # Prompts the user for a time and output whether it’s breakfast time, lunch time, or dinner time
    user_time = input("What time is it? (in 24:00 hour format -> #:## and ##:## OR in 12:00 hour format -> #:## a.m. and #:## p.m.) ")

    # Logic
    '''
    Suppose that you’re in a country where it’s customary to eat breakfast between 7:00 and 8:00,
    lunch between 12:00 and 13:00, and dinner between 18:00 and 19:00.
    Wouldn’t it be nice if you had a program that could tell you what to eat when?

    If it’s not time for a meal, don’t output anything at all.
    Assume that the user’s input will be formatted in 24-hour time as #:## or ##:##.
    And assume that each meal’s time range is inclusive.
    For instance, whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime in between, it’s time for breakfast.
    '''

    input_time = convert(user_time)

    if input_time >= 7 and input_time <= 8:
        print("Breakfast time")
    elif input_time >= 12 and input_time <= 13:
        print("Lunch time")
    elif input_time >= 18 and input_time <= 19:
        print("Dinner time")

if __name__ == "__main__":
    main()
