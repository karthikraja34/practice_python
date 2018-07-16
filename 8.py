# Rock Paper Scissors

""" 

Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock
 """

while True:
    input1 = raw_input("Player 1 : Enter Rock ,Paper or Scissors : ")
    input2 = raw_input("Player 2 : Enter Rock ,Paper or Scissors : ")

    if input1 == input2:
        print('DRAW GAME')
    elif input1 == 'Rock' and input2 == 'Paper':
        print('PLAYER 2 WINS')
    elif input1 == 'Rock' and input2 == 'Scissors':
        print('PLAYER 1 WINS')
    elif input1 == 'Paper' and input2 == 'Rock':
        print('PLAYER 1 WINS')
    elif input1 == 'Paper' and input2 == 'Scissors':
        print('PLAYER 2 WINS')
    elif input1 == 'Scissors' and input2 == 'Rock':
        print('PLAYER 2 WINS')
    elif input1 == 'Scissors' and input2 == 'Paper':
        print('PLAYER 1 WINS')
    else:
        print('Invalid Input, Type Rock, Paper or Scissors in your next attempt!')  

    answer = raw_input('Do you want to continue ? (Yes or No)')

    if answer == 'Yes':
        print('New game \n')
    elif answer == 'No':
        print('GAME OVER')
        break
    else:
        print('Wrong answer, please type Yes or No in your next attempt!')    