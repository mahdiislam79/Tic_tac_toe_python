game = [[0,0,0],
        [0,0,0],
        [0,0,0]]

def game_board(player = 0, row = 0, column = 0, just_display=False):

    print('   0, 1, 2')
    if not just_display:
        game[row][column] = player
    count=0
    for count, row in enumerate(game):
        print(count,row)
game_board(player=2,row=0,column=0)
def win(current_game):
    # for row in game:                                                    # Horizontal winner
    #     print(row)
    #     if row.count(row[0]) == len(row) and row[0] != 0:
    #         print('Winner')
    # for col in range(len(game)):
    #     check = []
    #     for row in game:
    #         check.append(row[col])
    #     if check.count(check[0]) == len(check) and check[0]!=0:        # Vertical Winner
    #         print('Winner')
    diag = [] 
    for i in range(len(game)):
        diag.append(game[i][i])
    if diag.count(diag[0]) == len(diag) and diag[0] != 0:
        print('Winner')

    diag = []
    for col,row in enumerate(list(reversed(range(len(game))))):
        diag.append(game[row][col])
    if diag.count(diag[0]) == len(diag) and diag[0] != 0:
          print('Winner')



game_board(2,1,1)
game_board(2,2,2)
win(game)
    