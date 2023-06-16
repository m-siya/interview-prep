## Algorithms

### Flood Fill

like the bucket tool in paint programs. 
1. Take the position of the starting point.
2. Decide wether you want to go in 4 directions (N, S, W, E) or 8 directions (N, S, W, E, NW, NE, SW, SE).
3. Choose a replacement color and a target color.
4. Travel in those directions.
5. If the tile you land on is a target, reaplce it with the chosen color.
6. Repeat 4 and 5 until you’ve been everywhere within the boundaries.

[code](floodFill.py)

---------------------------