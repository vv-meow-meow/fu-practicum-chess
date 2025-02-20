from typing import Literal


class Figure:
    def __init__(self, color: Literal["black", "white"]):
        self.color: Literal["black", "white"] = color


class Rook(Figure):
    def __str__(self):
        return "♖" if self.color == "white" else "♜"


class Knight(Figure):
    def __str__(self):
        return "♘" if self.color == "white" else "♞"


class Bishop(Figure):
    def __str__(self):
        return "♗" if self.color == "white" else "♝"


class Queen(Figure):
    def __str__(self):
        return "♕" if self.color == "white" else "♛"


class King(Figure):
    def __str__(self):
        return "♔" if self.color == "white" else "♚"


class Pawn(Figure):
    def __str__(self):
        return "♙" if self.color == "white" else "♟"


class GameField:
    def __init__(self, data=None):
        self.data = data

    def initialize_field(self):
        self.data = {
            "a": [Rook("white"), Pawn("white"), None, None, None, None, Pawn("black"), Rook("black")],
            "b": [Knight("white"), Pawn("white"), None, None, None, None, Pawn("black"), Knight("black")],
            "c": [Bishop("white"), Pawn("white"), None, None, None, None, Pawn("black"), Bishop("black")],
            "d": [Queen("white"), Pawn("white"), None, None, None, None, Pawn("black"), Queen("black")],
            "e": [King("white"), Pawn("white"), None, None, None, None, Pawn("black"), King("black")],
            "f": [Bishop("white"), Pawn("white"), None, None, None, None, Pawn("black"), Bishop("black")],
            "g": [Knight("white"), Pawn("white"), None, None, None, None, Pawn("black"), Knight("black")],
            "h": [Rook("white"), Pawn("white"), None, None, None, None, Pawn("black"), Rook("black")]
        }

    def print_field(self):
        # Белые снизу
        print("  A B C D E F G H  ")
        for i in range(7, -1, -1):
            print(i + 1, end=" ")
            for pos in "abcdefgh":
                if self.data[pos][i] is None:
                    print(".", end=" ")
                else:
                    print(self.data[pos][i], end=" ")
            print(i + 1, end=" ")
            print()
        print("  A B C D E F G H  ")


if __name__ == '__main__':
    print("Привет! Это игра в шахматы. Белые начинают первыми. Успехов!")
    g = GameField()
    g.initialize_field()
    g.print_field()
