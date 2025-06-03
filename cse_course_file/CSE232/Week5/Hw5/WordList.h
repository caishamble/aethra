#ifndef WORDLIST_H
#define WORDLIST_H

#include <string>
#include <vector>  // Include the vector header

using namespace std;

vector<string> generate_word(string s);
bool AtListPosition(const std::string &word_list, const std::string &word, size_t pos);
size_t FindInList(const std::string &word_list, const std::string &word, size_t pos = 0);
std::string GetFirstInList(const std::string &word_list, std::string *word1_ptr, std::string *word2_ptr);
size_t CountInList(const std::string &word_list, const std::string &word);
int cnt_word(string a, vector<string> word);  // Helper function

#endif
