# ### SUBSTRING WITH CONCATENATION OF ALL WORDS

# You are given a string s and an array of strings words. All the strings of words are 
# of the same length.

# A concatenated substring in s is a substring that contains all the strings of any
# permutation of words concatenated.

# For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab",
#  "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated 
#  substring because it is not the concatenation of any permutation of words.
# Return the starting indices of all the concatenated substrings in s. You can return 
# the answer in any order.

# https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/

# method - make a hashmap of words and their counts
# use sliding window to iterate through string s in window of length of the concatenated
# string. initialize a seen hashmap for all windows
# then iterate through all the words in the current sliding window and each time one in 
# words is found, increase count in the seen hashmap.
# at the end check if the original hashmap and seen are equivalent. if so then this is 
# a valid concatenated string

# n = len(s), k = len(words), m = len(words[0])
# tc - O((n - k) * k * m)
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        num_words = len(words)
        len_word = len(words[0])
        concat_str_len = num_words * len_word

        answer = []
        wordBag = Counter(words)

        for i in range(0, len(s) - concat_str_len + 1):
            #checkif s[i: i + concat_str_len] is a permutation of words
            seen = defaultdict(int)
            for j in range(i, i + concat_str_len, len_word):
                curr_word = s[j : j + len_word]
                if curr_word in wordBag:
                    seen[curr_word] += 1
                    if seen[curr_word] > wordBag[curr_word]:
                        break
                else:
                    break
            
            if seen == wordBag:
                answer.append(i)
        return answer



            


                    
                





