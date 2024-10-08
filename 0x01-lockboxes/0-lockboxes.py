#!/usr/bin/python3
# lock boxes 
def canUnlockAll(boxes):
    n = len(boxes)
    opened = set([0])  # Start with the first box opened
    keys = [0]  # Start with the keys from the first box (box 0)
    
    while keys:
        current_box = keys.pop()  # Take the last box to open
        for key in boxes[current_box]:
            if key not in opened and key < n:
                opened.add(key)
                keys.append(key)  # Add the keys from this new box to be opened
                
    return len(opened) == n
