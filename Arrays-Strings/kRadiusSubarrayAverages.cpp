// ### K RADIUS SUBARRAY AVERAGES

// You are given a 0-indexed array nums of n integers, and an integer k.

// The k-radius average for a subarray of nums centered at some index i with the radius k is the average of all 
// elements in nums between the indices i - k and i + k (inclusive). If there are less than k elements before or 
// after the index i, then the k-radius average is -1.

// Build and return an array avgs of length n where avgs[i] is the k-radius average for the subarray centered at index i.

// The average of x elements is the sum of the x elements divided by x, using integer division. The integer division 
// truncates toward zero, which means losing its fractional part.

// For example, the average of four elements 2, 3, 1, and 5 is (2 + 3 + 1 + 5) / 4 = 11 / 4 = 2.75, which truncates to 2.

// https://leetcode.com/problems/k-radius-subarray-averages/description/

//method -> generate a prefix sums array to quickly calculate sums of sub arrays

// time complexity - O(2 * N), space complexity - O(2 * N)

class Solution {
public:
    vector<int> getAverages(vector<int>& nums, int k) {
        int SIZE = nums.size();
        vector<long int> prefix_sums (SIZE + 1, 0);
        //int total_sum = 0;

        for (int i = 0; i < SIZE; i++) {
            prefix_sums[i + 1] = prefix_sums[i] + nums[i];
            //cout << prefix_sums[i] << endl;
        }

        vector<int> averages (SIZE, -1);

        for (int i = 0; i < SIZE; i++) {
            if (i - k < 0 || i + k >= SIZE) continue;

            //cout << prefix_sums[i + k] - prefix_sums[i - k] << endl;

            averages[i] = (prefix_sums[i + k + 1] - prefix_sums[i - k]) / (2 * k + 1);
        }

        return averages;     
    }

    
};
 
