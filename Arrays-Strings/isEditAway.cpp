// One Away: There are three types of edits that can be performed on strings: insert a character, 
// remove a character, or replace a character. Given two strings, write a function to check if they are 
// one edit (or zero edits) away. 
// EXAMPLE 
// pale , pi e - > tru e 
// pales , pal e - > tru e 
// pale , bal e - > tru e 
// pale , bak e - > fals e 

#include <iostream>
#include <string>
#include <vector>

using namespace std;

int getCharNumber(const char c) {
    int a = (int) 'a';
    int z = (int) 'z';
    int A = (int) 'A';
    int Z = (int) 'Z';
    int val = (int) c;

    if (a <= val && val <= z) {
        return val - 'a';
    }
    else if (A <= val && val <= 'Z') {
        return val - 'A';
    }
    return -1;
}

//my sol
//make a count hash table for each string
bool isOneAway(string source, string dest) {
    int source_hash[26] = {0};
    int dest_hash[26] = {0};

    int n1 = source.length();
    int n2 = dest.length();

    if (abs(n2 - n1) > 1){
        return false;
    }

    for (int i = 0; i < source.length(); i++) {
        int val = getCharNumber(source[i]);
        source_hash[val]++;
    }

    for (int i = 0; i < dest.length(); i++) {
        int val = getCharNumber(dest[i]);
        dest_hash[val]++;
    }

    if (abs(n2 - n1) == 1) {    
        //cout << source << " " << dest << " ";
        int edit_count = 0;
        for (int i = 0; i < 26; i++) {
            if (source_hash[i] != dest_hash[i]) {
                edit_count++;
            }
            if (edit_count > 1) 
                return false;
        }
        return true;
    }
    
    else {
        int edit_count = 0;
        for (int i = 0; i < 26; i++) {
            if (source_hash[i] != dest_hash[i]) {
                edit_count++;
            }

            if (edit_count > 2) 
                return false;
        }

        return true;
    }
   
}

void translate( bool result, const std::string str1, const std::string str2 )
{
    if (result == true ) {
        std::cout << str1 << " and " << str2 << " are one edit away\n";
    } else {
        std::cout << str1 << " and " << str2 << " are not one edit away\n";
    }
}


int main()
{
    translate ( isOneAway("pale", "ple"), "pale", "ple" );
    translate ( isOneAway("pales", "pale"), "pales", "pale" );
    translate ( isOneAway("pale", "pales"), "pale", "pales" );
    translate ( isOneAway("pale", "bale"), "pale", "bale" );
    translate ( isOneAway("pale", "bake"), "pale", "bake" );
    return 0;

}
