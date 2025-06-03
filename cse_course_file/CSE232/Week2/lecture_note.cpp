//1.7 pointer, arrays, and references

#include <iostream>


int main(){

    // Pointer: A pointer is a variable that stores the memory address of another variable.

    int a = 5;
    int *p = &a;    // 'p' hold the address of 'a'
    *p =  10;       // Dereferencing 'p' to change the value of 'a' to 10

    std:: cout << a << std:: endl;  // Output: 10
    std:: cout << *p << std:: endl; // Output: 10

    // &(address of): operator gives the memory address of a variable
    // *(dereference): operator gives the value of the variable that the pointer is pointing to

    // Reference: A reference is an alias for a variable. It is another name for the same memory location.

    int b = 20;
    int &r = b;     // 'r' is a reference to 'b'
    r = 30;         // Changing the value of 'r' will change the value of 'b'

    std:: cout << b << std:: endl;  // Output: 30
    std:: cout << r << std:: endl;  // Output: 30


    // difference between pointer and reference
    int a = 10;
    int b = 20;

    // Pointer
    int* p;    // Valid: Pointer declared without initialization
    p = &a;    // Now 'p' points to 'a'
    p = &b;    // Now 'p' points to 'b' (can be re-assigned)

    // Reference
    int& r = a;  // Must be initialized with a reference to 'a'
    r = b;       // Does not re-assign 'r' to 'b'. Instead, changes 'a' to 20
    // r = &b;   // Error: You cannot re-assign a reference to point to 'b'

    int* p = nullptr;  // Pointer can be null (pointing to nothing)                                                     
    // Reference
    // int& r = nullptr;  // Invalid: Reference cannot be null, it must always refer to something



    // Arrays
    // An array is a collection of elements of the same data type stored in contiguous memory locations.

    int arr[5] = {1, 2, 3, 4, 5};  // Declaring an array of size 5
    int arr[] = {1, 2, 3, 4, 5};    // Declaring an array without specifying the size

    // Accessing elements of an array
    std:: cout << arr[0] << std:: endl;  // Output: 1
    std:: cout << arr[1] << std:: endl;  // Output: 2

    // Modifying elements of an array
    arr[0] = 10;
    std:: cout << arr[0] << std:: endl;  // Output: 10

    // Array of pointers
    int x = 10, y = 20, z = 30;
    int* ar[] = {&x, &y, &z};  // Array of pointers to integers

    std:: cout << *ar[0] << std:: endl;  // Output: 10
    std:: cout << *ar[1] << std:: endl;  // Output: 20
    std:: cout << *ar[2] << std:: endl;  // Output: 30

    // Pointer to an array
    int arr[] = {1, 2, 3, 4, 5};
    // array is a pointer to the first element of the array
    int* p = arr;  // Pointer to the first element of the array

    std:: cout << *p << std:: endl;  // Output: 1
    std:: cout << *(p + 1) << std:: endl;  // Output: 2
    std:: cout << *(p + 2) << std:: endl;  // Output: 3

    // Pointer arithmetic
    // Pointers can be incremented and decremented to move to the next or previous memory location.

    int arr[] = {1, 2, 3, 4, 5};
    int* p = arr;  // Pointer to the first element of the array

    std:: cout << *p << std:: endl;  // Output: 1
    p++;  // Move to the next element
    std:: cout << *p << std:: endl;  // Output: 2
    p++;  // Move to the next element
    std:: cout << *p << std:: endl;  // Output: 3



    // C-style strings
    char str[] = "Hello";  // Declaring a C-style string
    char str[] = {'H', 'e', 'l', 'l', 'o', '\0'};  // Equivalent to the above declaration
    char str[3];
    str[0] = 'H';
    str[1] = 'i';
    str[2] = '\0';  // Null character to mark the end of the string

    '\0' == 0; // true




    return 0;
}


// 1.8 tests

int main(){

    // if-else
    int x = 10;
    if (x > 5) {
        std::cout << "x is greater than 5" << std::endl;
    } else {
        std::cout << "x is less than or equal to 5" << std::endl;
    }

    // conditional expression
    int y = (x > 5) ? 100 : 200;
    // if (x) == if (x != 0)
    // if (!x) == if (x == 0)

    
}


#include <iostream>
#include <iomanip>

int main(){
    std::cin >> std::noskipws;

    int char_count{0};
    char c;
    while(std::cin >> c){
        char_count += 1;
    }

    std::cout << char_count << std::endl;

    return 0;
}

int main(){

    int char_count{0};
    int digit_count{0};
    int whitespace_count{0};
    int line_count{0};
    int other_count{0};

    char character;
    while (std::cin >> character) {
    ++char_count;

    switch (character) {
        case '0':
        case '1':
        case '2':
        case '3':
        case '4':
        case '5':
        case '6':
        case '7':
        case '8':
        case '9':
            ++digit_count;
            break;
        case '\n':
            ++line_count;
        case ' ':
        case '\t':
            ++whitespace_count;
            break;
        default:
            ++other_count;
            break;
    }

}