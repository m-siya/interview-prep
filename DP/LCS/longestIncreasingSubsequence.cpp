// ### LONGEST INCREASING SUBSEQUENCE

// Given an integer array nums, return the length of the longest strictly increasing 
// subsequence

// https://leetcode.com/problems/longest-increasing-subsequence/description/

class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        int length = nums.size();
        int curr_num_index = length;

        vector<vector<int>> dp (length, vector<int> (length + 1, -1));

        function <int(int, int)> f = [&] (int i, int curr_num_index) -> int {
            // f(i) -> length of lis at index i 
            if (i < 0)
                return 0;

            if (dp[i][curr_num_index] != -1)
                return dp[i][curr_num_index];
            
            int leave = f(i - 1, curr_num_index);
            int take = 0;
            if (curr_num_index == length || nums[i] < nums[curr_num_index]) 
                take = 1 + f(i - 1, i);

            return dp[i][curr_num_index] = max(leave, take);
        };

        return f(length - 1, curr_num_index);
        
    }
};