### Tips

1. A binary search tree has the property that the sequence obtained through an in-order traversal is a sorted array.

Therefore, we only need to perform an in-order traversal and calculate the absolute difference between each pair of adjacent numbers. The minimum difference obtained will be the desired result. 