# ### RANGE SUM QUERY MUTABLE

# Given an integer array nums, handle multiple queries of the following types:

# Update the value of an element in nums.
# Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
# Implement the NumArray class:

# NumArray(int[] nums) Initializes the object with the integer array nums.
# void update(int index, int val) Updates the value of nums[index] to be val.
# int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

# https://leetcode.com/problems/range-sum-query-mutable/description/

class SegmentTreeNode:
    def __init__(self, lo, hi, val=0, leftChild=None, rightChild=None):
        self.lo = lo
        self.hi = hi
        self.val = val
        self.left = leftChild
        self.right = rightChild
    

def merge(x1: SegmentTreeNode, x2: SegmentTreeNode):
    return x1.val + x2.val

def build(arr: list[int], lo: int, hi: int) -> Optional[SegmentTreeNode]:
    if lo == hi:
        return SegmentTreeNode(lo, hi, arr[lo])
    
    root = SegmentTreeNode(lo, hi)
    mid = lo + (hi - lo) // 2
    root.left = build(arr, lo, mid)
    root.right = build(arr, mid + 1, hi)

    root.val = merge(root.left, root.right)
    return root

class NumArray:

    def __init__(self, nums: List[int]):
        self.root = build(nums, 0, len(nums) - 1)
        
    def update(self, index: int, val: int) -> None:

        def _update(root, index, val):
            if root.lo == root.hi == index:
                root.val = val
                return 
            
            mid = root.lo + (root.hi - root.lo) // 2
            if index <= mid:
                _update(root.left, index, val)
            else:
                _update(root.right, index, val)
            
            root.val = merge(root.left, root.right)
            return 
        
        _update(self.root, index, val)
        

    def sumRange(self, left: int, right: int) -> int:

        def _sumRange(root, left, right):
            if left > root.hi or right < root.lo:
                return 0
            
            if root.lo == left and root.hi == right:
                return root.val
            
            mid = root.lo + (root.hi - root.lo) // 2
            return _sumRange(root.left, left, min(right, mid)) + _sumRange(root.right, max(mid + 1, left), right)
        
        return  _sumRange(self.root, left, right)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)