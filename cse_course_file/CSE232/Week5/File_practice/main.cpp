#include <iostream>
#include "math_operations.h"

int main() {
    int x = 10;
    int y = 5;

    std::cout << "Addition: " << add(x, y) << std::endl;
    std::cout << "Subtraction: " << subtract(x, y) << std::endl;
    std::cout << "Multiplication: " << multiply(x, y) << std::endl;
    std::cout << "Division: " << divide(x, y) << std::endl;

    return 0;
}
