
def scores(game1,game2,game3,handicap_game):
    total = game1 + game2 + game3
    total_w_handicap = game1 + game2 + game3 + handicap_game
    average = total / 3
    avege_handicap = total_w_handicap / 3

    return avege_handicap,average






last_name = input("please enter your last name ")
game1 = float(input("Please enter your game score "))
game2  = float(input("Please enter your game score "))
game3  = float(input("Please enter your game score "))
handicap_game = float(input("Please enter your game score"))
avege_handicap,average = scores(game1,game2,game3,handicap_game)

print(last_name)
print("average score ",average)
print("average score with handicap ", avege_handicap)
