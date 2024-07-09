# ### MAXIMIZE CONFUSION OF AN EXAM

# A teacher is writing a test with n true/false questions, with 'T' denoting true and 'F' denoting false. He wants to confuse the students by maximizing the number of consecutive questions with the same answer (multiple trues or multiple falses in a row).

# You are given a string answerKey, where answerKey[i] is the original answer to the ith question. In addition, you are given an integer k, the maximum number of times you may perform the following operation:

# Change the answer key for any question to 'T' or 'F' (i.e., set answerKey[i] to 'T' or 'F').
# Return the maximum number of consecutive 'T's or 'F's in the answer key after performing the operation at most k times.

# https://leetcode.com/problems/maximize-the-confusion-of-an-exam/description/

class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        max_cons = 0
        for ans in ["T", "F"]:
            j = 0
            count = 0

            for i in range(len(answerKey)):

                if answerKey[i] != ans:
                    count += 1
                
                while count > k:
                    if answerKey[j] != ans:
                        count -= 1
                    j += 1

                max_cons = max(max_cons, i - j + 1)
        

        return max_cons
                


        