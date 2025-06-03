#include <iostream>
#include "rectangle.h"

int main() {
    // Create a Rectangle object
    Rectangle rect(10.0, 5.0);

    // Print area and perimeter
    std::cout << "Length: " << rect.getLength() << std::endl;
    std::cout << "Width: " << rect.getWidth() << std::endl;
    std::cout << "Area: " << rect.area() << std::endl;
    std::cout << "Perimeter: " << rect.perimeter() << std::endl;

    return 0;
}
