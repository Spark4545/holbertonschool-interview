#!/usr/bin/python3
""" Present with a list of lists, the nested list represent boxes
    with keys inside them. The method needs to return the
    possibility of all boxes being unlocked.
    The first box is always unlocked.
"""


def canUnlockAll(boxes):
    """Method that determines if all the boxes can be opened

    Args:
        boxes (nested list): list of the boxes with the keys inside

    Returns:
        boolean: if all the boxes can be opened return True,
        else return False
    """

    # Using a search algorithm
    opened = []
    keys = [0]
    while True:
        # Exit condition
        if keys == []:  # When all keys have been used
            if len(boxes) == len(opened):  # if the number of boxes is equal to the number of opened boxes
                return True
            else:
                return False

        else:
            current_key = keys[0]
            keys.pop(0)

            if current_key < len(boxes):
                opened.append(current_key)
                for key in boxes[current_key]:
                    if key not in opened and key not in keys:
                        keys.append(key)
