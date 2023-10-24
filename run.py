import math


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
        user_answer = input('Please enter your choice 1 or 2:')
        if user_answer == "1":
            print(warm_choice)
            temp_choice(warm_choice)
        elif user_answer == "2":
            print(cold_choice)
            temp_choice(cold_choice)
        else:
            print('Incorrect input please enter 1 for summer and 2 for winter')


# selecting_a_season()


# def summer_season():
def temp_choice(season):
    """
    Collecting user choice for temperature.
    """
    cooler = "below"
    warmer = "above"
    if season == "summer":
        print('What weather are you interested in?' +
              'Below or above 30 degrees?\n')
        print('1 : cooler.\n')
        print('2 : warmer.\n')
    elif season == "winter":
        print('What weather are you interested in?' +
              'Below or above 0 degrees?\n')
        print('1 : cooler.\n')
        print('2 : warmer.\n')

    while (True):
        user_answer = input('Please enter your option from above (1/2):')
        if user_answer == "1":
            print(temp_cooler_activities(season, cooler))
        # temp_cooler_activities(season, cooler)
        # < = Either pass with parameters and change function to activities
        elif user_answer == "2":
            print(temp_warmer_activities())
        # temp_warmer_activities() <= or keep same
        # but end whileloop by calling next function
        else:
            print('Please try again and enter correct option (1/2)')


temp_choice(temp_cooler_activities(), temp_warmer_activities())


def temp_cooler_activities():
    """
    Collecting data from user about preferred activities.
    Suggestions of holiday destinations selected based on
    data entered by the user.
    """
    first = "visiting city"
    second = "water activities"
    third = "hiking"
    print('Which activities interest you the most?')
    print('First: visiting city, second: water activities, third: hiking.\n')
    user_answer = input('Please enter your answer here:')
    if user_answer == first:
        print('The best would be to visit Poland, Germany,' +
              'Austria and Czech Republic.')
    elif user_answer == second:
        print('Good idea is to travel to Poland, Germany or France.')
    elif user_answer == third:
        print('The best places for hiking you will find in Austria,' +
              'Switzerland, Slovakia, Germany, Poland.\n')
    else:
        print('Please try again and enter correct word!')


# temp_cooler_activities()


def temp_warmer_activities():
    """
    Collecting data from user about preferred activities.
    Suggestions of holiday destinations selected based on
    data entered by the user.
    """
    first = "visiting city"
    second = "water activities"
    third = "hiking"
    print('Which activities interest you the most?')
    print('First: visiting city, second: water activities, third: hiking.\n')
    user_answer = input('Please enter your answer here:')
    if user_answer == first:
        print('The best would be to visit Spain, Italy,' +
              'Greece or France')
    elif user_answer == second:
        print('How about Cyprus, Spain, Italy, Greece, Maldives or Zanzibar')
    elif user_answer == third:
        print('The best places for hiking you will find in,' +
              'Italy, Spain or France')
    else:
        print('Please try again and enter correct word!')


# temp_warmer_activities()
