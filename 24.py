# Draw A Game Board 

""" This exercise is Part 1 of 4 of the Tic Tac Toe exercise series. The other exercises are: Part 2, Part 3, and Part 4.

Time for some fake graphics! Let's say we want to draw game boards that look like this:

 --- --- --- 
|   |   |   | 
 --- --- ---  
|   |   |   | 
 --- --- ---  
|   |   |   | 
 --- --- --- 
This one is 3x3 (like in tic tac toe). Obviously, they come in many other sizes (8x8 for chess, 19x19 for Go, and many more).

Ask the user what size game board they want to draw, and draw it for them to the screen using Python's print statement. """

def draw(n):
    line = ' ---'
    column = '|   '
    for i in range(1,n+1):
        print(' ---' * n)
        print(column * (n+1))
    print(line * n)

n = int(raw_input("Enter the board size : "))
draw(n)