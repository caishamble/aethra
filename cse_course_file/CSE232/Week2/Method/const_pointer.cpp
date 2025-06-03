#include <iostream>

int main(){

    int x{23};
    int const y{x};
    
    // int & ref{y}; // Error: Cannot bind a non-const reference to a const variable
    // int & ref; // Error: A reference must be initialized
    int & ref{x};

    std:: cout << ref << std:: endl;  // Output: 23

    ++ref;

    std:: cout << ref << std:: endl;  // Output: 24
    std:: cout << x << std:: endl;    // Output: 24

    ++x;

    // ++y; // Error: Cannot modify a const variable

    //int const & c_ref{y};
    int const & c_ref{x}; // you are allowed to bind a const reference to a non-const variable
    ++x;
    // ++c_ref;           // Error: Cannot modify a const reference

    int * ptr{&x};
    
    std::cout << ptr << std::endl; // Output: Memory address of x,, 0x319ffffc6c
    std::cout << &x << std::endl;  // Output: Memory address of x,, 0x319ffffc6c

    std::cout << *ptr << std::endl; // Output: 25


    int const * ptr2{&x}; // Pointer to a constant integer, not allowed to change the value you are pointing to

    // *ptr2 = 26; // Error: Cannot modify a constant integer
    ptr2 = &y; // Allowed to change the memory address you are pointing to


    int * const ptr3{&x}; // Constant pointer to an integer, not allowed to change the memory address you are pointing to

    // ptr3 = &y; // Error: Cannot reassign a constant pointer
    *ptr3 = 26; // Allowed to change the value you are pointing to 


    int const * const ptr4{&x}; // Constant pointer to a constant integer, not allowed to change the value you are pointing to and the memory address you are pointing to


    return 0;
}