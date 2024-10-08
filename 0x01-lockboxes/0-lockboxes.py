#!/usr/bin/python3
# lock boxes 
#!/usr/bin/python3
"""
Module to determine if all boxes can be unlocked.
"""

def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked.

    Args:
        boxes (list): A list of lists containing keys to other boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)  # Number of boxes
    opened = set([0])  # Start with box 0 unlocked
    stack = [0]  # Stack for boxes to explore

    # Explore the boxes while there are keys to process
    while stack:
        box = stack.pop()  # Take the last box opened
        for key in boxes[box]:
            if key not in opened and key < n:  # Only unlock unopened boxes within bounds
                opened.add(key)  # Mark the box as opened
                stack.append(key)  # Add the new box to explore further

    # Return True if all boxes are opened
    return len(opened) == n

