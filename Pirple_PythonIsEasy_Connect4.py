'''https://github.com/cpbride/Pirple/blob/main/Pirple_PythonIsEasy_Connect4.py
This is supposed to be a simple Connect 4 simulator. When I run this code (and it is 
not in its finished form, but I can't get it to do something simple), the row/column 
allocation when I take a turn does not make sense. For example, choosing r0/c0 will 
populate cells r0c0 through r0c3. Multiple spaces are populated sometimes, and other 
times nothing happens. But when I try to populate a space twice, it returns that 
the space is occupied even though it does not show up in the grid. This was copied
and augmented from a TicTacToe script, so I was thinking that it should behave in a 
similar fashion at this point, but it does not'''

def drawField(field):
    for row in range(11):
        if row % 2 == 0:
            practicalRow = int(row/2)
            for column in range(13):
                if column % 2 == 0:
                    practicalColumn = int(column/8)
                    if column != 12:
                        print(field[practicalColumn][practicalRow], end="")
                    else:
                        print(field[practicalColumn][practicalRow])
                else:
                    print("|", end="")
        else:
            print("-------------")


Player = 1
currentField = [[" ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " "]]
drawField(currentField)
while True:
    print("Players turn:", Player)
    MoveRow = int(input("Please enter the row\n"))
    MoveColumn = int(input("Please enter the column\n"))
    if Player == 1:
        if currentField[MoveColumn][MoveRow] == " ":
            currentField[MoveColumn][MoveRow] = "X"
            Player = 2
        else:
            if currentField[MoveColumn][MoveRow] != " ":
                print("That spot has been taken, please select another spot")
    else:
        if currentField[MoveColumn][MoveRow] == " ":
            currentField[MoveColumn][MoveRow] = "O"
            Player = 1
        else:
            if currentField[MoveColumn][MoveRow] != " ":
                print("That spot has been taken, please select another spot")
    drawField(currentField)
