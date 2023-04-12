// String Compression: Implement a method to perform basic string compression using the counts 
// of repeated characters. For example, the string aabcccccaaa would become a2blc5a3, If the 
// "compressed" string would not become smaller than the original string, your method should return 
// the original string. You can assume the string has only uppercase and lowercase letters (a - z). 

#include <iostream>
#include <string>

using namespace std;

string compressString(string org) {
    string compressed = "";

    if (org.length() < 2) {
        return org;
    }

    int count = 1;
    //compressed += str[0];

    for (int i = 1; i < org.length(); i++) {
        if (org[i] == org[i - 1]) {
            count++;
        }
        else {
            compressed += org[i - 1];
            compressed += to_string(count);
            count = 1;
        }
    }

    compressed += org[org.length() - 1];
    compressed += to_string(count);

    if (compressed.length() >= org.length()) {
        return org;
    }

    return compressed;
}

int main() {
	std::string str, out;
	std::cout << "Enter a string:\n";
	std::cin >> str;
	out = compressString(str);
	if (str.compare(out)) {
		std::cout << str << " can be compressed to " << out << std::endl;
	} else {
		std::cout << str << " can not be compressed\n";
	}
	return 0;
}

