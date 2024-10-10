#!/usr/bin/python3
""" Lockboxes """


def canUnlockAll(boxes):
    """
    Args: boxes - the number of locked boxes

    Return: True if all boxes can be opened, else return False
    """
    n = len(boxes)
    unlocked_boxes = []

    for i in range(0, n - 1):
        for key in boxes[i]:
            if key not in unlocked_boxes and key < n:
                unlocked_boxes.append(key)
    if len(unlocked) == len(boxes):
        return True
    return False
