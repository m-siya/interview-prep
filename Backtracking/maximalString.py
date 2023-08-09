### MAXIMAL STRING

# Given a string A and integer B, what is maximal lexicographical string that can be made from A if you do atmost B swaps.

# Problem Constraints
# 1 <= |A| <= 9

# A contains only digits from 0 to 9.

# 1 <= B <= 5



# Input Format
# First argument is string A.

# Second argument is integer B.



# Output Format
# Return a string, the naswer to the problem.



# Example Input
# Input 1:

# A = "254"
# B = 1
# Input 2:

# A = "254"
# B = 2


# Example Output
# Output 1:

#  524
# Output 2:

#  542


# Example Explanation
# Explanation 1:

#  Swap 2 and 5.
# Explanation 2:

# Swap 2 and 5 then swap 4 and 2.

def solve(string, max_swaps):
    #write your code here
    max_num = 0
    n = len(string)
    string = list(string)
    
    def backtrack(string, swaps):
        nonlocal max_num
        max_num = max(max_num, int(''.join(string)))
      #  print(string, swaps)
        if swaps == max_swaps:
            return 
        
        for first_num in range(n):
            for sec_num in range(first_num + 1, n):
                string[first_num], string[sec_num] = string[sec_num], string[first_num]
                backtrack(string, swaps + 1)
                string[first_num], string[sec_num] = string[sec_num], string[first_num]

    backtrack(string, 0)
    return max_num