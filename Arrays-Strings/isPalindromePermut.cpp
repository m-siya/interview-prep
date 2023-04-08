// Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome. 
// A palindrome is a word or phrase that is the same forwards and backwards. A permutation 
// is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words. 

//Do not generate all permutations - would be very inefficient
//Try hash table
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <bitset>

using namespace std;

//my sol
//to be a palindrome, a all letters (except at most one) should have frequencies divisible by 2
//create a vector to store all frequencies
bool isPalindromePermutation(string str) {
    vector <int> char_frequencies(256);

    transform(str.begin(), str.end(), str.begin(), ::tolower);

    for (int i = 0; i < str.length(); i++) {
        if (str[i] != ' ') {
            int letter = str[i];
            char_frequencies[letter]++;
        }
    }
 
    bool middle_letter_found = false;
    for (int i = 0; i < char_frequencies.size(); i++) {

        if (middle_letter_found && char_frequencies[i] % 2 != 0) 
            return false;
        
        if (char_frequencies[i] % 2 != 0)
            middle_letter_found = true;
        
    }
    return true;
}

int getCharNumber(const char & c){
    int a = (int) 'a';
    int z = (int) 'z';
    int A = (int) 'A';
    int Z = (int) 'Z';
    int val = (int) c;
    if(a <= val && val <= z){
        return val - 'a';
    }
    else if(A <= val && val <= Z){
        return val - 'A';
    }
    return -1;
}


//using bitvector
bool isPalindromePermutation_bitwise(string str) {
    const int num_char = 26;
    bitset <num_char> table(0);

    for (const char& c: str) {
        const int hash = getCharNumber(c);
        if (hash == -1) {
            continue;
        }
        table.flip(hash);
    }

    const int summary = table.to_ullong();
    cout << summary << endl;
    //dont understand why we are doing summary & summary - 1
    const bool isPowerOf2 = ((summary) & (summary - 1)) == 0;
    return isPowerOf2;
}


#define TEST(pFunc, pattern)                                \
    do {                                                    \
        cout << "[" #pFunc "]" << endl;                     \
        cout << "- Pattern: " << pattern << endl;           \
        cout << "- Result : " << pFunc(pattern) << endl;    \
    } while (0)


int main(int argc, const char *argv[])
{
    vector<string> patterns{
        "",
        "a",
        "ab",
        "Tact Coa",
        "Rats live on no evil st",
        "Rats live on no evil star"
        };
    for (auto& pattern: patterns)
    {
        TEST(isPalindromePermutation, pattern);
    }
    for (auto& pattern: patterns)
    {
        TEST(isPalindromePermutation_bitwise, pattern);
    }
    return 0;
}