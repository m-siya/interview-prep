- types of subarray problems 
    1. count subarrays with an "equals to" condition
        - involves use of prefix sum/hashmap 
    2. count subarrays with an "greater than/less than" condition
        - involves use of sliding window because you'll need to consider 
        all subarrays in an interval
        - and sliding window is just two pointers. and problems solved by two pointers need the following :
        (ref: https://leetcode.com/problems/subarray-sum-equals-k/solutions/301242/general-summary-of-what-kind-of-problem-can-cannot-solved-by-two-pointers/)
            1. If a wider scope of the sliding window is valid, the narrower scope of that wider scope is valid mush hold.
            2. If a narrower scope of the sliding window is invalid, the wider scope of that narrower scope is invalid mush hold.
    
