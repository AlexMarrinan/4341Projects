from TicTacToeClass import TicTacToeClass
from games4e import *


def main():
    answer = input("Would you like to run TicTacToe: ")
    if (answer.lower() == 'yes'):
        h = input("Please insert h: ")
        v = input("Please insert v: ")
        k = input("Please insert k: ")
        turn = 0
        first = input("Do you want to go first? (0 - yes, 1 - no)")
        if first != 0:
            turn = 1
        print('AI playing with Minmax Decision')
        searchType = 1
        game = TicTacToeClass(int(h), int(v), int(k))
        while True:
            state = game.initial
            while not game.terminal_test(state):
                if(turn %2 == 0):
                    if (searchType == 0):
                        move = minmax_decision(state, game)
                    else:
                        move = alpha_beta_search(state, game)
                else:
                    x = input("Please enter x coordinate of your move: ")
                    y = input("Please enter x coordinate of your move: ")
                    move = x,y
                print(move)
                state = game.result(state, move)
                print(game.display(state))
                move += 1

            answer = input("Would you like to run TicTacToe again? ")
            if (answer.lower() != 'yes'):
                print('Thank You for Playing Our Game')
                break


def mainAgain():
    game = TicTacToeClass(3, 3, 3)
    state = game.initial
    print(game.display(state))

    move = minmax_decision(game.initial, game)
    print(move)
    state = game.result(state, move)
    print(game.display(state))

if __name__=="__main__":
    main()
