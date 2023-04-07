// Check Permutation: Given two strings, write a method to decide if one is a permutation of the 
// other
#include <string>
#include <vector>
#include <iostream>
#include <bitset>
#include <algorithm>

using namespace std;


// uses sort (O(nlogn)) with no extra space
bool checkPermutation(string s1, string s2) {
    int n1 = s1.length();
    int n2 = s2.length();

    if (n1 != n2)
        return false;

    sort(s1.begin(), s1.end());
    sort(s2.begin(), s2.end());

    for (int i = 0; i < n1; i++) {
        if (s1[i] != s2[i]) {
            return false;
        }
    }

    return true;
}

//use concept of array as a hash map
//useful when fixed length of character set
// O(2N) => O(N) with O(N) space
bool checkPermutations_hash(string s1, string s2) {
    if (s1.length() != s2.length()) {
        return false;
    }

    int count[256] = {0};

    for (int i = 0; i < s1.length(); i++) {
        count[s1[i]]++;
    }

    for (int i = 0; i < s2.length(); i++) {
        count[s2[i]]--;

        if (count[s2[i]] < 0) {
            return false;
        }
    }

    return true;
}