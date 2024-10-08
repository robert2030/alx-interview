#!/usr/bin/python3
# lock boxes 
def canUnlockAll(boxes):
    n = len(boxes)  # Number of boxes
    opened = set([0])  # Start with box 0 unlocked
    stack = [0]  # Start exploring from box 0
    
    # Explore the boxes while there are keys to process
    while stack:
        box = stack.pop()  # Take the last box opened
        for key in boxes[box]:
            if key not in opened and key < n:  # Only unlock unopened boxes within bounds
                opened.add(key)  # Mark the box as opened
                stack.append(key)  # Add the new box to explore further

    # Return True if all boxes are opened
    return len(opened) == n

