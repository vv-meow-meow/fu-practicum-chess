from checkers import Figure, Man


class GameField:
    """A class representing the checkers game board.

    The board is implemented as a dictionary with keys representing columns ('a' to 'h')
    and values being lists representing the rows. The GameField class provides methods to
    initialize the board, access and modify pieces, and print the board state.
    """

    def __init__(self, data=None):
        """Initialize the GameField with an optional pre-existing board configuration.

        If no data is provided, the board is initialized with the default starting configuration.

        Args:
            data (dict, optional): A dictionary representing the board state. Defaults to None.
        """
        if data is None:
            self.data = self.initialize_field()
        else:
            self.data = data

    @staticmethod
    def initialize_field():
        """Initialize and return the default board configuration.

        Returns:
            dict: A dictionary representing the board where keys are columns ('a' to 'h')
                and values are lists of pieces or None.
        """
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
        """Retrieve the figure at the specified board position.

        The move parameter is expected to be in algebraic notation (e.g., 'a1').

        Args:
            move (str): The board position in algebraic notation.

        Returns:
            Figure or None: The figure at the given position, or None if the square is empty.
        """
        col = move[0].lower()
        row = int(move[1]) - 1
        return self.data[col][row]

    def remove_figure(self, move: str):
        """Remove the figure from the specified board position.

        The move parameter is expected to be in algebraic notation (e.g., 'a1').

        Args:
            move (str): The board position in algebraic notation from which to remove the figure.
        """
        col = move[0].lower()
        row = int(move[1]) - 1
        self.data[col][row] = None

    def set_figure(self, move: str, figure: Figure):
        """Place a figure at the specified board position.

        The move parameter is expected to be in algebraic notation (e.g., 'a1').

        Args:
            move (str): The board position in algebraic notation.
            figure (Figure): The figure to be placed on the board.
        """
        col = move[0].lower()
        row = int(move[1]) - 1
        self.data[col][row] = figure

    def print_field(self):
        """Print the current state of the board to the console.

        The board is displayed with columns labeled from A to H and rows from 1 to 8.
        Empty squares are represented by a dot.
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
