from typing import List
def canUnlockBoxes(boxes: List[List[int]]):
    
    keys = [0]
    
    for key in keys:
        for subKey in boxes[key]:
            if subKey < len(boxes) and not subKey in keys:
                keys.append(subKey)
    
    print(keys)
    if len(keys) != len(boxes):
        return False
    
    return True


box1 = [[1], [2], [3], [4], []]
box2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
box3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]

print(canUnlockBoxes(box1))
print(canUnlockBoxes(box2))
print(canUnlockBoxes(box3))

