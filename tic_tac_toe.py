class TicTacToe():
    def __init__(self):
        pass
    def two_player(self,name):
        '''
 Input Diagram
 1 | 2 | 3
-----------
 4 | 5 | 6
-----------
 7 | 8 | 9'''

        print(f"Starting Two Player Mode: {name[0]} vs {name[1]}")
        store = [[None]*3 for _ in range(3)]
        win_conditions = [
            [(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],
            [(0, 0), (1, 1), (2, 2)],
            [(0, 2), (1, 1), (2, 0)]
        ]
        player_symbols = ["X","O"]
        available_index = []
        turn = 0
        while True:
            try:
                print(self.two_player.__doc__)
                print("\nCurrent Board:\n")
                pos = 1
                for index,i in enumerate(store):
                    line = []
                    for j in i:
                        if j is None:   # blank place
                            line.append("   ")
                        else:
                            line.append(f" {j} ")
                        pos += 1
                    print("|".join(line))
                    if index < len(store)-1:
                        print("-" * 11)
                input_index = int(input(f"{name[turn]}'s turn ({player_symbols[turn]}), enter position (1-9): "))

                if input_index in available_index:
                    print("Error : Already Filled try Diffrent")
                    continue
                if input_index > 9 or input_index <= 0:
                    print("Error! : enter valid available input")
                    continue
                row = (input_index-1)//3
                col = (input_index-1)% 3
                store[row][col] = player_symbols[turn]
                indicat = []
                for index,item in enumerate(store):
                    for s_index,s_item in enumerate(item):
                        if s_item == player_symbols[turn]:
                            indicat.append((index,s_index))

                print(indicat)
                win = 0
                for condition in win_conditions:
                    c = 0
                    for position in condition:
                        if position in indicat:
                            c +=1
                    if c == 3:
                        win+=1
                if win ==1:
                    print(f"{name[turn]} is Win Tic Tac Toe\n")
                    break
                
                turn = 1-turn
                available_index.append(input_index)
                if len(available_index) == 9:
                    print("Game Over! Board Full.")
                    break
            except ValueError:
                print("Error : Please Enter valid type")        

    def computer(self,name):
        print(f"Starting Play Agaist {name[0]} vs {name[1]}")
        store = [[None]*3 for _ in range(3)]
        win_conditions = [
            [(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],
            [(0, 0), (1, 1), (2, 2)],
            [(0, 2), (1, 1), (2, 0)]
        ]
        player_symbols = ["O", "X"]
        available_index = []
        turn = 0
        comp_index = []
        while True:
            try:
                #belowe print is use for structure enter for input 
                print(self.two_player.__doc__)
                #belove code is using for current which place to enter and available board empty place display
                print("\nCurrent Board:\n")
                pos = 1
                for index,i in enumerate(store):
                    line = []
                    for j in i:
                        if j is None:   # blank place
                            line.append("   ")
                        else:
                            line.append(f" {j} ")
                        pos += 1
                    print("|".join(line))
                    if index < len(store)-1:
                        print("-" * 11)
                if turn == 0:
                    # for condition in win_conditions:
                    pass
                if turn == 0:
                    pass
                    def evaluate(board):
                        # Check all win conditions
                        for condition in win_conditions:
                            vals = [board[r][c] for r, c in condition]
                            if vals.count("O") == 3:   # computer is "O"
                                return 10
                            elif vals.count("X") == 3: # human is "X"
                                return -10
                        return 0

                    def minimax(board, depth, isMax):
                        score = evaluate(board)
                        if score == 10:   # computer win
                            return score - depth
                        if score == -10:  # human win
                            return score + depth
                        if all(all(cell is not None for cell in row) for row in board):
                            return 0  # draw

                        if isMax:  # computer's move
                            best = -1000
                            for i in range(3):
                                for j in range(3):
                                    if board[i][j] is None:
                                        board[i][j] = "O"
                                        best = max(best, minimax(board, depth + 1, not isMax))
                                        board[i][j] = None
                            return best
                        else:  # human's move
                            best = 1000
                            for i in range(3):
                                for j in range(3):
                                    if board[i][j] is None:
                                        board[i][j] = "X"
                                        best = min(best, minimax(board, depth + 1, not isMax))
                                        board[i][j] = None
                            return best

                    best_val = -1000
                    best_move = None
                    for i in range(3):
                        for j in range(3):
                            if store[i][j] is None:
                                store[i][j] = "O"
                                move_val = minimax(store, 0, False)
                                store[i][j] = None
                                if move_val > best_val:
                                    best_move = (i, j)
                                    best_val = move_val
                    row, col = best_move
                    input_index = row * 3 + col + 1
                    print(f"Computer chooses position {input_index}")
                    #######
                else:
                    input_index = int(input(f"{name[turn]}'s turn ({player_symbols[turn]}), enter position (1-9): "))
                # check input is available on board 
                if input_index in available_index:
                    print("Error : Already Filled try Diffrent")
                    continue
                if input_index > 9 or input_index <= 0:
                    print("Error! : enter valid available input")
                    continue
                row = (input_index-1)//3
                col = (input_index-1)% 3
                store[row][col] = player_symbols[turn]
                indicat = []
                #its provide to indicatn to index provide which know asigned 
                for index,item in enumerate(store):
                    for s_index,s_item in enumerate(item):
                        if s_item == player_symbols[turn]:
                            indicat.append((index,s_index))

                print(indicat)
                win = 0
                #is check if any user is win or not and its using is win_condition 
                for condition in win_conditions:
                    c = 0
                    for position in condition:
                        if position in indicat:
                            c +=1
                    if c == 3:
                        win+=1
                if win ==1:
                    print(f"{name[turn]} is Win Tic Tac Toe\n")
                    break
                #increase and decrease into turn
                turn = 1-turn
                available_index.append(input_index)
                if len(available_index) == 9:
                    print("Game Over! Board Full.")
                    break
            except ValueError:
                print("Error : Please Enter valid type")  
t1 = TicTacToe()
while True:
    try:
        choice = int(input(" (1)Play with two player\n (2)Play Agaist Computer\n (3)Exit\n Enter Your Choice :"))
        name = []
        if choice == 1:
            name_1 = str(input("Enter Player 1 Name :"))
            if not name_1.strip():
                print("Error : Please Enter String")
                continue
            name.append(name_1)
            name_2 = str(input("Enter Player 2 Name :"))
            if name_1 == name_2:
                print("Error : Please Enter Unique Name")
                continue
            if not name_2.strip():
                print("Error : Please Enter String")
                continue
            name.append(name_2)
            t1.two_player(name)
        elif choice == 2:
            human = str(input("Enter Player Name :"))
            if not human.strip():
                print("Error : Please Enter String")
                continue
            name.append('computer')
            name.append(human)
            t1.computer(name)
        elif choice == 3:
            print("-----Game End-----")
            break
        else:
            print("Error : Invalid Input ")
    except ValueError:
        print("Error : Value Error")