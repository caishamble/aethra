#include "WordList.h"
#include <vector>
#include <string>
using namespace std;


vector<string> generate_word(string s) {
    vector<string> word;
    string temp = "";
    for (size_t i = 0; i < s.size(); ++i) {
        if (s[i] == ',') {
            word.push_back(temp); 
            temp = "";  
        } else {
            temp += s[i];  
        }
    }
    word.push_back(temp);  
    return word;
}

bool AtListPosition(const std::string &word_list, const std::string &word, size_t position) {
    vector<string> words = generate_word(word_list); 
    if (position >= word_list.size()) {
        return false;
    }
    size_t current_pos = 0;
    for (const auto& w : words) {
        current_pos = word_list.find(w, current_pos);
        if (w == word && current_pos == position) {
            return true;
        }   
        current_pos += w.length();
    }

    return false;
}


size_t FindInList(const std::string &word_list, const std::string &word, size_t start) {
    vector<string> words = generate_word(word_list); 
    size_t current_pos = 0;  
    for (size_t i = 0; i < words.size(); ++i) {
        current_pos = word_list.find(words[i], current_pos);
        if (current_pos == std::string::npos || current_pos < start) {
            current_pos += words[i].length();  
            continue;
        }
        if (words[i] == word) {
            return current_pos;
        }
        current_pos += words[i].length();
    }
    return std::string::npos; 
}



std::string GetFirstInList(const std::string &word_list, std::string *word1_ptr, std::string *word2_ptr) {
    size_t pos1 = FindInList(word_list, *word1_ptr);
    size_t pos2 = FindInList(word_list, *word2_ptr);

    if (pos1 == string::npos && pos2 == string::npos) {
        return "N/A";  
    } else if (pos1 != string::npos && (pos2 == string::npos || pos1 < pos2)) {
        return *word1_ptr;  
    } else {
        return *word2_ptr;  
    }
}


size_t CountInList(const std::string &word_list, const std::string &word) {
    vector<string> words = generate_word(word_list);  
    return cnt_word(word, words);  
}


int cnt_word(string a, vector<string> word) {  
    int cnt = 0;
    for (const auto &w : word) {
        if (w == a) {
            cnt++;
        }
    }
    return cnt;
}
