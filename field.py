from figures import Pawn, Rook, Knight, Bishop, Queen, King, Figure


class GameField:
    """Represents a chess game field.

    This class provides methods for initializing the board with chess pieces,
    retrieving, updating, and printing the state of the game field.
    """

    def __init__(self, data=None):
        """Initializes the GameField.

        If no custom data is provided, the board is set up with the standard initial
        configuration of chess pieces. Otherwise, the provided data is used.

        Args:
            data (Optional[dict]): A dictionary representing the board state, where keys are
                column letters and values are lists representing rows. Defaults to None.
        """
        if data is None:
            self.data = self.initialize_field()
        else:
            self.data = data

    @staticmethod
    def initialize_field():
        """Initializes the game field with the standard chess starting position.

        Returns:
            dict: A dictionary representing the chess board with columns 'a' to 'h',
                where each column is a list of pieces or None, arranged in order.
        """
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
        """Retrieves the figure at the specified board position.

        Args:
            move (str): The board position in algebraic notation (e.g., 'e2').

        Returns:
            Figure or None: The chess figure at the given position, or None if the square is empty.
        """
        col = move[0].lower()
        row = int(move[1]) - 1
        return self.data[col][row]

    def remove_figure(self, move: str):
        """Removes the figure from the specified board position.

        Args:
            move (str): The board position in algebraic notation (e.g., 'e2').
        """
        col = move[0].lower()
        row = int(move[1]) - 1
        self.data[col][row] = None

    def set_figure(self, move: str, figure: Figure):
        """Places a chess figure at the specified board position.

        Args:
            move (str): The board position in algebraic notation (e.g., 'e2').
            figure (Figure): The chess figure to place on the board.
        """
        col = move[0].lower()
        row = int(move[1]) - 1
        self.data[col][row] = figure

    def print_field(self):
        """Prints the current state of the game board.

        The board is printed with columns labeled A to H and rows numbered 1 to 8,
        with white pieces displayed at the bottom.
        """
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
