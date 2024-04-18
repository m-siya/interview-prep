### BAG OF TOKENS

# You start with an initial power of power, an initial score of 0, and a bag of tokens given as an integer array tokens, where each tokens[i] denotes the value of tokeni.

# Your goal is to maximize the total score by strategically playing these tokens. In one move, you can play an unplayed token in one of the two ways (but not both for the same token):

# Face-up: If your current power is at least tokens[i], you may play tokeni, losing tokens[i] power and gaining 1 score.
# Face-down: If your current score is at least 1, you may play tokeni, gaining tokens[i] power and losing 1 score.
# Return the maximum possible score you can achieve after playing any number of tokens.

# https://leetcode.com/problems/bag-of-tokens/description/

#tc: O(nlogn)
#sc: O(1)

# because we can use tokens in any order, dp doesnt work

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        
        tokens.sort()
        left, right = 0, len(tokens) - 1

        curr_score = 0
        curr_power = power

        while left <= right:
            if curr_power >= tokens[left]:
                curr_score += 1
                curr_power -= tokens[left]
                left += 1
            elif curr_score >= 1 and (right - left > 1): #dont buy power if no futher chances to increase score
                curr_score -= 1
                curr_power += tokens[right]
                right -= 1
            else:
                break
           # print(left, right, curr_power, curr_score)
        return curr_score
            

