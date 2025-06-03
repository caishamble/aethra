/*
q1: dealing with vectors. The code is provided, you need to find 2 errors within the code. Youd are given a vector, and then a fucntion
takes that vector as input, reverses the order, and doubles each value. Then returns that new vector

q2: sum of digits. You have to write a program that takes lines of input with numbers in the string. You need to convert the numbers
from str to int and add them to a sum variable that you output
1
2
3
4

->10

q3: first int of each word. You had to write a program that takes in a line of input, and for each section output the first int.
I believe the output had to be on the same line but seperated.

*/

#include <bits/stdc++.h>

using namespace std;

int main() {
    string input;
    int num;
    int totalSum = 0;
    while(getline(cin, input)){
        totalSum += stoi(input);
    }
    cout << totalSum << endl;

    return 0;
}

