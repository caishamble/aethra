//1.1 Introduction to C++

#include <iostream>

int main(){

    std::cout << "Hello, World!" << std::endl;
    std::cout << "My name is Xiangbo Cai, and I am a student study Computer Engineering at MSU" << std::endl;

    return 0;
}

// 1.2 Comments/ cmd on terminal

// How to run the code in the terminal?
// g++ -std=c++20 -Wall main.cpp   (This is the command to compile the code, the main.cpp is the file name)
// ./a.out   (This is the command to run the code)  
// g++ example.cpp -o example   (This is the command to compile the code and name the output file as example)
// ./example   (This is the command to run the code)
// in the terminal, you can use the up and down arrow to go through the history of the command you have used.
// in the terminal, mv example.cpp example2.cpp   (This is the command to rename the file example.cpp to example2.cpp)
// in the terminal, del example2.cpp OR rm example2.cpp   (These are commands to remove the file example2.cpp)


// 1.3 About C++ and Python


// Script-y kind of langugaes, simple kind of things, ex, Python, Ruby, JavaScript, etc.
// System-y kind of languages, provide efficiency & power to do things,  ex, C, C++, Java, Rust etc.


// C++     complier: code is turn into a seperate executable program, not directly execuate the code;       static typing: every variable has a type, and the type cannot be changed;
// Python  interpreter: code is run line by line by another program, directly execuate the code;            dynamic typing: a variable types can be changed, and implicit stated;


//Print Square Example
#include <iostream> // Using include but not import 

double square(double x){ //Different brace style
    return x * x; // indentation with 4 spaces 
}

void print_square(double x){
    std::cout << 'the square of ' << x << ' is ' 
              << square(x) << '\n';  // Broke the statement into two lines.
}

int main(){
    print_square(1.234);
}


// 1.4 Functions

// C++ Function
// Name the return type and the type of each parameter
int add(int x, int y){
    return x + y;
}


// (a)

// Function Overloading
// Definition: Two functions with the same name but different parameters, are called overloaded functions.
// example:
int add(int x, int y){
    return x + y;
}

double add(double x, double y){
    return x + y;
}




// test function overloading


// void Jump();
// int Jump();
// no, because the return type is different

// void After(double a);
// void After(double);
// no, because the parameter identical are the same


// int Nice(string);
// int Nice(int);
// yes, because the parameter type is different


// string Bark(string);
// string Bark();
// yes, one has the parameter and the other one does not have the parameter



//(b)

// Function Declaration
// Declaration: A function declaration tells the compiler about a function's name, return type, and parameters.
// Example:
int add(int x, int y); // function declaration


// (c)

// Function Definition
// Definition: A function definition provides the actual body of the function.
// Example:
int add(int x, int y){ // function definition
    return x + y;
}

// real example

#include <iostream>

// Function declaration
int add(int a, int b);

int main() {
    int result = add(5, 3);
    std::cout << "The result is: " << result << std::endl;
    return 0;
}

// Function definition
int add(int a, int b) {
    return a + b;
}

// Usually, function declarations are put above the main function, and function definitions are put below the main function.

// When the parameter name is not ignored by the compiler in the function declaration, it means function declaration is also function definition.
#include <iostream>

// Function declaration (parameter names are optional here)
int add(int, int);  // Declaration without parameter names
// int add(int a, int b);  // This is also valid and equivalent

// Function definition (parameter names are required)
int add(int a, int b) {
    return a + b;
}

int main() {
    int x = 5;
    int y = 10;
    int result = add(x, y);  // Function call
    std::cout << "The result is: " << result << std::endl;
    return 0;
}

// How to reduce error? Write more function and shorter function

