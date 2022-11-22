from TicTacToeClass import TicTacToeClass


def main():
    answer = input("Would you like to run TicTacToe: ")
    if (answer.lower() == 'yes'):
        h = input("Please insert h: ")
        v = input("Please insert v: ")
        k = input("Please insert k: ")
        print('AI playing with Minmax Decision')
        while (True):
            game = TicTacToeClass(int(h), int(v), int(k))
            print(game.h)
            answer = input("Would you like to run TicTacToe again? ")
            if (answer.lower() != 'yes'):
                print('Thank You for Playing Our Game')
                break
        print('Alpha-Beta Pruning Search')
        while (True):
            game = TicTacToeClass(int(h), int(v), int(k))
            print(game.h)
            answer = input("Would you like to run TicTacToe again? ")
            if (answer.lower() != 'yes'):
                print('Thank You for Playing Our Game')
                break

def results(self):

    # print(f'Minmax {type(minmax_decision(state, self.game))}')

if __name__ == "__main__":
    main()