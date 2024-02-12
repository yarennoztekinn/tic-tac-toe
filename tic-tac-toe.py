

def board(game):
    for row in game:
        print(row)

def user_replace(game, player):
    while True:
        if player == 1:
            aninput = input("Where do you want to put an X? Enter coordinates(row,column)(Enter 'E' to quit): ")

        if player == 2:
            aninput = input("Where do you want to put an O? Enter coordinates(row,column)(Enter 'E' to quit): ")

        if aninput.lower() == "e":# çıkmak istiyor
            print("You quit the game!")
            return "bye"
        
        else:
            coordinates = aninput.split(",")

            if len(coordinates) != 2 or not coordinates[0].strip().isdigit() or not coordinates[1].strip().isdigit():#sayı girdi mi
                print("Invalid input format. Please enter two numbers separated by a comma or 'e/E' to quit the game. ")
                continue

            row = int(coordinates[0])
            col = int(coordinates[1])

            if row not in range(1,4) or col not in range(1,4):# sınırı aşan sayı girdi mi
                print("the board's size 3x3. you can enter 1, 2 or 3. Try again: ")
                continue

            if game[row - 1][col - 1] != 0:  # yer boş mu 
                print("This place is already taken. Enter new coordinat: ")
                continue
                
            else:
                game[row - 1][col - 1] = player
                break

def who_won(game):
    for i in range(3):
        if game[i][0] == game[i][1] == game[i][2] != 0: #check rows
            return "Congrats, player {} won".format(game[i][0])
        elif game[0][i] == game[1][i] == game[2][i] != 0: #check columns
            return "Congrats, player {} won".format(game[0][i])
        elif game[0][0] == game[1][1] == game[2][2] != 0: #check diagonal 1
            return "Congrats, player {} won".format(game[0][0]) 
        elif game[0][2] == game[1][1] == game[2][0] != 0: #check diagonal 2
            return "Congrats, player {} won".format(game[0][2]) 
    return "Next player!!"

def play_again():
    again = input("Do you want to play again?(Yes or No) ")
    if again.lower() == "yes":
        new_game = [[0, 0, 0], 
                    [0, 0, 0], 
                    [0, 0, 0]]
        run_the_game(new_game)
    elif again.lower() == "no":
        print("See you later!!")
    else:
        print("I am sorry I did not understand. Can you just write 'yes' or 'no'")
        play_again()
    
def run_the_game(game):
    how_many = 0
    board(game)
    while True:
        result = user_replace(game, 1)
        if result == "bye": #oyuncu 1 oyundan çıktı. oyun sonlandı
            break
        else:
            how_many += 1
            board(game)
            result = who_won(game)
            if "won" in result:# oyuncu 1 kazandı. oyun sonlandı
                print(result)
                break

        if how_many == 9:  # tüm yerler doldu. oyun sonlandı
            print("Tie!")
            break

        result == user_replace(game, 2)
        if result == "bye": #oyuncu 2 oyundan çıktı. oyun sonlandı
            break
        else:
            how_many += 1
            board(game)
            result = who_won(game)
            if "won" in result: # oyuncu 2 kazandı. oyun sonlandı
                print(result)
                break

    play_again() #yeni oyun?

game = [[0,0,0],
        [0,0,0],
        [0,0,0]]
        
run_the_game(game)
