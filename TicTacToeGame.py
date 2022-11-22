from TicTacToeClass import TicTacToeClass
from games4e import *


def main():
    answer = input("Would you like to run TicTacToe: ")
    if (answer.lower() == 'yes'):
        h = input("Please insert h: ")
        v = input("Please insert v: ")
        k = input("Please insert k: ")
        print('AI playing with Minmax Decision')
        game = TicTacToeClass(int(h), int(v), int(k))
        state = game.initial
        while (not game.terminal_test(state)):
            move = minmax_decision(state, game)
            print(move)
            state = game.result(state, move)
            print(game.display(state))

            answer = input("Would you like to run TicTacToe again? ")
            if (answer.lower() != 'yes'):
                print('Thank You for Playing Our Game')
                break
        
        
        
        print('Alpha-Beta Pruning Search')
'''        while (True):
            game = TicTacToeClass(int(h), int(v), int(k))
            print(game.h)
            answer = input("Would you like to run TicTacToe again? ")
            if (answer.lower() != 'yes'):
                print('Thank You for Playing Our Game')
                break'''


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
