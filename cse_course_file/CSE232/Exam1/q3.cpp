/**
 * Question 3 - FixTheBug
 *  -> There is a bug in the following code. Find and fix it.
 *  -> The code is supposed to take an input vector of integers and reverse and double.
 *  -> code has compilation and runtime error problems
 *  -> ex: {1, 2, 4, 8, 20, 100} -> "200, 40, 16, 8, 4, 2,"

    for this problem, either try to fix the below, or 
    create the whole code yourself, using a vector returning function 
    that takes in vector and pointer to vector
*/
// #include <iostream>

#include <bits/stdc++.h>

using namespace std;

// vector<int> reverseAndDouble(vector<int> vec){
//     vector<int> result;

//     for (int i = vec.size() - 1; i >= 0; --i){ 
//         result.push_back(vec[i]*2);
//     }
//     return result;
// }

void reverseAndDouble(vector<int> vec){
    vector<int> result;

    for(int i = vec.size() - 1; i >=0; --i){
        cout << vec[i] << " ";
    }
}


int main(){
    vector<int> input = {1, 2, 4, 8, 20, 100};
    reverseAndDouble(input);
    
    // vector<int> output = reverseAndDouble(input);

    // for(size_t i = 0; i <= output.size() - 1; ++i){
    //     cout << output[i] <<',';
    // }
    return 0;
}