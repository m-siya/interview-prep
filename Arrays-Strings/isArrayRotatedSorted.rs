// ### CHECK IF ARRAY IS SORTED AND ROTATED

// Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated 
// some number of positions (including zero). Otherwise, return false.

// There may be duplicates in the original array.

// Note: An array A rotated by x positions results in an array B of the same length such that A[i] == B[(i+x) % A.length], 
// where % is the modulo operation.

// https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/description/

impl Solution {
    pub fn check(nums: Vec<i32>) -> bool {
        let mut turning_points = 0;
        for i in 0..nums.len() {
            if nums[i] > nums[(i + 1) % nums.len()] {
                turning_points += 1;
            }
        }
        turning_points <= 1
    }
}