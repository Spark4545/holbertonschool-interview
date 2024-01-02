#!/usr/bin/python3
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
        # If there are no boxes to explore
        if frontier == []:
            if len(explored) == len(boxes):
                return True
            else:
                return False
        if frontier[0] > len(boxes):
            return False
        for key in boxes[frontier[0]]:
            # Add the current box to the explored list
            if frontier[0] not in explored:
                explored.append(frontier[0])
            # Case when the box has no key in it

            # if the key is for an unexplored box, add the key to the frontier
            if key not in explored:
                frontier.append(key)
        if boxes[frontier[0]] == []:
            explored.append(frontier[0])
        # Remove the explored box from the frontier
        frontier.pop(0)

        # print("Explored :", end="")
        # print(explored)
        # print("Frontier :", end="")
        # print(frontier)
        # print("=========")
