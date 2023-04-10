// Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you 
// cannot use additional data structures?

#include <string>
#include <vector>
#include <iostream>
#include <bitset>
#include <algorithm>


using namespace std;

bool isUniqueChars(const string &str) {
    if (str.length() > 128) {
        return false;
    }
    vector <bool> char_set(128);
    for (int i = 0; i < str.length(); i++){
        int val = str[i];

        if (char_set[val]) {
            return false;
        }
        char_set[val] = true;
    }

    return true;
}

bool isUniqueChars_bitvector(const string &str) {
    //reduce space by a factor of 8 using bitvector
    //each bool otherwise occupies a size og 8 bits

    bitset<256> bits(0);
    for (int i = 0; i < str.length(); i++) {
        int val = str[i];

        if (bits.test(val) > 0) {
            return false;
        }

        bits.set(val);
    }
    return true;
}

//without using data structures
bool isUniqueChars_noDS(string str) { //cannot pass reference here and make the str const because we are making changes
// to the string
    sort(str.begin(), str.end());

    bool noRepeat = true;

    for (int i = 0; i < str.length() - 1; i++) {
        if (str[i] == str[i + 1]) {
            noRepeat = false;
            break;
        }
    }

    return noRepeat;
}



