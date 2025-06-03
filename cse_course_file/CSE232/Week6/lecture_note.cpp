#include <iostream>
#include <stdexcept> // For standard exception types

int divide(int a, int b) {
    if (b == 0) {
        throw std::runtime_error("Division by zero is not allowed.");
    }
    return a / b;
}

int main() {
    int x = 10;
    int y = 0;

    try {
        int result = divide(x, y);
        std::cout << "Result: " << result << std::endl;
    }
    catch (const std::runtime_error& e) {
        std::cerr << "Caught an exception: " << e.what() << std::endl;
    }

    std::cout << "Program continues after exception handling." << std::endl;

    return 0;
}
