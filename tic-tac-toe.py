"""A tic-tac-toe game"""

from datetime import datetime

class Player:
    def __init__(self, name, piece):
        self.piece = piece  #X or O
        self.name = name


class Move(Player):
    def __init__(self, Player, position):
        self.player = Player        #a player
        self.position = position    #tuple of row, column
        super().__init__(piece = Player.piece, name = Player.name)


class Board:
    def __init__(self):
        self.moves = {
            (0,0): '-',
            (0,1): '-',
            (0,2): '-',
            (1,0): '-',
            (1,1): '-',
            (1,2): '-',
            (2,0): '-',
            (2,1): '-',
            (2,2): '-'
        }

    def display(self):
        print(f"{self.moves[0,0]} {self.moves[0,1]} {self.moves[0,2]}")
        print(f"{self.moves[1,0]} {self.moves[1,1]} {self.moves[1,2]}")
        print(f"{self.moves[2,0]} {self.moves[2,1]} {self.moves[2,2]}")

    def add_move(self, Move):
        self.moves[Move.position] = Move.piece
        my_board.display()
        if my_game.check_win():
            print(f"{Move.name} wins! The game is over at {my_game.stop}")


class Game:
    def __init__(self, Board, Player1, Player2):
        self.board = Board
        self.player1 = Player1
        self.player2 = Player2
        self.start = datetime.now().strftime("%H:%M:%S")
        self.stop = None
        print(f"The game begins at {self.start}")

    def check_win(self):
        for i in range(0,3):
            a = self.board.moves[(i,0)] #check rows
            b = self.board.moves[(i,1)]
            c = self.board.moves[(i,2)]
            if a == b and a == c and a != '-':
                self.stop = datetime.now().strftime("%H:%M:%S")
                return True
            a = self.board.moves[(0,i)] #check columns
            b = self.board.moves[(1,i)]
            c = self.board.moves[(2,i)]
            if a == b and a == c and a != '-':
                self.stop = datetime.now().strftime("%H:%M:%S")
                return True
        a = self.board.moves[(0,0)] #check forward diagonal
        b = self.board.moves[(1,1)]
        c = self.board.moves[(2,2)]
        if a == b and a == c and a != '-':
            self.stop = datetime.now().strftime("%H:%M:%S")
            return True
        a = self.board.moves[(0,2)] #check backward diagonal
        c = self.board.moves[(2,0)]
        if a == b and a == c and a != '-':
            self.stop = datetime.now().strftime("%H:%M:%S")
            return True
        if '-' not in self.board.moves.values():
            self.stop = datetime.now().strftime("%H:%M:%S")
            print("The game is a draw at {self.stop}")
        return False

harry = Player("Harry", "X")
hermione = Player("Hermione", "O")

my_board = Board()

my_game = Game(my_board, harry, hermione)

first_move = Move(harry, (0, 2))

# my_board.add_move(first_move)
my_board.display()