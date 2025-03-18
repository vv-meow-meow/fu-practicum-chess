from checkers import Figure, Man


class GameField:
    def __init__(self, data=None):
        if data is None:
            self.data = self.initialize_field()
        else:
            self.data = data

    @staticmethod
    def initialize_field():
        field = {
            "a": [Man("white"), None, Man("white"), None, None, None, Man("black"), None],
            "b": [None, Man("white"), None, None, None, Man("black"), None, Man("black")],
            "c": [Man("white"), None, Man("white"), None, None, None, Man("black"), None],
            "d": [None, Man("white"), None, None, None, Man("black"), None, Man("black")],
            "e": [Man("white"), None, Man("white"), None, None, None, Man("black"), None],
            "f": [None, Man("white"), None, None, None, Man("black"), None, Man("black")],
            "g": [Man("white"), None, Man("white"), None, None, None, Man("black"), None],
            "h": [None, Man("white"), None, None, None, Man("black"), None, Man("black")]
        }
        return field

    def get_figure(self, move: str) -> Figure | None:
        col = move[0].lower()
        row = int(move[1]) - 1
        return self.data[col][row]

    def remove_figure(self, move: str):
        col = move[0].lower()
        row = int(move[1]) - 1
        self.data[col][row] = None

    def set_figure(self, move: str, figure: Figure):
        col = move[0].lower()
        row = int(move[1]) - 1
        self.data[col][row] = figure

    def print_field(self):
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
