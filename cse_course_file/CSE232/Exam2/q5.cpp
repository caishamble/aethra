/**
 * Question 5 - DayTripper
 * 
 * In DayTripper.cpp, write a function named hide_day_tripper that takes a string (of characters) as a parameter that contains notes
 * for example, "ABCG#"
 * 
 * First, we need to validate that the string contains only real notes, as well as sharps.
 * - We not only need to ensure just note letters and sharps are in the string, but
 * - - we need to ensure there are no unprecedented or double sharps -> "A##" or "#G#"
 * - - if the string is invalid for any of these reasons, throw an invalid_argument exception
 * 
 * Next, we need to hide the day tripper, which is the sequence "EGG#BED" in the string.
 * - If the string contains the sequence anywhere in it, wherever it is, replace it with "*******"
 * - - for example, "ABCG#EGG#BED" should become "ABCG#*******"
 * - - directly modify the string passed in, do not return a new string, instead, return the total number of replacements made
 */

// DayTripper.cpp - TO MODIFY

#include <string>
#include <stdexcept>
#include <iostream>
#include <cassert>

using namespace std;

int hide_day_tripper(string & str){
    int cnt = 0;
    for(size_t i = 0; i < str.size(); ++i){
        if(str[0] == '#'){
            throw std::invalid_argument("It is wrong");
        }
        if(i < str.size() - 1){
            if(str[i] == '#' && str[i + 1] == '#'){
                throw std::invalid_argument("It is wrong");
            }
        }
        
        if(str[i] == 'E' && str.substr(i,7) == "EGG#BED"){
            cnt += 1;
            str.replace(i, 7, "*******");
        }
    }
    return cnt;
}

int main() {
    std::string notes = "ABCG#EGG#BED##";
    assert(hide_day_tripper(notes) == 1);
    assert(notes == "ABCG#*******");
    // cout << hide_day_tripper(notes) << endl;
    // cout << notes << endl;
    return 0;
}
