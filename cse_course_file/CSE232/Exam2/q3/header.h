#pragma once

#include <iostream>
#include <string>
#include <vector>


using namespace std;

class VoteSystem{
private:
    vector<string> candidates;


public:
    VoteSystem();// we need to create a constructor that initializes the candidates to an empty list
    void add_candidate(string const & candidate);// we need to create a function that adds a candidate to the list of candidates
    string to_string();// we need to create a function that returns a string representation of the candidates -> e.g. "The candidates running are Alice and Bob and Charlie."
    void System(initializer_list<std::string> candidates);// we need to create a function that initializes the candidates to the list of candidates passed in

};