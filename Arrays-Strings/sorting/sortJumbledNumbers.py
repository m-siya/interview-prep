# ### SORT THE JUMBLED NUMBERS

# You are given a 0-indexed integer array mapping which represents the mapping rule of a shuffled decimal system. mapping[i] = j means digit i should be mapped to digit j in this system.

# The mapped value of an integer is the new integer obtained by replacing each occurrence of digit i in the integer with mapping[i] for all 0 <= i <= 9.

# You are also given another integer array nums. Return the array nums sorted in non-decreasing order based on the mapped values of its elements.

# Notes:

# Elements with the same mapped values should appear in the same relative order as in the input.
# The elements of nums should only be sorted based on their mapped values and not be replaced by them.

# https://leetcode.com/problems/sort-the-jumbled-numbers/description/?envType=daily-question&envId=2024-07-24

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        mp = {i: mapping[i] for i in range(len(mapping))}

        maps = []

        for num in nums:
            str_num = str(num)
            mapped_str_num = ''.join((str(mp[int(n)]) for n in str_num))
            maps.append(mapped_str_num)

       # print(maps)

        return [n for n, m in sorted(zip(nums, maps), key= lambda x: int(x[1]))]

        #return nums

# same solution but using the library

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        maps = str.maketrans({str(i): str(num) for i, num in enumerate(mapping)})

        return sorted(nums, key=lambda x: int(str(x).translate(maps)))
        