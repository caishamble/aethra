#include <iostream>
#include <algorithm>  // For std::sort, std::reverse

int main() {
    // 1. Declaring and initializing arrays
    int arr1[5];                  // Uninitialized array of 5 integers
    int arr2[5] = {1, 2, 3, 4, 5}; // Array of 5 integers with initial values
    int arr3[] = {10, 20, 30};     // Array with size inferred from the number of elements

    // 2. Accessing and modifying elements in an array
    arr2[1] = 10;  // Modify the second element of arr2
    std::cout << "arr2[1]: " << arr2[1] << std::endl; // Output the modified element

    // 3. Getting the size of an array (using sizeof)
    int arr2_size = sizeof(arr2) / sizeof(arr2[0]);
    std::cout << "Size of arr2: " << arr2_size << std::endl;

    // 4. Iterating through an array (traditional for loop)
    std::cout << "Elements in arr2:" << std::endl;
    for (int i = 0; i < arr2_size; ++i) {
        std::cout << arr2[i] << " ";
    }
    std::cout << std::endl;

    // 5. Range-based for loop (C++11 and later)
    std::cout << "Range-based loop through arr2:" << std::endl;
    for (int val : arr2) {
        std::cout << val << " ";
    }
    std::cout << std::endl;

    // 6. Sorting an array (using std::sort)
    std::sort(arr2, arr2 + arr2_size);  // Sorts arr2 in ascending order
    std::cout << "After sorting arr2: ";
    for (int val : arr2) {
        std::cout << val << " ";
    }
    std::cout << std::endl;

    // 7. Reversing an array (using std::reverse)
    std::reverse(arr2, arr2 + arr2_size);  // Reverses the array
    std::cout << "After reversing arr2: ";
    for (int val : arr2) {
        std::cout << val << " ";
    }
    std::cout << std::endl;

    // 8. Multi-dimensional arrays
    int matrix[2][3] = {{1, 2, 3}, {4, 5, 6}};  // 2x3 matrix (2D array)
    
    // Accessing and modifying elements in a multi-dimensional array
    matrix[1][2] = 10; // Modify the element at row 1, column 2
    std::cout << "Modified matrix[1][2]: " << matrix[1][2] << std::endl;

    // Iterating through a 2D array (traditional for loop)
    std::cout << "Elements in the matrix:" << std::endl;
    for (int i = 0; i < 2; ++i) {
        for (int j = 0; j < 3; ++j) {
            std::cout << matrix[i][j] << " ";
        }
        std::cout << std::endl;
    }

    // 9. Passing arrays to functions (function defined below)
    int arr4[] = {5, 9, 2, 7};
    int arr4_size = sizeof(arr4) / sizeof(arr4[0]);
    std::cout << "Sum of arr4: " << arraySum(arr4, arr4_size) << std::endl;

    return 0;
}

// 10. Function to calculate the sum of an array
int arraySum(int arr[], int size) {
    int sum = 0;
    for (int i = 0; i < size; ++i) {
        sum += arr[i];
    }
    return sum;
}
