from __future__ import annotations
from typing import Literal, TYPE_CHECKING

from abc import ABC, abstractmethod

if TYPE_CHECKING:
    from field import GameField


class Figure(ABC):
    def __init__(self, color: Literal["black", "white"]):
        """Initialize a Figure with a specified color.

        Args:
            color (Literal["black", "white"]): The color of the figure.
        """
        self.color: Literal["black", "white"] = color

    @abstractmethod
    def _get_moves(self, pos: str) -> list:
        """Get the basic potential moves for the figure from the specified position.

        This is a helper method and should not be called directly; use get_available_moves() for move validation.

        Args:
            pos (str): The current position in algebraic notation (e.g., 'a1').

        Returns:
            list: A list (or nested list for sliding pieces) of potential moves.
        """
        pass

    @abstractmethod
    def get_available_moves(self, pos: str, board: GameField) -> list:
        """Calculate the legal moves for the figure from the given position.

        This method uses the basic moves and evaluates the board state to determine possible captures.

        Args:
            pos (str): The current position in algebraic notation (e.g., 'a1').
            board (GameField): The game board containing the positions of all figures.

        Returns:
            list: A list of legal moves for the figure.
        """
        pass


class King(Figure):
    """Represents a King piece in checkers.

    A king can move one square diagonally in any direction and capture opposing pieces by jumping over them.
    """

    def __str__(self):
        """Return a string representation of the king piece."""
        return "KW" if self.color == "white" else "KB"

    def _get_moves(self, pos: str) -> list:
        col = ord(pos[0])
        row = int(pos[1])
        possible_moves = (
            f"{chr(col - 1)}{row + 1}",
            f"{chr(col + 1)}{row + 1}",
            f"{chr(col - 1)}{row - 1}",
            f"{chr(col + 1)}{row - 1}"
        )
        result = []
        for move in possible_moves:
            if "a" <= move[0] <= "h" and 1 <= int(move[1]) <= 8:
                result.append(move)
        return result

    def get_available_moves(self, pos: str, board: GameField) -> list:
        """Calculate the legal moves for the king from the given position.

        This method determines basic diagonal moves and then validates them against the game board.
        If an opponent's piece is encountered,
        it checks whether the capture move is valid by ensuring the landing square is empty.

        Args:
            pos (str): The current position in algebraic notation (e.g., 'a1').
            board (GameField): The game board containing piece positions.

        Returns:
            list: A list of valid moves for the king, including potential capture moves.
        """
        pos = pos.lower()
        pos_col = ord(pos[0])
        pos_row = int(pos[1])
        moves = self._get_moves(pos)

        result = []
        for move in moves:
            figure = board.get_figure(move)
            if figure is None:
                result.append(move)
                continue
            else:
                if figure.color != self.color:
                    move_col = ord(move[0])
                    move_row = int(move[1])
                    col_dir = move_col - pos_col
                    row_dir = move_row - pos_row
                    future_pos = f"{chr(move_col + col_dir)}{move_row + row_dir}"
                    future_move_figure = board.get_figure(future_pos)
                    if future_move_figure is None:
                        result.append(future_pos)
        print(f"Available moves: {result}")
        return result


class Man(Figure):
    """Represents a Man piece in checkers.

    A man moves diagonally forward (up for white, down for black) and can capture opposing pieces by jumping over them.
    """

    def __str__(self):
        """Return a string representation of the man piece."""
        return "⚪" if self.color == "white" else "⚫"

    def _get_moves(self, pos: str) -> list:
        col = ord(pos[0])
        row = int(pos[1])
        if self.color == "white":
            possible_moves = (
                f"{chr(col - 1)}{row + 1}",
                f"{chr(col + 1)}{row + 1}"
            )
        else:
            possible_moves = (
                f"{chr(col - 1)}{row - 1}",
                f"{chr(col + 1)}{row - 1}"
            )
        result = []
        for move in possible_moves:
            if "a" <= move[0] <= "h" and 1 <= int(move[1]) <= 8:
                result.append(move)
        return result

    def get_available_moves(self, pos: str, board: GameField) -> list:
        """Calculate the legal moves for the man from the given position.

        This method determines valid forward moves and checks for possible captures based on the board state.
        If an opponent's piece is encountered, it validates the capture move by ensuring the landing square is empty.

        Args:
            pos (str): The current position in algebraic notation (e.g., 'a1').
            board (GameField): The game board containing piece positions.

        Returns:
            list: A list of valid moves for the man, including potential capture moves.
        """
        pos = pos.lower()
        pos_col = ord(pos[0])
        pos_row = int(pos[1])
        moves = self._get_moves(pos)

        result = []
        for move in moves:
            figure = board.get_figure(move)
            if figure is None:
                result.append(move)
                continue
            else:
                if figure.color != self.color:
                    move_col = ord(move[0])
                    move_row = int(move[1])
                    col_dir = move_col - pos_col
                    row_dir = move_row - pos_row
                    future_pos = f"{chr(move_col + col_dir)}{move_row + row_dir}"
                    future_move_figure = board.get_figure(future_pos)
                    if future_move_figure is None:
                        result.append(future_pos)
        print(f"Available moves: {result}")
        return result
