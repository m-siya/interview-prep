### Moore Majority Voting Algorithm

to find majority of a sequence using linear time O(n) and O(1).
resource :
https://gregable.com/2013/10/majority-vote-algorithm-find-majority.html

---------------------------

### Misra-Gries heavy hitters Algorithm
Given is a bag b of n elements and an integer k ≥ 2. Find the values that occur more than n ÷ k times in b. The Misra-Gries algorithm solves the problem by making two passes over the values in b, while storing at most k values from b and their number of occurrences during the course of the algorithm.

--------------------

### Binary Search

resource -> https://leetcode.com/discuss/study-guide/3726061/mastering-binary-search-technique-a-comprehensive-guide

--------------------------------

### Sweep Line Algorithm
- for events in sorted order with a start and end
- at start, increment by 1; at end, decrement by 1



------------------

### Solving substring questions

- problem statement - find a substring of a given string that satisfies some given criteria
- use hashmaps + two pointers

```Python
def find_substring(s: str) -> int:
    map_array = [0] * 26

    begin, end = 0, 0
    substr_length = 0

    #init hashmap
    
    while end < len(s) :
        #modify counts
        if map_array[s]

        while #counter condition:

            #update substr_length if criteria satisfied

            #increase begin to make substr invalid again

            #modify counts
            if map_array[s[begin]]

        #update substr_length if criteria satisfiedd

    return substr_length
```
--------------------------

### Things to Remember

1. No. of subarrays (seq of contiguous elements in an array) of an array of len N = N(N + 1) / 2

