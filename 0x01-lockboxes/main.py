#!/usr/bin/python3
"""
Test the canUnlockAll function.
"""

canUnlockAll = __import__('0-lockboxes').canUnlockAll

# Test cases
boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))  # Expected: True

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))  # Expected: True

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))  # Expected: False

