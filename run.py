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
    season_selected = True
    while (season_selected):
        user_answer = input('Please enter your choice 1 or 2:\n')
        if user_answer == "1":
            print(warm_choice)
            season_selected = False
            temp_choice(warm_choice)
        elif user_answer == "2":
            print(cold_choice)
            season_selected = False
            temp_choice(cold_choice)
        else:
            print('Incorrect input please enter 1 for summer and' +
                  '2 for winter.\n')


def temp_choice(season):
    """
    Collecting user choice for temperature.
    """
    if season == "summer":
        print('What weather are you interested in? ' +
              'Cooler below or warmer above 30 degrees?\n')
        print('1 : cooler\n')
        print('2 : warmer\n')
    elif season == "winter":
        print('Are you looking for an exotic place or with snow?\n')
        print('1 : exotic\n')
        print('2 : with snow.\n')

    temp_selected = True
    user_answer = input('Please enter your option from above (1 or 2):\n')

    while (season == "summer" and temp_selected):
        if user_answer == "1":
            temp_selected = False
            temp_cooler_activities()
        elif user_answer == "2":
            temp_selected = False
            temp_warmer_activities()
        else:
            user_answer = input('Please try again and enter' +
                                'correct option (1 or 2):\n')

    while (season == "winter" and temp_selected):
        if user_answer == "1":
            temp_selected = False
            exotic_activities()
        elif user_answer == "2":
            temp_selected = False
            with_snow_activities()
        else:
            user_answer = input('Please try again and enter correct' +
                                'option (1 or 2):\n')


def temp_cooler_activities():
    """
    Collecting data from user about preferred activities
    in summer season with cooler temperature.
    Suggestions of holiday destinations selected based on
    data entered by the user.
    """
    FIRST = "visiting city"
    SECOND = "water activities"
    THIRD = "hiking"
    choice = True
    while (choice):
        print('Which activities interest you the most?')
        print(f'Option 1: {FIRST}.\n'
              f'Option 2: {SECOND}.\n'
              f'Option 3: {THIRD}.\n')
        user_answer = input('Please enter your answer here (1, 2 or 3):\n')
        if user_answer == "1":
            print(f"You chose {FIRST}")
            print('The best would be to visit Poland, Germany,' +
                  'Austria and Czech Republic.')
            choice = False
            repeat()
        elif user_answer == "2":
            print(f"You chose {SECOND}")
            print('Good idea is to travel to Poland, Germany or France.')
            choice = False
            repeat()
        elif user_answer == "3":
            print(f"You chose {THIRD}")
            print('The best places for hiking you will find in Austria,' +
                  'Switzerland, Slovakia, Germany, Poland.')
            choice = False
            repeat()
        else:
            print('Please try again and enter correct word!')


def temp_warmer_activities():
    """
    Collecting data from user about preferred activities
    in summer season with warmer temperature.
    Suggestions of holiday destinations selected based on
    data entered by the user.
    """
    FIRST = "visiting city"
    SECOND = "water activities"
    THIRD = "hiking"
    choice = True
    while (choice):
        print('Which activities interest you the most?')
        print(f'Option 1: {FIRST}.\n'
              f'Option 2: {SECOND}.\n'
              f'Option 3: {THIRD}.\n')
        user_answer = input('Please enter your answer here (1, 2 or 3):\n')
        if user_answer == "1":
            print(f"You chose {FIRST}")
            print('The best would be to visit Spain, Italy,' +
                  'Greece or France.')
            choice = False
            repeat()
        elif user_answer == "2":
            print(f"You chose {SECOND}")
            print('How about Cyprus, Spain, Italy, Greece, Maldives' +
                  'or Zanzibar.')
            choice = False
            repeat()
        elif user_answer == "3":
            print(f"You chose {THIRD}")
            print('The best places for hiking you will find in' +
                  'Italy, Spain or France.')
            choice = False
            repeat()
        else:
            print('Please try again and enter correct word!\n')


def exotic_activities():
    """
    Collecting data from user about preferred activities
    in winter season in exotic places.
    Suggestions of holiday destinations selected based on
    data entered by the user.
    """
    FIRST = "visiting city"
    SECOND = "water activities"
    choice = True
    while (choice):
        print('Which activities interest you the most?')
        print(f'Option 1: {FIRST}.\n'
              f'Option 2: {SECOND}.\n')
        user_answer = input('Please enter your answer here (1 or 2):\n')
        if user_answer == "1":
            print(f"You chose {FIRST}")
            print('The best would be to visit Thailand, Australia' +
                  'Mexico or Brazil.')
            choice = False
            repeat()
        elif user_answer == "2":
            print(f"You chose {SECOND}")
            print('How about Australia, Zanzibar, Cuba or Domenican Rep.')
            choice = False
            repeat()
        else:
            print('Please try again and enter correct word!\n')


def with_snow_activities():
    """
    Collecting data from user about preferred activities
    in winter season in snowy places.
    Suggestions of holiday destinations selected based on
    data entered by the user.
    """
    FIRST = "spa, saunas, thermal baths"
    SECOND = "visiting cities, Christmas Markets"
    THIRD = "skiing, snowboard"
    choice = True
    while (choice):
        print('Which activities interest you the most?')
        print(f'Option 1: {FIRST}.\n'
              f'Option 2: {SECOND}.\n'
              f'Option 3: {THIRD}.\n')
        user_answer = input('Please enter your answer here (1, 2 or 3):\n')
        if user_answer == "1":
            print(f"You chose {FIRST}")
            print('The best would be to go to France, Italy,' +
                  'Germany or Hungary.')
            choice = False
            repeat()
        elif user_answer == "2":
            print(f"You chose {SECOND}")
            print('How about Poland, Germany or Czech Republic.')
            choice = False
            repeat()
        elif user_answer == "3":
            print(f"You chose {THIRD}")
            print('The best places for skiing and snowboard' +
                  'you will find in Italy, Germany, France' +
                  'Austria and Switzerland')
            choice = False
            repeat()
        else:
            print('Please try again and enter correct word!\n')


def repeat():
    repeat = True
    while (repeat):
        again = input("Would you like to try again? (y/n):")
        if again == "y":
            repeat = False
            selecting_a_season()
        elif again == "n":
            repeat = False
            print("Thank you for using our app.")
        else:
            print("Please enter correct option (y/n):")


welcome_screen()
selecting_a_season()
