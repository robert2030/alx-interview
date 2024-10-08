#!/usr/bin/python3
# lock boxes 
def canUnlockAll(boxes):
    """
    Solution to the lockboxes problem
    """
    if (type(boxes)) is not list:
        return False
    elif (len(boxes)) == 0:
        return False

    for k in range(1, len(boxes) - 1):
        boxes_seen = False
        for idx in range(len(boxes)):
            boxes_seen = k in boxes[idx] and k != idx
            if boxes_seen:
                break
        if boxes_seen is False:
            return boxes_seen
    return True
