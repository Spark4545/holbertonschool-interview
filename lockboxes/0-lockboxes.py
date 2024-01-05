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
    opened = []
    keys = [0]
    while True:
        # Exit condition
        if keys == []:  # When all keys have been used
            if len(boxes) == len(opened):  # if the number of boxes is equal to the number of opened boxes
                return True
            else:
                return False

        # Get the key and remove it from the list
        current_key = keys[0]
        keys.pop(0)

        # If the current key opens a box that exists
        if current_key < len(boxes):
            opened.append(current_key)
            # Main loop
            for key in boxes[current_key]:
                if key not in opened and key not in keys:
                    keys.append(key)
        else:
            pass
