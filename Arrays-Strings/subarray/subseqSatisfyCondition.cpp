// ### NUMBER OF SUBSEQUENCES THAT SATISFY A GIVEN CONDITION

// You are given an array of integers nums and an integer target.

// Return the number of non-empty subsequences of nums such that the sum of the minimum and 
// maximum element on it is less or equal to target. Since the answer may be too large, return it modulo 109 + 7.

// https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/description/

// we are only interested in the 'count' of subsequences which is the same as the count of subsets

class Solution {
public:
    int numSubseq(vector<int>& nums, int target) {
        int start = 0;
        int end = nums.size() - 1;
        long long subseq_count = 0;
        int mod = 1e9 + 7;

        sort(nums.begin(), nums.end());
        vector<int> pows(end + 1, 1);

        for (int i = 1; i < nums.size(); i++) {
            pows[i] = pows[i - 1] * 2 % mod;
        }

        while (start <= end) {
           // cout << nums[start] << " " << nums[end] << endl;
            if (nums[start] + nums[end] <= target) {
                subseq_count = (subseq_count + pows[end - start]) % mod;
            }
            
            if (nums[start] + nums[end] > target) {
                end--;
            }
            else {
                start++;
            }
        }

        return subseq_count;
    }
    
};