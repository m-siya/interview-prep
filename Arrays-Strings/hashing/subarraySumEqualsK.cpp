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

// ### SUBARRAY SUMS DIVISIBLE BY K
// Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.

// A subarray is a contiguous part of an array.

// https://leetcode.com/problems/subarray-sums-divisible-by-k/description/

class Solution {
public:
    int subarraysDivByK(vector<int>& nums, int k) {
        unordered_map <int, int> map;

        int sum = 0, result = 0;
        map[sum] = 1;

        for (int num: nums) {
            sum = (sum + num % k + k) % k;
            result += map[sum];
            map[sum]++;
        }

        return result;
        
    }
};

// ### CONTINUOUS SUBARRAY SUM

// Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.

// A good subarray is a subarray where:

// its length is at least two, and
// the sum of the elements of the subarray is a multiple of k.
// Note that:

// A subarray is a contiguous part of the array.
// An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.
 
// https://leetcode.com/problems/continuous-subarray-sum/description/

// method -> 
// sum % k = 0
// => (p[j] - p[i]) % k = 0
// => p[j] % k - p[i] % k = 0
// => p[j] % k = p[i] % k,  where j - i >= 1

class Solution {
public:
    bool checkSubarraySum(vector<int>& nums, int k) {
        unordered_map<int, int> map;
        // map = {prefix_sum % k : index of first occurence}

        if (nums.size() < 2) return false;

        int sum = 0;
        map[sum] = -1;
      //  map[sum] = 1;
        

        for (int i = 0; i < nums.size(); i++) {
            sum = (sum + nums[i]) % k;
           // cout << map[sum] << endl;
           if (map.find(sum) != map.end()){
               //sum already exists
               if (i - map[sum] > 1) return true;
           }
           else {
               map[sum] = i;
           }
        }

        // for (auto pair: map) {
        //     cout << pair.first << ": " << pair.second << endl;
        // }

        return false;      
    }
};


