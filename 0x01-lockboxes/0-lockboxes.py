#!/usr/bin/python3
""" Lockboxes Module
"""


def canUnlockAll(boxes):
    """ Checks if all boxes in a list can be unlocked

    Args:
        boxes(list): list of lists representing boxes with keys to other boxes

    Returns:
        (bool): True if alse boxes are unlockable, otherwise False
    """
    n = len(boxes)
    keys = [0]
    opened_boxes = []

    while keys:
        # dequeue key
        key = keys.pop(0)

        # add key to opened boxes
        if key not in opened_boxes:
            opened_boxes.append(key)

            # get new keys from opened box and enque them
            for new_key in boxes[key]:
                if new_key < n and new_key not in opened_boxes:
                    keys.append(new_key)

    return len(opened_boxes) == n
