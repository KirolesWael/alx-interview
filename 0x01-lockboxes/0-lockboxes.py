#!/usr/bin/python3

def canUnlockAll(boxes):
    boxesopened = {0}
    open_box(boxes[0], boxesopened, boxes)
    if (len(boxesopened) == len(boxes)):
        return True
    return False

def open_box(box, boxesopened, boxes):
    if not box:
        return
    for i in box:
        if i in boxesopened:
            continue
        else:
            boxesopened.add(i)
            open_box(boxes[i], boxesopened, boxes)

