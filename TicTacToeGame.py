from TicTacToeClass import TicTacToeClass
from games4e import *


def main():
    answer = input("Would you like to run TicTacToe: ")
    if (answer.lower() == 'yes'):
        h = input("Please insert h: ")
        v = input("Please insert v: ")
        k = input("Please insert k: ")

        first = int(input("Do you want to go first? (1 - yes, 0 - no) "))

        game = TicTacToeClass(int(h), int(v), int(k))
        while True:
            state = game.initial
            searchAlg=input("What search alg should we use? Minmax or AlphaBeta?: ")
            if searchAlg.lower() == 'minmax':
                print('AI playing with Minmax Decision')
            else:
                print('AI playing with Alpha-Beta Search')
            
            game.display(state)
            while not game.terminal_test(state):
                if(first %2 == 0):
                    print("AI move...")
                    if (searchAlg == 'minmax'):
                        move = minmax_decision(state, game)
                    else:
                        move = alpha_beta_search(state, game)
                else:
                    x = int(input("Please enter x coordinate of your move: "))
                    y = int(input("Please enter y coordinate of your move: "))
                    move = y,x
                print(move)
                state = game.result(state, move)
                game.display(state)
                first += 1

            answer = input("Would you like to run TicTacToe again? ")
            if (answer.lower() != 'yes'):
                print('Thank You for Playing Our Game')
                break

if __name__=="__main__":
    main()
