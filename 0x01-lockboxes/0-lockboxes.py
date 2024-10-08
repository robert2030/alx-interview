#!/usr/bin/python3
# lock boxes 
#!/usr/bin/python3
"""
Module to determine if all boxes can be unlocked.
"""

def canUnlockAll(boxes):
    """Checks if all boxes can be opened

        Args: boxes (List): List of Lists of integers

        Returns:
            (bool): Tells whether all items in the list can be opened
    """
    listSize = len(boxes)
    openedBoxes = [False] * listSize

    stack = [0]

    while stack:
        currentBox = stack.pop()

        openedBoxes[currentBox] = True
        currentKeys = boxes[currentBox]
        for key in currentKeys:
            if key in range(listSize) and openedBoxes[key] is False and key not in stack:
                stack.append(key)

    return all(openedBoxes)
