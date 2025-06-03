/**
 * Question 1 - RemoveAllNonalphabeticWords
 *  -> Write a function that removes all non-alphabetic words from an input (string or set of strings)
 *  -> The function should return the input with only alphabetic words, along with the ending character "|"
 *  -> The words are separated by the "|" character
 *  -> ex: "hello|world|123|msu|!|" -> "hello|world|msu|"
 *  -> ex: "hello|928349!|world|123|yes |" -> "hello|world|"
 *  -> assume no upper case letters
 */

// #include <bits/stdc++.h>

// using namespace std;

// vector<string> generate_word(string text){
//     istringstream iss(text);
//     string word;
//     vector<string> words;
//     while(getline(iss, word, '|')){
//         words.push_back(word);
//     }
//     return words;
// }

// bool is_myword(string s){
//     for(char ch : s){
//         if(!isalpha(ch)){
//             return false;
//         }
//     }
//     return true;
// }

// string remove_non(string s){
//     string new_str = "";
//     vector<string> words = generate_word(s);
//     for(size_t i = 0; i < words.size(); ++i){
//         if(is_myword(words[i])){
//             new_str += words[i] + '|';
//         }
//     }
//     return new_str;
// }

// int main(){
//     string text;
//     while(getline(cin, text)){
//         string result = remove_non(text);
//         cout << result << endl;
//     }
//     return 0;
// }


#include <iostream>
#include <string>
#include <sstream>
#include <cctype>

std::string removeAllNonalphabeticWords(const std::string& input) {
  std::stringstream ss;
  bool inWord = false;

  for (char c : input) {
    if (std::isalpha(c)) {
      if (!inWord) {
        ss << c;
        inWord = true;
      } else {
        ss << c;
      }
    } else if (inWord) {
      ss << "|";
      inWord = false;
    }
  }

  if (inWord) {
    ss << "|";
  }

  return ss.str();
}

int main() {
  std::string input1 = "hello|world|123|msu|!|";
  std::string input2 = "hello|928349!|world|123|yes |";

  std::cout << removeAllNonalphabeticWords(input1) << std::endl; // Output: "hello|world|msu|"
  std::cout << removeAllNonalphabeticWords(input2) << std::endl; // Output: "hello|world|"

  return 0;
}