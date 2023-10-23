import math


def selecting_a_season():
    """
    Collecting data from users regarding preferred season for holiday.
    """
    warm_choice = "summer"
    cold_choice = "winter"
    print('Are you interested in a holiday in the summer or winter season?\n')
    user_answer = input('Please enter your answer here by using one word:')
    if user_answer == warm_choice:
        print()
    elif user_answer == cold_choice:
        print()
    else:
        print('Please try again and enter correct word!')


selecting_a_season()


# def summer_season():
def summer_temp_choice():
    """
    Collecting user choice for temperature.
    """
    hot = "below"
    hotter = "above"
    print('What weather are you interested in? Below or above 30 degrees?\n')
    user_answer = input('Please enter your answer here by using one word:')
    if user_answer == hot:
        print()
    elif user_answer == hotter:
        print()
    else:
        print('Please try again and enter correct word!')


summer_temp_choice()


def temp_below_activities():
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


temp_below_activities()


def temp_above_activities():
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


temp_above_activities()
