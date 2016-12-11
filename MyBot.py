""" An energy based bot
"""

import numpy as np

import hlt
from hlt import NORTH, EAST, SOUTH, WEST, STILL, Move, Square
import random


my_id, game_map = hlt.get_init()
hlt.send_init("MyPythonBot")

def build_player_square_maps(game_state):
    # {int : [Square]}
    playerid_to_squares = {}
    # {Square: int}
    square_to_playerid = {}
    for square in game_state:
        if square.owner in playerid_to_squares:
            playerid_to_squares[square.owner].append(square)
        else:
            playerid_to_squares[square.owner] = [square]

        square_to_playerid[square] = square.owner
    return square_to_playerid, playerid_to_squares


def hamiltonian(game_state):
    """ Computes the energy of the game state.
    """
    # evaluate energy of position
    pass

def simulate_move(curr_state, move):
    """ Simulate the result of applying move to game_map. Hopefully

    Args:
      curr_state: a game state - GameMap
      move: move specification, one for every piece owned by player - [(Square, direction)]

    Returns:
      next_state: the simulation next state - GameMap

    """
    pid_to_sqs, sq_to_pid = build_player_square_maps()

    assert len(move) == len(pid_to_sqs[0])
    assert len(set([sq for sq, _ in moves])) == len(move)
    assert np.array([(sq.owner == 0) for sq, _ in move])

    increments = np.zeros((curr_state.width, curr_state.height))
    balance_decrements = np.zeros((curr_state.width, curr_state.height))
    attack_decrements = np.zeros((curr_state.width, curr_state.height))
    enemy_attack_decrements = np.zeros((curr_state.width, curr_state.height))

    # first pass
    # calculate increment and decrement arrays
    for sq, direction in move:
        target = curr_state.get_target(sq, direction)
        # accumulate logic
        if target == sq:
            increments[sq.x, sq.y] += sq.production

        balance_decrements[sq.x, sq.y] -= sq.strength
        increments[target.x, target.y] += sq.strength
        # overkill logic
        for direction, nbr_sq in enumerate(curr_state.neighbors(target, include_self=True)):
            if nbr_sq.owner != 0:
                attack_decrements[nbr_sq.x, nbr_sq.y] += sq.strength
                enemy_attack_decrements[target.x, target.y] += nbr_sq.strength
            if target.owner != 0


    # second pass
    # apply increment and decrement arrays
    for x_idx in range(curr_state.width):
        for y_idx in range(curr_state.height):
            curr_sq = curr_state.contents[y_idx][x_idx]
            if curr_sq.owner != 0:
                curr_sq.strength += increments[x_idx, y_idx]
                curr_sq.strength -= balance_decrements[x_idx, y_idx]
                curr_sq.strength -= attack_decrements[x_idx, y_idx]

















while True:
    game_map.get_frame()
    moves = []
    hlt.send_frame(moves)
