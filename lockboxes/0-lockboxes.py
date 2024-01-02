#!/usr/bin/env python3
"""summary
"""


def canUnlockAll(boxes):
    """Method that determines if all the boxes can be opened

    Args:
        boxes (nested list): list of the boxes with the keys inside

    Returns:
        possibility (boolean): if all the boxes can be opened
    """

    # Using a search algorithm
    explored = []
    frontier = [0]
    while True:
        if frontier == []:
            if len(explored) == len(boxes):
                return True
            else:
                return False
        for key in boxes[frontier[0]]:
            if frontier[0] not in explored:
                explored.append(frontier[0])
            if key not in explored:
                frontier.append(key)
        frontier.pop(0)
