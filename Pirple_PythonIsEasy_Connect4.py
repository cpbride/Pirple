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
