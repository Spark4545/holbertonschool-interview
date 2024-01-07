# Lockboxes

## Context

You have ```n``` number of locked boxes in front of you. Each box is numbered sequentially
from ```0``` to ```n - 1``` and each box may contain keys to the other boxes. <br>
<br>
Write a method that determines if all the boxes can be opened. <br>
Prototype: ```def canUnlockAll(boxes)``` <br>
```boxes``` is a list of lists <br>
A key with the same number as a box opens that box <br>
We can assume all keys will be positive integers but there can be keys that don't have boxes <br>
The first box ```boxes[0]``` will always be open <br>
Return ```True``` if all boxes can be opened, and ```False``` if not <br>

## Example

```
boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))
```

Result:

```
True
True
False
```
