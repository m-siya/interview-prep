// URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string 
// has sufficient space at the end to hold the additional characters, and that you are given the "true" 
// length of the string.

#include <iostream>
#include <string>

using namespace std;

string URLify(string str, int trueLength) {
    int spaceCount = 0, newLength = 0;

    for (int i = 0; i < trueLength; i++){
        if (str[i] == ' ')
            spaceCount++;
    }

    newLength = trueLength + (spaceCount * 2);
    for(int i = trueLength - 1; i >= 0; i--) {
        if (str[i] == ' ') {
            str[newLength - 1] = '0';
            str[newLength - 2] = '2';
            str[newLength - 3] = '%';
            newLength = newLength - 3;
        }
        else {
            str[newLength - 1] = str[i];
            newLength = newLength - 1;
        }
    }
}