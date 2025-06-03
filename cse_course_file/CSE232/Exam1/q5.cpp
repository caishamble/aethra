/**
 * Question 5 - LastDigit
 *  -> Write a program that takes a lines of integers, sometimes 
 *      spaced by whitespace, and outputs the last digit of each
 *  -> ex: "123 456
 *          789 1000" -> "3
 *                        6 
 *                        9 
 *                        0"
 */

#include <bits/stdc++.h>

using namespace std;

vector<string> generateword(string s){
    istringstream iss(s);
    string word;
    vector<string> words;
    while(iss>>word){
        words.push_back(word);
    }
    return words;
}

int main(){
    string s;
    while(getline(cin, s, '!')){
        vector<string> words = generateword(s);
        for(size_t i = 0; i <= words[i].size() - 1; ++i){
            cout << words[i].substr(words[i].size() - 1) << endl;
        }
    }
    return 0;
}