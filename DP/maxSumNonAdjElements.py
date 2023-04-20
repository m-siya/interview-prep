# Given an array of ‘N’  positive integers, we need to return the maximum sum of 
# the subsequence such that no two elements of the subsequence are adjacent elements in the array.

# Note: A subsequence of an array is a list with elements of the array where some elements are 
# deleted ( or not deleted at all) and the elements should be in the same order in the subsequence 
# as in the array.

#https://practice.geeksforgeeks.org/problems/max-sum-without-adjacents2430/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=max-sum-without-adjacents

class Solution:
	
	def findMaxSum(self, arr, n):
		
		dp = [-1] * n
		# dp[i] = the maximum sum at ith index
		#at each index i we can either consider the index or not

		def f(i): #-> max sum at ith index
			if i < 0:
				return 0

			takeElement = arr[i] + f(i - 2)
			leaveElement = f(i - 1)
			return max(takeElement, leaveElement)
		
		return f(n - 1)
