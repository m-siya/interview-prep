// ### REMOVE DUPLICATES FROM SORTED ARRAY __is_identifier

// Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique 
// element appears at most twice. The relative order of the elements should be kept the same.

// Since it is impossible to change the length of the array in some languages, you must instead have the result be 
// placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates,
//  then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first 
//  k elements.

// Return k after placing the final result in the first k slots of nums.

// Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) 
// extra memory.

// https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int i = 0, j = 0;
        //j keeps track of valid array indices. array valid till index j

        bool seen_twice = false;
        for (int i = 1; i < nums.size(); i++) {
          //  cout << seen_twice << " " << i << " " << j << endl;
            if (!seen_twice && nums[i] == nums[i - 1]) {
                seen_twice = true;
                j++;
                nums[j] = nums[i];
            }

            if (nums[i] != nums[i - 1]) {
                seen_twice = false;
                j++;
                nums[j] = nums[i];
            }
        }

        return j + 1;
        
    }
};