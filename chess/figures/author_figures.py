from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..field import GameField

from .figures import *


class Balloon(Figure):
    """Balloon Figure.

    This figure is placed on cells B and G (instead of knights).
    When used, it ascends and then falls onto an opponent's piece (except King and Queen), capturing it.
    It can move to any square (except those occupied by King and Queen).
    """

    def __str__(self):
        """Return a string representation of the Balloon figure."""
        return "⚪" if self.color == "white" else "⚫"

    def _get_moves(self, pos: str) -> list:
        moves = []
        for col in range(97, 104 + 1):
            for row in range(1, 8 + 1):
                moves.append(f"{chr(col)}{row}")
        moves.remove(pos)
        return moves

    def get_available_moves(self, pos: str, board: GameField) -> list:
        """Determine available moves for the Balloon figure given the current board state.

        This method filters the potential moves computed by _get_moves by checking the board.
        A move is available if the destination square is empty or contains an opponent's piece
        (excluding King and Queen).

        Args:
            pos (str): The current position in algebraic notation.
            board (GameField): The current game board.

        Returns:
            list: A list of legal moves for the Balloon figure.
        """
        pos = pos.lower()
        moves = self._get_moves(pos)
        result = []
        for move in moves:
            figure_on_move = board.get_figure(move)
            if figure_on_move is None:
                result.append(move)
            else:
                if figure_on_move.color != self.color:
                    if not (isinstance(figure_on_move, King) or isinstance(figure_on_move, Queen)):
                        result.append(move)
        return result


class Tank(Figure):
    """Tank Figure.

    This figure, resembling a knight with a large shield in front,
    can move diagonally and capture only in the forward direction.
    """

    def __str__(self):
        """Return a string representation of the Tank figure."""
        return "🏳" if self.color == "white" else "🏴"

    def _get_moves(self, pos: str) -> list:
        col = ord(pos[0])
        row = int(pos[1])

        if row == 8:
            return []

        moves = []
        left_move = chr(col - 1)
        if "a" <= left_move <= "h":
            moves.append(f"{left_move}{row + 1}")
        right_move = chr(col + 1)
        if "a" <= right_move <= "h":
            moves.append(f"{right_move}{row + 1}")

        return moves

    def get_available_moves(self, pos: str, board: GameField) -> list:
        """Determine the available moves for the Tank figure given the board state.

        The Tank can move diagonally forward to an empty square.
        If the forward square contains an opponent's piece, that move is also considered available.

        Args:
            pos (str): The current position in algebraic notation.
            board (GameField): The current game board.

        Returns:
            list: A list of legal moves for the Tank figure.
        """
        pos = pos.lower()
        moves = self._get_moves(pos)

        result = []
        for move in moves:
            figure_on_move = board.get_figure(move)
            if figure_on_move is None:
                result.append(move)

        col = pos[0]
        row = int(pos[1])
        capture_move = f"{col}{row + 1}"
        figure_on_capture = board.get_figure(capture_move)
        if figure_on_capture is not None:
            if figure_on_capture.color != self.color:
                result.append(capture_move)

        return result


class PEKKA(Figure):
    """PEKKA Figure.

    This figure can move one step forward and capture opponent pawns that are one or two squares ahead.
    """

    def __str__(self):
        """Return a string representation of the PEKKA figure.

        Returns:
            str: "✝" if the figure is white, otherwise "✞".
        """
        return "✝" if self.color == "white" else "✞"

    def _get_moves(self, pos: str) -> list:
        """Calculate the basic forward move for the PEKKA figure based on its position.

        The PEKKA moves one square forward. The direction depends on its color:
        white moves upward (increasing row) while black moves downward (decreasing row).
        If at the edge of the board, no move is available.

        Args:
            pos (str): The current position in algebraic notation.

        Returns:
            list: A list containing the potential move.
        """
        col = pos[0]
        row = int(pos[1])
        if row == 8:
            return []

        return [f"{col}{row + 1}" if self.color == "white" else f"{col}{row - 1}"]

    def get_available_moves(self, pos: str, board: GameField) -> list:
        """Determine the available moves for the PEKKA figure based on the board state.

        This method returns the basic forward move if the destination is empty or occupied by an opponent.
        Additionally, it checks for potential capture moves two squares ahead if an opponent's piece is present,
        subject to board limits.

        Args:
            pos (str): The current position in algebraic notation.
            board (GameField): The current game board.

        Returns:
            list: A list of legal moves for the PEKKA figure.
        """
        pos = pos.lower()
        moves = self._get_moves(pos)
        result = []
        for move in moves:
            figure_on_move = board.get_figure(move)
            if figure_on_move is None:
                result.append(move)
            elif figure_on_move.color != self.color:
                result.append(move)

        pos_col = pos[0]
        pos_row = int(pos[1])
        if self.color == "white":
            if 1 <= pos_row <= 6:
                capture_move = f"{pos_col}{pos_row + 2}"
                figure_on_capture = board.get_figure(capture_move)
                if figure_on_capture is not None:
                    if figure_on_capture.color != self.color:
                        result.append(capture_move)
        else:
            if 3 <= pos_row <= 8:
                capture_move = f"{pos_col}{pos_row - 2}"
                figure_on_capture = board.get_figure(capture_move)
                if figure_on_capture is not None:
                    if figure_on_capture.color != self.color:
                        result.append(capture_move)

        return result


#: Starting board configuration for the custom chess game.
AUTHOR_FIELD = {
    "a": [Rook("white"), Pawn("white"), None, None, None, None, Pawn("black"), Rook("black")],
    "b": [Balloon("white"), Pawn("white"), None, None, None, None, Pawn("black"), Balloon("black")],
    "c": [Bishop("white"), Pawn("white"), None, None, None, None, Pawn("black"), Bishop("black")],
    "d": [Queen("white"), Tank("white"), None, None, None, None, Tank("black"), Queen("black")],
    "e": [King("white"), PEKKA("white"), None, None, None, None, PEKKA("black"), King("black")],
    "f": [Bishop("white"), Pawn("white"), None, None, None, None, Pawn("black"), Bishop("black")],
    "g": [Knight("white"), Pawn("white"), None, None, None, None, Pawn("black"), Knight("black")],
    "h": [Rook("white"), Pawn("white"), None, None, None, None, Pawn("black"), Rook("black")]
}
