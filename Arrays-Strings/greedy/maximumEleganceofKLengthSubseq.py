# ### MAXIMUM ELEGANCE OF A K LENGTH SUBSEQUENCE

# You are given a 0-indexed 2D integer array items of length n and an integer k.

# items[i] = [profiti, categoryi], where profiti and categoryi denote the profit and category of the ith item respectively.

# Let's define the elegance of a subsequence of items as total_profit + distinct_categories2, where total_profit is the sum of all profits in the subsequence, and distinct_categories is the number of distinct categories from all the categories in the selected subsequence.

# Your task is to find the maximum elegance from all subsequences of size k in items.

# Return an integer denoting the maximum elegance of a subsequence of items with size exactly k.

# Note: A subsequence of an array is a new array generated from the original array by deleting some elements (possibly none) without changing the remaining elements' relative order.

# https://leetcode.com/problems/maximum-elegance-of-a-k-length-subsequence/description/

# method - sort the items in non increasing order of profits. choose first k items which represent max
# price. now for the remaining n - k items, the only situation we would want to include them
# in out subsequence is if they are contributing a not seen before category and this inclusion
# is increasing profit. in that case, we would replace it with the item with lowest profit and whose
# category is already included in the subsequence. 
# do this for all n - k items and at each point update max_elegance

# tc - O(nlogn), sc - O(n)

class Solution:
    def findMaximumElegance(self, items: List[List[int]], k: int) -> int:
        items.sort(key = lambda item: item[0], reverse=True)

        max_elegance = 0
        curr_profit = 0
        seen = set()
        can_replace = []

        for i, (price, category) in enumerate(items):
            if i < k:
                #ensures that only the items with lower price in categories seen before are added to the list of items which can be replaced          
                if category in seen:
                    can_replace.append(price)
                curr_profit += price
            #have taken the first k elements, now looking for distinct categories
            elif category not in seen:
                if not can_replace: break
                # try to replace the new item with distinct category with item with least profit in current can_replaceuence
                curr_profit += price - can_replace.pop()
            
            seen.add(category)
            max_elegance = max(max_elegance, curr_profit + (len(seen) * len(seen)))
        
        return max_elegance

        

        
        return 0
        


