from figures import Pawn, Rook, Knight, Bishop, Queen, King, Figure


class GameField:
    def __init__(self, data=None):
        if data is None:
            self.data = self.initialize_field()
        else:
            self.data = data

    @staticmethod
    def initialize_field():
        field = {
            "a": [Rook("white"), Pawn("white"), None, None, None, None, Pawn("black"), Rook("black")],
            "b": [Knight("white"), Pawn("white"), None, None, None, None, Pawn("black"), Knight("black")],
            "c": [Bishop("white"), Pawn("white"), None, None, None, None, Pawn("black"), Bishop("black")],
            "d": [Queen("white"), Pawn("white"), None, None, None, None, Pawn("black"), Queen("black")],
            "e": [King("white"), Pawn("white"), None, None, None, None, Pawn("black"), King("black")],
            "f": [Bishop("white"), Pawn("white"), None, None, None, None, Pawn("black"), Bishop("black")],
            "g": [Knight("white"), Pawn("white"), None, None, None, None, Pawn("black"), Knight("black")],
            "h": [Rook("white"), Pawn("white"), None, None, None, None, Pawn("black"), Rook("black")]
        }
        return field

    def get_figure(self, move: str) -> Figure | None:
        col = move[0]
        row = int(move[1]) - 1
        return self.data[col][row]

    def remove_figure(self, move: str):
        col = move[0]
        row = int(move[1]) - 1
        self.data[col][row] = None

    def set_figure(self, move: str, figure: Figure):
        col = move[0]
        row = int(move[1]) - 1
        self.data[col][row] = figure

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
