/**
 * Question 4 - CountWord
 *  -> Write a program, including function CountWord(), that takes, 
 *      from lines of strings, each line and counts the number of times 
 *      the word "word" appears in the line, print this number out 
 *      for each line
 *  -> ex: "hello world word word word
 *          word word word word word" -> "3 
 *                                       5"
 */
#include <bits/stdc++.h>

using namespace std;

vector<string> generateword(string s){
    istringstream iss(s);
    string word;
    vector<string> words;
    while(iss >> word){
        words.push_back(word);
    }
    return words;
}

void CountWord(string s){
    
    vector<string> words = generateword(s);
    int cnt = 0;
    for(size_t i = 0; i <= words.size() - 1; ++i){
        if(words[i] == "word"){
            cnt += 1;
        }
    }
    cout << cnt << endl;
}

int main(){
    string s;
    while(getline(cin, s)){
        CountWord(s);
    }
    return 0;
}