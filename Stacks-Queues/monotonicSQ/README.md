## Resources
- https://leetcode.com/discuss/study-guide/2347639/A-comprehensive-guide-and-template-for-monotonic-stack-based-problems
- https://1e9.medium.com/monotonic-queue-notes-980a019d5793#:~:text=Definition,entirely%20in%20non%2Ddecreasing%20order.
- https://dwf.dev/blog/2024/04/26/2024/monotonic-stacks-queues/
 

- used to solve problems involving next greater element, next smaller element, previous greater element and previous smaller element, accessing the maximum or minimum value of a contiguous subarray or sliding window

- types of monotonic stack:
    1. Strictly increasing - every element of the stack is strictly greater than the previous element. Example - [1, 4, 5, 8, 9]
    2. Non-decreasing - every element of the stack is greater than or equal to the previous element. Example - [1, 4, 5, 5, 8, 9, 9]
    3. Strictly decreasing - every element of the stack is strictly smaller than the previous element - [9, 8, 5, 4, 1]
    4. Non-increasing - every element of the stack is smaller than or equal to the previous element. - [9, 9, 8, 5, 5, 4, 1]

- mono decreasing stack for next greater, previous greater
- mono increasing stack for next smaller, prev smaller

- special care must be taken when adding values to a monotonic stack or deque to ensure its monotonicity invariant remains intact. Specifically, adding value x means first removing all other values that would cause the invariant to be broken should x be added to the stack or queue in its current state — only then should x be added. Since the collection of values being maintained is a stack or deque, additions generally happen from the right

- Adding values generally happens from the right. Removal of values, which typically precedes the addition of new values, also generally happens from the right. Why? Because values that would otherwise break the invariant are effectively popped from the top/right before adding the new value to the top/right

- Removing elements from the left (when a queue-like operation is needed): In some cases (e.g., sliding windows), we may want to remove an element in our collection from the left. For sliding window problems especially, window values are generally added as the right endpoint advances and removed as the left endpoint advances. Since the leftmost values in our collection are always the "oldest", it makes sense that in certain scenarios we might want to remove the leftmost value.
 
- once every element in an input array has been iterated over, all remaining elements in the collection are those which had no such next larger/smaller (or equal) value based on the monotonic invariant being maintained for the collection

- **next larger/smaller value** - if B is the value being added to the collection, then every value A popped from collection has B as their next larger/smaller value where larger/smaller depends on the monotonic variant of stack.  After every element has been iterated over, all remaining elements in stack are those which have no such next larger/smaller value.

- **prev larger/smaller value** - in next larger/smaller value, effectively, determining how B related to each element removed from collection. think about what happens when we *stop* removing elements. after stopping, the rightmost element is B's previous larger/smaller value.

```python

def fn_next(nums):
    n = len(nums)
    ans = [None] * n
    stack = []
    for i in range(n):
        val_B = nums[i]

        while stack and nums[stack[-1]] ? val_B:
            idx_val_A = stack.pop()
            ans[idx_val_A] = val_B
        
        stack.append(i)
    
    #process elements that never had a "next":
    while stack:
        idx_val_A = stack.pop()
        ans[idx_val_A] = -1
    
    return ans


def fn_prev(nums):
    n = len(nums)
    ans = [None] * n
    stack = []

    for i in range(n):
        val_A = nums[i]

        while stack and nums[stack[-1]] ? val_A:
            stack.pop()
        
        if stack:
            idx_val_B = stack[-1]
            val_B = nums[idx_val_B]
            ans[i] = val_B
        else:
            ans[i] = -1
        
        stack.append(i)
    
    return ans

```

## Time Complexity
- It can be argued that no element is accessed more than four times (a constant) - one, when comparing its value with the item in the stack (while conditional). two, when pushing the item in the stack. three, when comparing this item in the stack with the current item being iterated (while conditional again). four, when popping the item out of stack. As a result, the time complexity of this algorithm is linear. - O(n) where n is the number of elements in the array.