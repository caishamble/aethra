#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main(){

    // Introduction to vectors and functions

    // 1. Declaring and initializing vectors
    vector<int> vec1;  // Empty vector of integers
    vector<int> vec2(5);  // Vector of 5 integers with default value (0)
    vector<int> vec3 = {1, 2, 3, 4, 5};  // Vector of integers with initial values

    vector<double> vec4(3, 1.5);  // Vector of 3 doubles with initial value (1.5)
    vector<char> vec5 = {'a', 'b', 'c'};  // Vector of characters with initial values
    vector<string> vec6 = {"Hello", "World"};  // Vector of strings with initial values
    
    // 2. Accessing and modifying elements in a vector
    vec2[1] = 10;  // Modify the second element of vec2
    cout << "vec2[1]: " << vec2[1] << endl;  // Output the modified element

    // 3. Getting the size of a vector
    int vec3_size = vec3.size();
    cout << "Size of vec3: " << vec3_size << endl;

    // 4. Iterating through a vector (range-based for loop)
    cout << "Elements in vec3:" << endl;
    for (int val : vec3) {
        cout << val << " ";
    }
    cout << endl;
    

    // 5. Adding elements to a vector
    vec1.push_back(5);  // Add 5 to the end of vec1
    vec1.push_back(10); // Add 10 to the end of vec1
    cout << "Elements in vec1:" << endl;
    for (int val : vec1) {
        cout << val << " ";
    }
    cout << endl;

    // 6. Removing elements from a vector
    vec3.pop_back();  // Remove the last element from vec3
    cout << "Elements in vec3 after pop_back:" << endl;
    for (int val : vec3) {
        cout << val << " ";
    }

    //7. Position
    vec1.at(0) = 15;
    cout << "Elements in vec1:" << endl;
    vec1[0] = 20;
    cout << "Elements in vec1:" << endl;

    for (int i = 0; i <  static_cast<int>(vec1.size()); i++){
        cout << vec1.at(i) << " ";
    }

    // command
    // rm -r Week3 
    // mv Week3/lecture_note.cpp Week3/lab3.cpp
    // mv -r Week3 Week3/lab3.cpp Week3/test.cpp
    // mv Week3/lecture_note.cpp Week3/test.cpp
    // cp Week3/lab3.cpp Week3/test2.cpp
    // touch Week3/test3.cpp
    // cp -r Week3 Week3/lab3.cpp  
    

    // getline

    string name;
    cout << "Enter your name: ";
    getline(cin, name);
    cout << "Hello, " << name << "!" << endl;

    getline(cin, name, ' ');  // Read until a space character is encountered
    getline(cin, name, '\n');  // Read until a newline character is encountered
    getline(cin, name, '\t');  // Read until a tab character is encountered

    return 0;
}

#include <iostream>
#include <string>
#include <sstream>

int main() {
    std::string line;
    bool firstLine = true;

    // Read input line by line
    while (std::getline(std::cin, line)) {
        std::istringstream iss(line);
        std::string word;
        bool firstWord = true;

        if (!firstLine) {
            std::cout << std::endl; // Print a newline between lines except before the first one
        }

        // Process each word in the line
        while (iss >> word) {
            if (word.length() > 4) {
                if (!firstWord) {
                    std::cout << " "; // Add space before every word after the first
                }
                std::cout << word;
                firstWord = false;
            }
        }

        // Print an additional space at the end of the line if any word was printed
        if (!firstWord) {
            std::cout << " ";
        }

        firstLine = false;
    }

    return 0;
}
