#include <iostream>
#include <vector>
#include <string>
#include "WordList.h"  // Assuming this contains the GetFirstInList and CountInList declarations

using namespace std;

int main() {

    string a, b;
    vector<string> word_lists;
    string word_list;

    // Get user input for the words to search
    getline(cin, a);  // First word to search
    getline(cin, b);  // Second word to search

    // Get multiple word lists
    while (true) {
        getline(cin, word_list);
        if (word_list.empty()) {
            break;  // Stop when the user inputs an empty line
        }
        word_lists.push_back(word_list);  // Add each non-empty word list to the vector
    }

    // Process and print the results for each word list
    for (const auto& list : word_lists) {
        cout << GetFirstInList(list, &a, &b) << " " 
             << CountInList(list, a) << " " 
             << CountInList(list, b) << endl;
    }

    return 0;
}
