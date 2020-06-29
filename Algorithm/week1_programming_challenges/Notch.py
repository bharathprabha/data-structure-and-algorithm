from random import choice

def play(player_name, player_score):
    seq = [1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 0]
    n = choice(seq)
    print("You got score of ", n)
    player_score += n
    print(player_name, " total score is ", player_score)
    return player_score


def check_for_win(player_total):
    if player_total > 99:
        return True
    else:
        return False


if __name__ == "__main__":
    player_one_total = 0
    player_two_total = 0
    while True:
        print("Player One")
        print("Enter 1 to play 0 to exit the game")
        if input() is "0":
            break
        else:
            player_one_total = play("Player One", player_one_total)
        if check_for_win(player_one_total):
            print("player One is the winner")
            break
        print("Player Two")
        print("Enter 1 to play 0 to exit the game")
        if input() is "0":
            break
        else:
            player_two_total = play("Player Two", player_two_total)
        if check_for_win(player_two_total):
            print("player Two is the winner")
            break