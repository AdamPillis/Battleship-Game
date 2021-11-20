# [Battleship Voyage](https://battleship-voyage.herokuapp.com/)

## 1. **Introduction**

### **What is Battleship Voyage?**
Battleship voyage is a CLI or Command Line Interface program which connects the user with the computer to play a game of Battleships in its simplest form. 
[Click on me to view full game rules](https://www.thesprucecrafts.com/the-basic-rules-of-battleship-411069)
- This program allows the user to chose the size of each play board as well as the number of ships, hence rounds to be played. 
- Numbers are validated to be between 5 and 10 to allow each user to chose the level of difficulty of their game. i.e highest size and lowest number of ships. 

The overall **Project Aim** was to design an interactive game using a back-end computer language, like Python. The program requests user input throughout the game from start to finish. Time library, *time.sleep(),* was used to pause at certain sections to enhance the game workflow while adding fun when the player needs to wait several seconds before realising whether they hit a ship or not. After each round, a user input offers the user the option to continue or quit the game if they so wish. 
Given the limited numbers between 5 and 10, the minimum number of rounds are 5 and maximum 10 to prevent users from getting uninterested.

### **How it works?**

1. The first CLI interaction between the program and the user is a **Welcome Message** followed by an input asking the user to enter a *name*. 

2. Once a name has been entered, the game rules are shown with time delay to ensure the user has no choice but to read the rules which is vital to fully enjoy the game. 

3. The user is then asked to input a number for rows and cols followed by the number of ships which will dictate the number of rounds. 

4. The game starts by populating both boards, identifying user's ship co-ordinates while hiding computers. 

5. Each round requests a row and col input from the user and using time delay, provide an answer and show scores at the end of each round.

6. Every round starts by the user pressing **Enter** and the game remains in loop until the number of guesses equal to the number ships, hence number of rounds. 

7. At the end, a *specific* feedback message is given to the user with a final updated board and offers the user to press a key to play again or quit after one game.

### **Who is it for?**
The original game was released in 1967 which indicates that the older generation would recognise the game be able to play as well as children from the age of 5 and over.

**New User** : Every new user has the ability to play as many games as they wish because the developer used random number to create ship co-ordinates and computer guesses. Rounds vary from 5 and 10 to ensure that each game isn't too short but not too long either.

**Returning User** : As mentioned above, every player has the ability to play unlimited number of games which means as a returning user, the only possible difference is the name input at the very start.