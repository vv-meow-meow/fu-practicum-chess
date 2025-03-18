from __future__ import annotations
from typing import Literal, TYPE_CHECKING

from abc import ABC, abstractmethod

if TYPE_CHECKING:
    from ..field import GameField


class Figure(ABC):
    def __init__(self, color: Literal["black", "white"]):
        """Initialize a Figure with a specified color.

        Args:
            color (Literal["black", "white"]): The color of the figure.
        """
        self.color: Literal["black", "white"] = color

    @abstractmethod
    def _get_moves(self, pos: str) -> list:
        """Return a list of basic moves for a figure from a given position.

        This method should not be used directly. Use get_available_moves for move validation.

        Args:
            pos (str): The current position in algebraic notation (e.g., 'a1').

        Returns:
            list: A list (or nested list for sliding pieces) of potential moves.
        """
        pass

    @abstractmethod
    def get_available_moves(self, pos: str, board: GameField) -> list:
        """Return a list of available moves for a figure from a given position.

        The method calculates legal moves based on basic moves and checks for possible captures.

        Args:
            pos (str): The current position in algebraic notation (e.g., 'a1').
            board (GameField): The game board containing the positions of all figures.

        Returns:
            list: A list of legal moves for the figure.
        """
        pass


class Rook(Figure):
    def __str__(self):
        """Return the Unicode symbol for the rook."""
        return "♖" if self.color == "white" else "♜"

    def _get_moves(self, pos: str) -> list[list[str]]:
        """Calculate potential moves for the rook in each cardinal direction.

        Iterates in each direction until the edge of the board is reached.

        Args:
            pos (str): The starting position of the rook in algebraic notation (e.g., 'a1').

        Returns:
            list[list[str]]: A list of lists, where each sublist contains moves in one direction.
        """
        moves = []
        col = pos[0]
        row = int(pos[1]) - 1
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dcol, drow in directions:
            moves_vector = []
            i = 1
            while True:
                new_col = ord(col) + dcol * i
                new_row = row + drow * i
                if new_col < ord('a') or new_col > ord('h') or new_row < 0 or new_row > 7:
                    break
                moves_vector.append(f"{chr(new_col)}{new_row + 1}")
                i += 1
            moves.append(moves_vector)
        return moves

    def get_available_moves(self, pos: str, board: GameField) -> list:
        """Determine legal moves for the rook by checking for obstructions and potential captures.

        Args:
            pos (str): The starting position of the rook in algebraic notation.
            board (GameField): The game board used to validate moves.

        Returns:
            list: A list of legal moves available to the rook.
        """
        moves = self._get_moves(pos)
        result = []
        for vector in moves:
            for move in vector:
                figure = board.get_figure(move)
                if figure is None:
                    result.append(move)
                    continue
                elif figure.color != self.color:
                    result.append(move)
                    break
                else:
                    break
        return result


class Knight(Figure):
    def __str__(self):
        """Return the Unicode symbol for the knight."""
        return "♘" if self.color == "white" else "♞"

    def _get_moves(self, pos: str) -> list:
        """Compute all potential moves for the knight from a given position.

        The knight moves in an L-shape pattern.

        Args:
            pos (str): The starting position of the knight in algebraic notation.

        Returns:
            list: A list of potential positions the knight can move to.
        """
        moves = []
        col = pos[0]
        row = int(pos[1]) - 1
        knight_moves = [(2, 1), (2, -1), (-2, 1), (-2, -1),
                        (1, 2), (1, -2), (-1, 2), (-1, -2)]
        for dcol, drow in knight_moves:
            new_col = ord(col) + dcol
            new_row = row + drow
            if ord('a') <= new_col <= ord('h') and 0 <= new_row <= 7:
                moves.append(f"{chr(new_col)}{new_row + 1}")
        return moves

    def get_available_moves(self, pos: str, board: GameField) -> list:
        """Return legal moves for the knight considering board constraints.

        Checks moves for validity and ensures that moves do not capture pieces of the same color.

        Args:
            pos (str): The starting position of the knight in algebraic notation.
            board (GameField): The game board to evaluate move legality.

        Returns:
            list: A list of legal moves available to the knight.
        """
        moves = self._get_moves(pos)
        result = []
        for move in moves:
            figure = board.get_figure(move)
            if figure is None or figure.color != self.color:
                result.append(move)
        return result


class Bishop(Figure):
    def __str__(self):
        """Return the Unicode symbol for the bishop."""
        return "♗" if self.color == "white" else "♝"

    def _get_moves(self, pos: str) -> list[list[str]]:
        """Compute diagonal moves for the bishop from a given position.

        Iterates diagonally until the edge of the board is reached.

        Args:
            pos (str): The bishop's starting position in algebraic notation.

        Returns:
            list[list[str]]: A list of lists, each containing potential diagonal moves.
        """
        moves = []
        col = pos[0]
        row = int(pos[1]) - 1
        directions = [(1, 1), (-1, -1), (1, -1), (-1, 1)]
        for dcol, drow in directions:
            moves_vector = []
            i = 1
            while True:
                new_col = ord(col) + dcol * i
                new_row = row + drow * i
                if new_col < ord('a') or new_col > ord('h') or new_row < 0 or new_row > 7:
                    break
                moves_vector.append(f"{chr(new_col)}{new_row + 1}")
                i += 1
            moves.append(moves_vector)
        return moves

    def get_available_moves(self, pos: str, board: GameField) -> list:
        """Determine legal diagonal moves for the bishop by filtering based on obstructions and captures.

        Args:
            pos (str): The bishop's starting position in algebraic notation.
            board (GameField): The game board to validate moves.

        Returns:
            list: A list of legal moves available to the bishop.
        """
        moves = self._get_moves(pos)
        result = []
        for vector in moves:
            for move in vector:
                figure = board.get_figure(move)
                if figure is None:
                    result.append(move)
                    continue
                elif figure.color != self.color:
                    result.append(move)
                    break
                else:
                    break
        return result


class Queen(Figure):
    def __str__(self):
        """Return the Unicode symbol for the queen."""
        return "♕" if self.color == "white" else "♛"

    def _get_moves(self, pos: str) -> list[list[str]]:
        """Compute all potential moves for the queen from a given position.

        Combines the moves of the rook and bishop.

        Args:
            pos (str): The queen's starting position in algebraic notation.

        Returns:
            list[list[str]]: A list of lists, each containing potential moves.
        """
        moves = []
        col = pos[0]
        row = int(pos[1]) - 1
        directions = [
            (1, 0), (-1, 0), (0, 1), (0, -1),
            (1, 1), (-1, -1), (1, -1), (-1, 1)
        ]
        for dcol, drow in directions:
            moves_vector = []
            i = 1
            while True:
                new_col = ord(col) + dcol * i
                new_row = row + drow * i
                if new_col < ord('a') or new_col > ord('h') or new_row < 0 or new_row > 7:
                    break
                moves_vector.append(f"{chr(new_col)}{new_row + 1}")
                i += 1
            moves.append(moves_vector)
        return moves

    def get_available_moves(self, pos: str, board: GameField) -> list:
        """Determine legal moves for the queen by filtering moves based on board obstructions and captures.

        Args:
            pos (str): The queen's starting position in algebraic notation.
            board (GameField): The game board to validate moves.

        Returns:
            list: A list of legal moves available to the queen.
        """
        moves = self._get_moves(pos)
        result = []
        for vector in moves:
            for move in vector:
                figure = board.get_figure(move)
                if figure is None:
                    result.append(move)
                    continue
                elif figure.color != self.color:
                    result.append(move)
                    break
                else:
                    break
        return result


class King(Figure):
    def __str__(self):
        """Return the Unicode symbol for the king."""
        return "♔" if self.color == "white" else "♚"

    def _get_moves(self, pos: str) -> list:
        """Compute potential moves for the king from a given position.

        The king can move one square in any direction.

        Args:
            pos (str): The king's starting position in algebraic notation.

        Returns:
            list: A list of positions the king can move to.
        """
        moves = []
        col = pos[0]
        row = int(pos[1]) - 1
        directions = [
            (0, 1), (0, -1), (1, 0), (1, 1),
            (1, -1), (-1, 0), (-1, 1), (-1, -1)
        ]
        for dcol, drow in directions:
            new_col = ord(col) + dcol
            new_row = row + drow
            if new_col < ord('a') or new_col > ord('h') or new_row < 0 or new_row > 7:
                continue
            moves.append(f"{chr(new_col)}{new_row + 1}")
        return moves

    def get_available_moves(self, pos: str, board: GameField) -> list:
        """Determine legal moves for the king by filtering out moves blocked by same-colored pieces.

        Args:
            pos (str): The king's starting position in algebraic notation.
            board (GameField): The game board used to validate moves.

        Returns:
            list: A list of legal moves available to the king.
        """
        moves = self._get_moves(pos)
        result = []
        for move in moves:
            figure = board.get_figure(move)
            if figure is None:
                result.append(move)
            elif figure.color != self.color:
                result.append(move)
        return result


class Pawn(Figure):
    def __str__(self):
        """Return the Unicode symbol for the pawn."""
        return "♙" if self.color == "white" else "♟"

    def _get_moves(self, pos: str) -> list:
        """Compute forward moves for the pawn from a given position.

        Accounts for single-step and initial double-step moves based on the pawn's color.

        Args:
            pos (str): The pawn's starting position in algebraic notation.

        Returns:
            list: A list of potential forward moves for the pawn.
        """
        row = int(pos[1]) - 1
        col = pos[0].lower()
        moves = []
        if self.color == "white":
            direction = 1
            start_row = 1
        else:
            direction = -1
            start_row = 6
        next_row = row + direction
        if 0 <= next_row <= 7:
            moves.append(f"{col}{next_row + 1}")
            if row == start_row:
                next_row2 = row + 2 * direction
                if 0 <= next_row2 <= 7:
                    moves.append(f"{col}{next_row2 + 1}")
        return moves

    def get_available_moves(self, pos: str, board: GameField) -> list:
        """Determine legal moves for the pawn, including diagonal captures.

        Evaluates forward moves and adds diagonal moves if an opponent's piece is present.

        Args:
            pos (str): The pawn's starting position in algebraic notation.
            board (GameField): The game board used to validate moves.

        Returns:
            list: A list of legal moves available to the pawn.
        """
        moves = self._get_moves(pos)
        result = []
        for i in range(len(moves)):
            move = moves[i]
            move_col = move[0]
            move_row = move[1]
            if i == 0:
                diag_moves = []
                for num in (-1, 1):
                    if "a" <= chr(ord(move_col) + num) <= "h":
                        diag_moves.append(f"{chr(ord(move_col) + num)}{move_row}")

                figure = board.get_figure(move)
                if figure is None:
                    result.append(move)

                for diag_move in diag_moves:
                    figure = board.get_figure(diag_move)
                    if figure is None:
                        continue
                    elif figure.color != self.color:
                        result.append(diag_move)
            if i == 1:
                figure = board.get_figure(move)
                if figure is None:
                    result.append(move)

        return result
