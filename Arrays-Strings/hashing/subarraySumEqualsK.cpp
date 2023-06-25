// ### SUBARRAY SUM EQUALS K

// Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

// A subarray is a contiguous non-empty sequence of elements within an array.

// https://leetcode.com/problems/subarray-sum-equals-k/description/

//method - make a hashmap. iterate through the numbers in nums, in each iteration, 
// add num to sum, thereby storing the cumulative sum in it and find if (sum - k ) exists in map.
// if exists, then increment result. this means we found a subarray su, equal to k. then store the new sum in map

class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        //vector<int> prefix_sums (nums.size() + 1, 0);
        std::unordered_map <int, int> map;

        int sum = 0, result = 0;
        map[sum] = 1;

        for (int num: nums) {
            sum += num;
            result += map[sum - k];
          //  cout << sum << " " << map[sum - k] << endl;
            map[sum] ++;
        }

        


        return result;
    }
};