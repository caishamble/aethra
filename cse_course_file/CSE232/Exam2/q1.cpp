/**
 * Question 1 - Ambiguate
 * 
 * Create a main.cpp, given input text, simply output that same text with all "X" characters with "K" instead, and vice versa.
 * Lowercase instances do not change, and do not modify whitespace and associated punctuation characters.
 * 
 * Input:
 * Xylophone is a musical instrument that starts with the letter X.
 * Y is the 25th letter of the alphabet.
 * X's and K's.
 * these letters inlcluding x and k don't change.
 * 
 * Output:
 * Kylophone is a musical instrument that starts with the letter K.
 * Y is the 25th letter of the alphabet.
 * K's and X's.
 * these letters inlcluding x and k don't change.
 */

#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main(){

    string input;
    while(getline(cin, input)){
            for (size_t i = 0; i < input.size(); ++i){
            if (input[i] == 'X'){
                input[i] = 'K';
            } else if (input[i] == 'K'){
                input[i] = 'X';
            }
        }

        cout << input << endl;
    }



    return 0;
}