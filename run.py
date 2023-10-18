import math


def selecting_a_season():
    """
    Collecting data from users regarding preferred season for holiday
    """
    cold_choice = "winter"
    warm_choice = "summer"
    print('Are you interested in a holiday in the summer or winter season?\n')
    user_answer = input('Please enter your answer here by using one word:')
    if user_answer == cold_choice:
        print(user_answer)
    elif user_answer == warm_choice:
        print(user_answer)
    else:
        print('Please try again and enter correct word')


selecting_a_season()
