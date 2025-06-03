#include <iostream>
#include <complex> // Add this line to include the <complex> header file
#include <vector> // Add this line to include the <vector> header file


// 1.4 types, variables, and arithmetic
// bool, char, int, double, unsigned

int main(){
    std::cout << sizeof(bool) << std::endl; // 1
    std::cout << sizeof(char) << std::endl; // 1
    std::cout << sizeof(int) << std::endl; // 4
    std::cout << sizeof(double) << std::endl; // 8
    std::cout << sizeof(unsigned) << std::endl; // 4


// arithmetic operators

    int a = 5;
    int b = 2;
    std::cout << a + b << std::endl; // 7
    std::cout << a - b << std::endl; // 3
    std::cout << a * b << std::endl; // 10
    std::cout << a / b << std::endl; // 2
    std::cout << a % b << std::endl; // 1


    int x, y;
    x&y; // bitwise AND
    x|y; // bitwise OR
    x^y; // bitwise XOR
    ~x;// bitwise NOT
    x << 1; // left shift
    x >> 1; // right shift


// initialization

    double d1 = 2.3; // copy initialization, initialize d1 with 2.3
    double d2(2.3); // direct initialization, initialize d2 with 2.3
    double d3{2.3}; // uniform initialization, initialize d3 with 2.3

    std::complex<double> z = 1; // copy initialization, initialize z with 1.0 + 0.0i
    std::complex<double> z2 = {d1, d2}; // copy initialization, initialize z2 with d1 + d2i
    std::complex<double> z3{d1, d2}; // uniform initialization, initialize z3 with d1 + d2i

    // for complex part knolwedge, please refer see the code following
    /*  #include <iostream>
        #include <complex>

        int main() {
            // Define a complex number with real part 3.0 and imaginary part 4.0
            std::complex<double> z(3.0, 4.0);

            std::cout << "Real part: " << z.real() << std::endl; // 3
            std::cout << "Imaginary part: " << z.imag() << std::endl; // 4

            // Perform some arithmetic operations
            std::complex<double> z2(1.0, 2.0);
            std::complex<double> sum = z + z2;
            std::cout << "Sum: " << sum << std::endl; // (4, 6)
            
            return 0;
        }
    */

   auto b = true; // b is a bool
   auto ch = 'x'; // ch is a char
   auto i = 123; // i is an int
   auto z = sqrt(y); // z has the type of whatever sqrt(y) returns

}

// 1.5 Scope and Lifetime

int main(){

    //local scope: variables declared inside a block
    int x = 1;
    {
        int y = 2;
        std::cout << x << std::endl; // 1
        std::cout << y << std::endl; // 2
    }
    std::cout << x << std::endl; // 1

    //global scope: variables declared outside of all blocks
    int z = 3;
    std::cout << z << std::endl; // 3
    
    //class scope: variables declared inside a class
    class A {
        public:
            int a;
            void f() {
                std::cout << a << std::endl;
            }
    };
    // namespace scope: variables declared inside a namespace
    
}


// 1.6 const, constexpr, and symbolic constants

int main(){
    //constexpr: Ensures that variables and functions can be evaluated at compile time when possible, but also allows run-time evaluation if necessary.
    //consteval: Forces the function to be evaluated at compile time, and it cannot be used at run time.
    constexpr double pi = 3.14159; // pi is a compile-time constant
    int var = 17; // var is not a constant
    const double sqv = sqrt(var); // sqv is a named constant, possibly
    double sum(const std::vector<double>&); // sum is a function that takes a reference to a constant vector<double>

}

//1.7 Pointers, Arrays, and References

int main(){

    int* ptr;  // Declares a pointer to an int

    int value = 42;
    int* ptr = &value;  // 'ptr' stores the address of 'value'
    std::cout << *ptr;  // Dereferencing the pointer, it prints 42

    int value = 42;
    int* ptr = &value;  // 'ptr' now stores the address of 'value'

    int* ptr = nullptr;  // Pointer does not point to any valid memory

    int arr[3] = {10, 20, 30};
    int* ptr = arr;  // Points to the first element of the array

    std::cout << *ptr;      // Outputs 10
    ptr++;                  // Moves to the next element in the array
    std::cout << *ptr;      // Outputs 20
    /*
    #include <iostream>

    int main() {
        int number = 100;
        int* ptr = &number;  // Pointer stores the address of 'number'

        std::cout << "Address of number: " << ptr << std::endl;  // Prints memory address of 'number' 0x6d321ffd84
        std::cout << "Value of number: " << *ptr << std::endl;   // Dereferences pointer to get value 100

        // Changing value using pointer
        *ptr = 200;  // Changes 'number' to 200 via pointer
        std::cout << "New value of number: " << number << std::endl; //200

        return 0;
    }

    */
   char x = 'a' + 2;
   std:: cout << x << std::endl; // c
}


// file formatting 
// clang-format -style=google lecture_note.cpp      // to format the code
// clang-format -style=google -i lecture_note.cpp   // -i flag to overwrite the file with the formatted code

// ls          // list all files in the current directory
// pwd         // print the current working directory
// cd ..       // move up one directory
// cd folder_name // move to a specific directory
// mkdir folder_name // create a new directory
// cd ~        // move to the home directory
// cd /        // move to the root directory
// cd -        // move to the previous directory