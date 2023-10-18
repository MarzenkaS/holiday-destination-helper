import math


def selecting_a_season():
    """
    Collecting data from users regarding preferred season for holiday
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
        print('Please try again and enter correct word')


selecting_a_season()


def summer_temp_choice():
    """
    Collecting user choice for temperature
    """
    hot = "below"
    hotter = "above"
    print('What weather are you interested in? Below or above 30 degrees\n')
    user_answer = input('Please enter your answer here by using one word:')
    if user_answer == hot:  
        print()
    elif user_answer == hotter:
        print()  
    else:
        print('Please try again and enter correct word')


summer_temp_choice()    
    