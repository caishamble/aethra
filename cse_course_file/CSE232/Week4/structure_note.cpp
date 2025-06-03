#include <bits/stdc++.h>

using namespace std;

// structure

// pass by value
//int Count (string s);
// the argument is copied, and thus no changes to it affect to original variable

// pass by reference
//int Count (string &s);
// the parameter is a reference to the original variable, so changes to it affect the original variable


// access operator

int main(){

    string s{"CSE232"};
    cout << s.size() << endl; // 6
    // dot operator allows to access to the members of the string

    string *s_str = &s;
    cout << s_str->size() << endl; // 6
    // arrow operator does the same thing, but dereferences the pointer first

    cout << (*s_str).size() << endl; // 6
    //cout << *s_str.size() << endl; // compiler time error, dot operator has higher precedence than dereference operator
    //cout << *(s_str.size()) << endl; // same as above, still compiler time error, because pointers don't have member 

    //In C++, the term member refers to the components or elements inside a class or structure. 
    //These members can either be data members (variables) or member functions
    // (methods or functions defined inside the class or structure).

    // Dynamic memory 
    // Dynamic memory refers to memory that is allocated during a program's execution (runtime)

    // new operator
    // new operator is used to allocate memory at runtime.
    // new operator returns the address of the space allocated.
    // new operator is used to allocate memory for a single variable of a given type.
    // new operator is used to allocate memory for an array of variables of a given type.

    //dynamic memory allocation will automically be deallocated when it falls out of scope

    int *x = new int{0};
    // new returns to a pointer dynamically allocated memory
    // this object's live until the program ends or until it is deleted

    delete x;



    string * word = new string[40]{"CSE232", "232"};
    // new can also be used to allocate memory for an array of variables
    // the initialization is optional
    delete [] word;
    // Note [] is required to delete an array of dynamically allocated memory

    // Benefits of dynamic memory allocation
    // 1. The size of the array can be determined at runtime.   
    // 2. Scope of the array can be controlled by the programmer.
    // 3. Heap memory is not limited to the size of the stack. //The heap is a region of a computer's memory used for dynamic memory allocation.
    // 4. Control over the memory allocation and deallocation.

    cout << "2" << '32';
    


    return 0;
}

// struct
#include <iostream>
#include <string>

// Define a struct to hold data
struct Person {
    std::string name;
    int age;
};

int main() {
    // Create an instance (object) of the struct
    Person person1;

    // Access and assign values to the members of the struct
    person1.name = "Alice";
    person1.age = 25;

    // Print out the values
    std::cout << "Name: " << person1.name << std::endl;
    std::cout << "Age: " << person1.age << std::endl;

    return 0;
}
