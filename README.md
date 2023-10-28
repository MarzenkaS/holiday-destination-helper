# HOLIDAY DESTINATION HELPER APP

I created the Holiday Destination Helper app for people who need help choosing a vacation destination.
Following the questions in app, at the end user wil see suggested holiday destination based on their responses.

![Different screen sizes](https://github.com/MarzenkaS/holiday-destination-helper/blob/main/docs/screens.png?raw=true)
[Live version of app you can find here](https://holiday-destination-helper-790434daa39e.herokuapp.com/)

## FEATURES
### Existing Features

1. _Start_

The application consists of questions. First, the user must answer the question whether he wants to travel in the summer or winter season.
![start game](https://github.com/MarzenkaS/holiday-destination-helper/blob/main/docs/start.game.png?raw=true)

2. _Running game_

The next questions also have several options for the user to choose from. Options and answers are displayed.
![running game](https://github.com/MarzenkaS/holiday-destination-helper/blob/main/docs/running.game.png?raw=true)

3. _Wrong input_

If the user enters the answer incorrectly, the application will display a message to correct the answer.
![wrong input](https://github.com/MarzenkaS/holiday-destination-helper/blob/main/docs/wrong.input.png?raw=true)

4. _End of game_

After displaying the proposed holiday destinations, the user will be asked whether he wants to leave or stay in the application.
![end of game](https://github.com/MarzenkaS/holiday-destination-helper/blob/main/docs/end.game.png?raw=true)


### Future Features

Later, I would like to increase the number of questions to better match the holiday destination to the user's preferences.


## TESTING

I have tested my project on https://pep8ci.herokuapp.com/

### Bugs

- I had some bugs you can see below. Most of them concerned whitespaces, trailing whitespace and often lines of code were too long.
![bugs](https://github.com/MarzenkaS/holiday-destination-helper/blob/main/docs/bugs.png?raw=true)

- I fixed them and there were no errors.
![no errors](https://github.com/MarzenkaS/holiday-destination-helper/blob/main/docs/nobugs.png?raw=true)

## DEPLOYMENT

My project was deployed using Code Institute's mock terminal for Heroku.

Steps for deployment:
- create an account on [Heroku](https://heroku.com)
- create a new Heroku app
- we give an unique name for the app
- we go to settings tab and there is config vars where we write PORT as a key and 8000 as a value
- next we go to buildpack and we add Python as a first one and node.js as a second one and we save changes
- we go to deploy section and we connect to Github
- below we search for our Github repository name and we click connect to link up our Heroku app to our Github repository code 
- last step is to scroll down and we can set up automatic deploys choose manually deploy

## CREDITS

- Before starting to create the application, I used the website [draw.io](draw.io) to plan the structure of the application.
![plan](https://github.com/MarzenkaS/holiday-destination-helper/blob/main/docs/plan.png?raw=true)

- Code Institute for the deployment terminal.

For solving problems with code I used 
1. [chataigpt.org](https://chataigpt.org/)
2. [stackoverflow.com](https://stackoverflow.com/)
3. [pep8ci.herokuapp.com](https://pep8ci.herokuapp.com/)