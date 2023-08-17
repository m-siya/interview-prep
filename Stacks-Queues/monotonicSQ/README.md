## Resources
- https://leetcode.com/discuss/study-guide/2347639/A-comprehensive-guide-and-template-for-monotonic-stack-based-problems
- https://1e9.medium.com/monotonic-queue-notes-980a019d5793#:~:text=Definition,entirely%20in%20non%2Ddecreasing%20order.
 

- used to solve problems involving next greater element, next smaller element, previous greater element and previous smaller element. 
 
## Time Complexity
- It can be argued that no element is accessed more than four times (a constant) - one, when comparing its value with the item in the stack (while conditional). two, when pushing the item in the stack. three, when comparing this item in the stack with the current item being iterated (while conditional again). four, when popping the item out of stack. As a result, the time complexity of this algorithm is linear. - O(n) where n is the number of elements in the array.