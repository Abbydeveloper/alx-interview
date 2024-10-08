#!/usr/bin/python3
""" Lockboxes """


def canUnlockAll(boxes):
    """
    Args: boxes - the number of locked boxes

    Return: True if all boxes can be opened, else return False
    """

    if not boxes or type(boxes) is not list:
        return False

    n = len(boxes)
    unlocked_boxes = [0]

    for i in unlocked_boxes:
        for key in boxes[i]:
            if key not in unlocked_boxes and key < n:
                unlocked_boxes.append(key)
    if len(unlocked_boxes) == len(boxes):
        return True
    return False
