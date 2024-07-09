## SEGMENT TREES

### resources 
- https://cp-algorithms.com/data_structures/segment_tree.html
- https://www.youtube.com/watch?v=-dUiRtJ8ot0
- https://aden-q.github.io/segment-tree/ -> for impl, also includes arr impl

### theory

- A Segment Tree is a data structure that stores information about array intervals as a tree. This allows answering range queries over an array efficiently, while still being flexible enough to allow quick modification of the array. 

- This includes finding the sum of consecutive array elements or finding the minimum element in a such a range in O(logn) time.

- Between answering such queries, the Segment Tree allows modifying the array by replacing one element, or even changing the elements of a whole subsegment (e.g. assigning all element a[l..r] to any value, or adding a value to all element in the subsegment).

- require linear memory - 4n vertices for array of size n


#### simple segment tree
- given an array a[0..n-1], find sum of elements between indices l and r and also handle changing values of elements in the array. Do this both in O(logn) time

- simple arr approach can update elements in O(1) time but needs O(n) to compute each sum query. Prefix sums can compute sums in O(1) but need O(n) for updating values

- compute and store the sum of the elements of the whole array, i.e. the sum of the segment a[0..n-1] . We then split the array into two halves a[0..n/2-1] and a[n/2..n-1] and compute the sum of each halve and store them. Each of these two halves in turn are split in half, and so on until all segments reach size 1.

- approx 4n vertices, height of tree is O(logn)


#### implementation

```python
class SegmentTreeNode:
    def __init__(self, lo, hi, val=0, leftChild=None, rightChild=None):
        self.lo = lo
        self.hi = hi
        self.val = val
        self.leftChild = leftChild
        self.rightChild = rightChild
    
def merge(self, x1: SegmentTreeNode, x2: SegmentTreeNode):
    return x1.val + x2.val
    
# run in O(N) time where N is max range
def build(self, arr: list[int], lo: int, hi: int) -> Optional[SegmentTreeNode]:
    if lo == hi:
        return SegmentTreeNode(lo, hi, arr[lo])
    
    root = SegmentTreeNode(lo, hi)
    mid = lo + (hi - lo) // 2
    root.left = build(arr, lo, mid)
    root.right = build(arr, mid + 1, hi)

    root.val = merge(root.left, root.right)

    return root

# run i O(logN + k) time where N is max range and k is number of retrived segments. 
def rangeQuery(root: SegmentTreeNode, left: int, right: int) -> int:
    # if query [left..right] does not overlap with root range [lo..hi]
    if left > root.hi or right < root.lo:
        return 0>
    
    # if query is matching exactly
    if root.lo == left and root.hi == right:
        return root.val
    
    mid = root.lo + (root.hi - root.lo) // 2
    return rangeQuery(root.left, left, min(right, mid)) + rangeQuery(root.right, max(mid + 1, left), right)

# run in O(logN) time
def update(root: SegmentTreeNode, index: int, val: int) -> None:
    if root.lo == root.hi == index:
        root.val = val
        return

    mid = root.lo + (root.hi - root.lo) // 2
    if index <= mid:
        update(root.left, index, val)
    else:
        update(root.right, index, val)
    
    root.val = merge(root.left, root.right) #update curr root
    return



```