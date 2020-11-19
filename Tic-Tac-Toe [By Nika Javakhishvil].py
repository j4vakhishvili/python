def tic_tac_toe():
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    end = False
    win_commbinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

    def draw():
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("Tic-Tac-Toe")
        print("X-O")
        print("By Nika Javakhisvili")
        print("-----")
        print(board[0],  board[1],  board[2])
        print("-----")
        print(board[3],  board[4],  board[5])
        print("-----")
        print(board[6],  board[7],  board[8])
        print("-----")
        print()

    def p1():
        n = choose_number()
        if board[n] == "X" or board[n] == "O":
            print("\nადგილი დაკავებულია, დაწერეთ სხვა ნომერი !")
            p1()
        else:
            board[n] = "X"

    def p2():
        n = choose_number()
        if board[n] == "X" or board[n] == "O":
            print("\nადგილი დაკავებულია, დაწერეთ სხვა ნომერი !")
            p2()
        else:
            board[n] = "O"

    def choose_number():
        while True:
            while True:
                a = input()
                try:
                    a  = int(a)
                    a -= 1
                    if a in range(0, 9):
                        return a
                    else:
                        print("\nადგილი დაკავებულია, დაწერეთ სხვა ნომერი !")
                        continue
                except ValueError:
                   print("\nეს ნომერი აქ არ მდებარეობს, დაწერეთ სხვა ნომერი !")
                   continue

    def check_board():
        count = 0
        for a in win_commbinations:
            if board[a[0]] == board[a[1]] == board[a[2]] == "X":
                print("მოიგო X-მა !!!\n")

                print("გილოცავთ!\n")
                return True

            if board[a[0]] == board[a[1]] == board[a[2]] == "O":
                print("მოიგო O-მა !!!\n")
                print("გილოცავთ!\n")
                return True
        for a in range(9):
            if board[a] == "X" or board[a] == "O":
                count += 1
            if count == 9:
                print("ფრეა გამარჯვებული ვერ გამოვლინდა\n")
                return True

    while not end:
        draw()
        end = check_board()
        if end == True:
            break
        print("შეიყვანეთ X-ის ნომერი:")
        p1()
        print()
        draw()
        end = check_board()
        if end == True:
            break
        print("შეიყვანეთ O-ის ნომერი:")
        p2()
        print()

    if input("ცადეთ თავიდან [თავიდან დასაწყებად დაწერეთ R, დასასრულებად E] (r/e)\n") == "r":
        print()
        tic_tac_toe()

tic_tac_toe()
