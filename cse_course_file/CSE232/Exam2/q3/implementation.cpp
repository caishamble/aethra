/**
 * Question 3 - VoteSystem
 * 
 * For a defined header.h file below, write an implementation.cpp file that defines the functions as intended from the header.
 * You can use the provided main.cpp file to test your implementation.
 */

#include <iostream>
#include <string>
#include <vector>
#include "header.h"

using namespace std;

VoteSystem::VoteSystem(){
    candidates = {};
}

void VoteSystem::add_candidate(string const & candidate){
    candidates.push_back(candidate);
}

string VoteSystem::to_string(){
    string result = "The candidates running are";
    for(size_t i = 0; i < candidates.size(); i++){
        result += (" "+ candidates[i] + " and");
    }
    return result.substr(0, result.size()-4) + ".";
}

void VoteSystem::System(initializer_list<string> candidates){
    this -> candidates = candidates;
}