# **Revforum**

## **Overview**

Revforum is an online forum made with Django framework. It allows people with their shared love for motorcycle to exchange options and experiences. On categories created by the admin, the users can create their own posts and comment on posts made by themselves or others. They can also like, favourite and report posts. When the post is reported, it is flagged for the admin to analyse.

![Main screen screenshot]()

## Table of contents

- [**Revforum**](#revforum)
  - [**Overview**](#overview)
  - [Table of contents](#table-of-contents)
  - [**Planning stage**](#planning-stage)
    - [**Target Audiences:**](#target-audiences)
    - [**User Stories:**](#user-stories)
    - [**Site Aims:**](#site-aims)
    - [**Forum Structure:**](#forum-structure)
  - [**Current Features**](#current-features)
      - [*Main Screen:*](#main-screen)
      - [*Post List screen:*](#post-list-screen)
      - [*Post screen:*](#post-screen)
      - [*Game:*](#game)
      - [*Congratulations and Game Over:*](#congratulations-and-game-over)
  - [**Future-Enhancements**](#future-enhancements)
  - [**Testing Phase**](#testing-phase)
  - [**Validators**](#validators)
  - [**Bugs**](#bugs)
  - [**Deployment**](#deployment)
  - [**Tech**](#tech)
  - [**Credits**](#credits)
    - [**Honorable mentions**](#honorable-mentions)
    - [**Content:**](#content)

## **Planning stage**

### **Target Audiences:**

* Users interested in motorcycles.
* Users interested in interact with other people with shared loved for motorcycles.
* Users interested in share their experiences.
​

### **User Stories:**

* As a user, I want to make a post.
* As a user, I want to comment a post.
* As a user, I want to update a post.
* As a user, I want to delete a post.
* As a user, I want to like a post.
* As a user, I want to report a post.
* As a user, I want to update a comment.
* As a user, I want to delete a comment.
* As an administrator, I want to create a category.
* As an administrator, I want to review a flagged post.
​

### **Site Aims:**

* To create a space for conversation regarding motorcycles.
* To present itself as another option for users to get and share information.
* To incentivate discussions.
* To facilitate the spread of information, specially regarding events or similar.
* To provide an excellent user experience without any errors or bugs.

### **Forum Structure:**

![Forum Structure]()

## **Current Features**

​

#### *Main Screen:*

* Main screen of the forum. User or visitors (they do not have to be logged) can see the categories.

![Main screen screenshot]()

#### *Post List screen:*

* Once the user/visitor clicks in one category, they are then redirected to all the posts inside that category. If the user is logged, the page shows the favourite posts first, from the newest to the last one.

![Post List screenshot]()

#### *Post screen:*

* When the user clicks the post, they are presented with: the title, the description, who made it, when it was made, when the last update was made (if there was), the possibility to like, comment and report.

![Post screenshot]()

#### *Game:*

* The game starts with three main parts: the hangman design (empty, because there is no mistakes yet), the random word hidden and the request for the user to guess a letter. Once the user guesses the first letter, two more items are added to the game: the used letters lists (so the user can see which letters they already guessed) and the amount of mistakes they made.

![Game screenshot 1](assets/images-docs/game_screenshot_1.png)

![Game screenshot 2](assets/images-docs/game_screenshot_2.png)

![Game screenshot 3](assets/images-docs/game_screenshot_3.png)

#### *Congratulations and Game Over:*

* There is two outcomes of the game: the user can either win or lose. If they win, they are greeted with a congratulations message and an invitation to play again. If the user loses, they receive a Game Over message, the information of what was the word and also the invitation to replay the game.

![Congratulations screenshot](assets/images-docs/congrats_screenshot.png)

![Game Over screenshot](assets/images-docs/game_over_screenshot.png)

​

## **Future-Enhancements**

​

* Color could be added to the game to enhance the user experience.
* Store the game on a server so the game could be played online without a necessity of a terminal.
​

## **Testing Phase**

​

Implementation: Main screen offers the user the option to play the game.

Test: Access the game and pressed the correct option to start the game.

Result: Game started.
***

Implementation: Prevent user of typing wrong keys while starting the game.

Test: Tried wrong keys as input.

Result: Game informs that the keys are incorrect and did not started.
***

Implementation: Offer the user the option to exit the game in the main screen.

Test: Typed "exit" on the main screen.

Result: Game finished.
***

Implementation: Once the game starts, user can choose the difficulty.

Test: Tried the correct inputs and wrong ones.

Result: The correct ones allowed the game to start with the parameters considered for the chosen level, wrong keys did not allow the game to start.
***

Implementation: Once the game starts, the user can choose one letter.

Test: Started the game and guessed a word.

Result: Game continued.
***

Implementation: Prevent user to type a full word or numbers.

Test: Typed a random words and numbers.

Result: Game informed that those inputs were not accepted and requested user to type just a letter.
***

Implementation: Game allows to user to make five wrong guesses before finishing the game.

Test: Made five wrong guesses.

Result: On the sixth wrong guess, the game finished.
***

Implementation: Allow user to finish the game at any moment during the game, typing "exit".

Test: Typed "exit" during the game.

Result: Game finished.
***

Implementation: Allow user to replay the game when the game finishes.

Test: Finished the game, losing and winning, and tried to replay the game.

Result: Game rebooted.
***

Implementation: Allow user to exit the game when the game finishes.

Test: Finished the game, losing and winning, and tried to exit the game.

Result: Exited the game.
***

## **Validators**

. Python Linter [Python Linter Validator](https://pep8ci.herokuapp.com/)

Only error related to the ASCII graphics (W605)
![Python Linter Validator screenshot - run.py](assets/images-docs/run_py_python_linter.png)

![Python Linter Validator screenshot - words.py](assets/images-docs/words_py_python_linter.png)

## **Bugs**

Problem 🐞: Game continued even after six wrong guesses.

Cause🛠: The input code was running twice within the while loop.

Resolution✅: Removed the unnecessary input call.
***

Problem 🐞: If a incorrect key was used to chose the difficulty the game was rebooted.

Cause🛠: The function being called was wrong.

Resolution✅: Change the structure of the function and the function being called.
***

Problem 🐞: Start game function entering a loop without continuing the game.

Cause🛠: The conditions for the while loop where not considered because of the logic applied.

Resolution✅: Change the condition from OR to AND.
***

Problem 🐞: Endgame function was breaking the game.

Cause🛠: Since the function is the base to the end, either winning or losing, another parameter was necessary to differentiate.

Resolution✅: A second parameter was added to run the function.
***

Problem 🐞: Used letters list was being printed with brackets.

Cause🛠: The print statement was not being called with the correct commands.

Resolution✅: Correct commands added.
***

## **Deployment**

I deployed the application on Heroku via the following procedure: -
​

1. Push the code to the Github [repository](https://github.com/AlexDralur/hangman-game-python).
2. Log in or sign up to Heroku where you need to create a new app.
3. Select a unique name.
4. In the settings tab reveal the config vars, for this project one had to be added per Code Institutes guidance.
5. For KEY, input PORT and for VALUE, input 8000 and click add.
6. Below that, click add buildpack, select Python and save.
7. Click add buildpack again, now select Nodejs and save.
8. Python should be above Nodejs on the buildpack list.
9. Go to deploy tab and for deployment method select GitHub and connect your GitHub account.
10. When prompted enter the repository you want to deploy, search and once found connect it.
11. Now you can either set it automatically or manually deploy the appropriate branch.
12. Automatically will deploy the app everytime you push something to GitHub.
13. Manually you have control over when the app should be deployed, but you have to remember to do it.
14. It might take a little while, but once the app is built Heroku will have a link to the live web page.

You can find the game live via the following URL - [live game](https://hangman-alexander-78ba1ad29a14.herokuapp.com/)
***
​

## **Tech**

- Python.
​

## **Credits**

### **Honorable mentions**

* Larissa Moura (my wife) - She was my tester and also my design guru.
* Richard Wells (my Code Institute tutor) - Help me throughout the project in all aspects.
​

### **Content:**

* Words taken from the words.txt [Github](https://github.com/Xethron/Hangman) from Xethron.
* Word Graphics (ASCII art) taken from [TextKool](https://textkool.com/en)
* Code to run through the hidden word and only the letter which was guessed, if correct, from the Python tutorial [Youtube](https://www.youtube.com/watch?v=m4nEnsavl6w) from Kite.
