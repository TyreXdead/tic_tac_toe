from ast import Break
import random


class TicTocToe():  # All first character of words be capetalize -> Pascal case

    state = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
    current_turn = 'X'

    def random_choose_player(self):
        rand_num = random.randint(0, 1)
        if rand_num == 0:
            return "X"

        return "O"

    def show_board(self):
        for row in self.state:
            for col in row:
                print(col, end=' ')
            print()

    def turn(self):
        while True:
            x = int(input('Enter your row number : '))
            if x > 2:
                continue
            y = int(input('Enter your col number; '))
            if y > 2:
                continue
            if self.state[x][y] != '-':
                continue

            self.state[x][y] = self.current_turn
            break

        self.show_board()

        # call win & tie functions
        if self.is_player_win():
            print("player {} won :)".format(self.current_turn))
        elif self.is_board_filled():
            print('it is a tie :|')
        else:
                
            if self.current_turn == 'X':
                self.current_turn = 'O'
            else:
                self.current_turn = 'X'

        
            self.turn()

    def start(self):
        self.show_board()
        self.current_turn = self.random_choose_player()
        print('it is {} turn'.format(self.current_turn))
        self.turn()
    
    def is_player_win(self):
        for i in range(3):
            if self.state[i][0]==self.current_turn and self.state[i][1]==self.current_turn and self.state[i][2]==self.current_turn:
                return True
        
        for i in range(3):
            if self.state[0][i]==self.current_turn and self.state[1][i]==self.current_turn and self.state[2][i]==self.current_turn:
                return True

        if self.state[0][0]==self.current_turn and self.state[1][1]==self.current_turn and self.state[2][2]==self.current_turn:
            return True

        if self.state[0][2]==self.current_turn and self.state[1][1]==self.current_turn and self.state[2][0]==self.current_turn:
            return True    

    def is_board_filled(self):
        for row in self.state:
            for col in row:
                if col=='-':
                    return False
        return True            


def main():
    tic_toc_toe = TicTocToe()

    tic_toc_toe.start()


if __name__ == '__main__':
    main() 