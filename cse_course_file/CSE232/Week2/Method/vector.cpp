#include <iostream>
#include <vector>
#include <algorithm>  // For std::sort

int main() {
    // 1. Declare and initialize a vector
    std::vector<int> vec1;                  // Empty vector of integers
    std::vector<int> vec2(5);               // Vector of 5 integers, initialized to 0
    std::vector<int> vec3(5, 10);           // Vector of 5 integers, initialized to 10
    std::vector<int> vec4 = {1, 2, 3, 4};   // Vector with initializer list

    // 2. Add elements to a vector
    vec1.push_back(1);  // Adds 1 to the end of vec1
    vec1.push_back(2);  // Adds 2 to the end of vec1
    vec1.push_back(3);  // Adds 3 to the end of vec1

    // 3. Accessing elements in a vector
    std::cout << "Element at index 0: " << vec1[0] << std::endl; // Using []
    std::cout << "Element at index 1: " << vec1.at(1) << std::endl; // Using at()

    // 4. Modifying elements in a vector
    vec1[1] = 20; // Modify the element at index 1
    std::cout << "Modified element at index 1: " << vec1[1] << std::endl;

    // 5. Getting the size of the vector
    std::cout << "Size of vec1: " << vec1.size() << std::endl;

    // 6. Iterating through a vector (traditional for loop)
    std::cout << "Iterating through vec1:" << std::endl;
    for (size_t i = 0; i < vec1.size(); ++i) {
        std::cout << vec1[i] << " ";
    }
    std::cout << std::endl;

    // 7. Iterating through a vector (range-based for loop)
    std::cout << "Range-based loop through vec1:" << std::endl;
    for (int val : vec1) {
        std::cout << val << " ";
    }
    std::cout << std::endl;

    // 8. Removing the last element from a vector
    vec1.pop_back(); // Removes the last element
    std::cout << "After pop_back, size of vec1: " << vec1.size() << std::endl;

    // 9. Inserting elements into a vector
    vec1.insert(vec1.begin() + 1, 100);  // Insert 100 at index 1
    std::cout << "After insert, vec1: ";
    for (int val : vec1) {
        std::cout << val << " ";
    }
    std::cout << std::endl;

    // 10. Erasing elements from a vector
    vec1.erase(vec1.begin() + 1);  // Erase the element at index 1
    std::cout << "After erase, vec1: ";
    for (int val : vec1) {
        std::cout << val << " ";
    }
    std::cout << std::endl;

    // 11. Resizing a vector
    vec1.resize(5);  // Resize vec1 to contain 5 elements
    std::cout << "After resize, vec1: ";
    for (int val : vec1) {
        std::cout << val << " ";
    }
    std::cout << std::endl;

    // 12. Clearing all elements from a vector
    vec1.clear();
    std::cout << "After clear, size of vec1: " << vec1.size() << std::endl;

    // 13. Sorting a vector
    std::vector<int> vec5 = {3, 1, 4, 1, 5, 9, 2, 6};
    std::sort(vec5.begin(), vec5.end());
    std::cout << "After sorting, vec5: ";
    for (int val : vec5) {
        std::cout << val << " ";
    }
    std::cout << std::endl;

    return 0;
}
