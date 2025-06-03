/**
 * Question 2 - LargestCapital
 *  -> Write the whole program that takes an input set of strings, and, for each line, outputs the largest capital letter
 *  -> ex: "Hello, My Name is Xiangbo." -> "X"
 *  -> if there are no capitals in the string, output an empty string
 */

#include <bits/stdc++.h>

using namespace std;

int main(){
    string s;
    vector<char> store;
    
    while(getline(cin, s)){
        bool string_find = false;
        char ans = 'A';
        for(size_t i = 0; i < s.size(); ++i){
            if((s[i] >= 'A')&&(s[i] <= 'Z')){
                string_find = true;
                store.push_back(s[i]);
            }
        }
        if(string_find){
            for(size_t j = 0; j < store.size(); ++j){
                if(store[j] >= ans){
                    ans = store[j];
                }
            }
            cout << ans << endl;
            store.clear();
        }else{
            cout << "" << endl;
        }
    }
    return 0;
}