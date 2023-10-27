import math


def welcome_screen():
    """
    Introduction and description of the application.
    """
    print('Welcome to the Holiday Destination Helper App.\n' +
          'If you are wondering where you want to spend\n' +
          'your holiday, this app is made for you.\n'
          'Just please follow the questions and at the end\n' +
          'you will see suggested holiday destinations.\n' +
          'Enjoy!')


def selecting_a_season():
    """
    Collecting data from users regarding preferred season for holiday.
    """
    warm_choice = "summer"
    cold_choice = "winter"
    print('Are you interested in a holiday in: the summer or winter season?\n')
    print('1: the summer season.\n')
    print('2: the winter season.\n')

    while (True):
        user_answer = input('Please enter your choice 1 or 2:\n')
        if user_answer == "1":
            print(warm_choice)
            temp_choice(warm_choice)
        elif user_answer == "2":
            print(cold_choice)
            temp_choice(cold_choice)
        else:
            print('Incorrect input please enter 1 for summer and 2 for winter')


# def summer_season():
def temp_choice(season):
    """
    Collecting user choice for temperature.
    """
    # cooler = "below"
    # warmer = "above"
    if season == "summer":
        print('What weather are you interested in? ' +
              'Below or above 30 degrees?\n')
        print('1 : cooler\n')
        print('2 : warmer\n')
    elif season == "winter":
        print('Are you looking for an exotic place or with snow?\n')
        print('1 : exotic\n')
        print('2 : with snow.\n')

    while ("summer"):
        user_answer = input('Please enter your option from above (1/2):\n')
        if user_answer == "1":
            print(temp_cooler_activities())
        elif user_answer == "2":
            print(temp_warmer_activities())
        else:
            print('Please try again and enter correct option (1/2):')


# temp_choice()


def temp_cooler_activities():
    """
    Collecting data from user about preferred activities 
    in summer season with cooler temperature.
    Suggestions of holiday destinations selected based on
    data entered by the user.
    """
    first = "visiting city"
    second = "water activities"
    third = "hiking"
    print('Which activities interest you the most?')
    print('First: visiting city(v),\n'
          'second: water activities(w),\n'
          'third: hiking(h).\n')
    user_answer = input('Please enter your answer here (v/w/h):\n')
    if user_answer == "v":
        print(first)
        print('The best would be to visit Poland, Germany, ' +
              'Austria and Czech Republic.')
    elif user_answer == "w":
        print(second)
        print('Good idea is to travel to Poland, Germany or France.')
    elif user_answer == "h":
        print(third)
        print('The best places for hiking you will find in Austria, ' +
              'Switzerland, Slovakia, Germany, Poland.\n')
    else:
        print('Please try again and enter correct word!')


# temp_cooler_activities()


def temp_warmer_activities():
    """
    Collecting data from user about preferred activities
    in summer season with warmer temperature.
    Suggestions of holiday destinations selected based on
    data entered by the user.
    """
    first = "visiting city"
    second = "water activities"
    third = "hiking"
    print('Which activities interest you the most?')
    print('First: visiting city(v),\n'
          'second: water activities(w),\n'
          'third: hiking(h).\n')
    user_answer = input('Please enter your answer here (v/w/h):')
    if user_answer == "v":
        print(first)
        print('The best would be to visit Spain, Italy, ' +
              'Greece or France.')
    elif user_answer == "w":
        print(second)
        print('How about Cyprus, Spain, Italy, Greece, Maldives or Zanzibar.')
    elif user_answer == "h":
        print(third)
        print('The best places for hiking you will find in, ' +
              'Italy, Spain or France.')
    else:
        print('Please try again and enter correct word!')


# temp_warmer_activities()

def exotic_activities():
    """
    Collecting data from user about preferred activities
    in exotic place.
    Suggestions of holiday destinations selected based on
    data entered by the user.
    """
    first = "visiting city"
    second = "water activities"
    print('Which activities interest you the most?')
    print('First: visiting city(v),\n'
          'second: water activities(w).)
    user_answer = input('Please enter your answer here (v/w):')
    if user_answer == "v":
        print(first)
        print('The best would be to visit Thailand, Australia\' +
              'Mexico or Brazil.')
    elif user_answer == "w":
        print(second)
        print('How about Australia, Zanzibar, Cuba or Domenican Rep.')
    else:
        print('Please try again and enter correct word!')










welcome_screen()
selecting_a_season()
