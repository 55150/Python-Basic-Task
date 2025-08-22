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
        player_symbols = ["O", "X"]
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
                # available_index.append(input_index)
            except ValueError:
                print("Error : Please Enter valid type")        

    def computer(self,name):
        print(f"Starting Player vs Computer Mode: {name} vs Computer")
        pass
t1 = TicTacToe()
while True:
    try:
        choice = int(input(" (1)Play with two player\n (2)Play Agaist Computer\n (3)Exit\n Enter Your Choice :"))
        if choice == 1:
            name = []
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
            name = str(input("Enter Player 1 Name :"))
            if not name.strip():
                print("Error : Please Enter String")
                continue
            t1.computer(name)
        elif choice == 3:
            print("-----Game End-----")
            break
        else:
            print("Error : Invalid Input ")
    except ValueError:
        print("Error : Value Error")

'''
win condition of 3x3 array
store[0][0] == store[0][1] == store[0][2]
store[1][0] == store[1][1] == store[1][2]
store[2][0] == store[2][1] == store[2][2]
store[0][0] == store[1][0] == store[2][0]
store[0][1] == store[1][1] == store[2][1]
store[0][2] == store[1][2] == store[2][2]
store[0][0] == store[1][1] == store[2][2]
store[0][2] == store[1][1] == store[2][0]
'''