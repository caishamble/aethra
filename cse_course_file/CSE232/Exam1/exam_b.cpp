// Exam 1 - Pool B Questions

/**
 * Question 1 - RemoveAllNonalphabeticWords
 *  -> Write a function that removes all non-alphabetic words from an input (string or set of strings)
 *  -> The function should return the input with only alphabetic words, along with the ending character "|"
 *  -> The words are separated by the "|" character
 *  -> ex: "hello|world|123|msu|!" -> "hello|world|msu|"
 *  -> assume no upper case letters
 */

/**
 * Question 2 - LargestCapital
 *  -> Write the whole program that takes an input set of strings, and, for each line, outputs the largest capital letter
 *  -> ex: "Hello, My Name is Xiangbo." -> "X"
 *  -> if there are no capitals in the string, output an empty string
 */

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
#include <iostream>
#include <vector>
#include <algorithm>

std::vector<int> reverseAndDouble(std::vector<int> vec {
    std::vector<int> result;

    for (i = vec.size(); i <= 0; i--) 
        result.push_back(vec[i] * 2)

    return reslt;
}

int main() {
    std::vector<int input = {1, 2, 4, 8, 20, 100;
    
    std::vector<int> output = reverseAndDouble(input;

    for j < output.size {
        std::cout << output[i] << , ;
    }

}


/**
 * Question 4 - CountWord
 *  -> Write a program, including function CountWord(), that takes, 
 *      from lines of strings, each line and counts the number of times 
 *      the word "word" appears in the line, print this number out 
 *      for each line
 *  -> ex: "hello world word word word
 *          word word word word word" -> "1 
 *                                       5"
 */

/**
 * Question 5 - LastDigit
 *  -> Write a program that takes a lines of integers, sometimes 
 *      spaced by whitespace, and outputs the last digit of each
 *  -> ex: "123 456
 *          789 1000" -> "3
 *                        6 
 *                        9 
 *                        0"
 */