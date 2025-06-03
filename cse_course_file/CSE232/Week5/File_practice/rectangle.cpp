#include "rectangle.h"

// Constructor definition
Rectangle::Rectangle(double l, double w) : length(l), width(w) {}

// another way to define constructor
// Rectangle::Rectangle(double l, double w) {
//     length = l;
//     width = w;
// }S

// Getter for length
double Rectangle::getLength() const {
    return length;
}

// Getter for width
double Rectangle::getWidth() const {
    return width;
}

// Setter for length
void Rectangle::setLength(double l) {
    length = l;
}

// Setter for width
void Rectangle::setWidth(double w) {
    width = w;
}

// Function to calculate area
double Rectangle::area() const {
    return length * width;
}

// Function to calculate perimeter
double Rectangle::perimeter() const {
    return 2 * (length + width);
}

// header.hpp
#pragma once
class Rectangle {
private:
    double length;
    double width;

public:
    // Constructor
    Rectangle(double l, double w);

    // Getters
    double getLength() const;
    double getWidth() const;

    // Setters
    void setLength(double l);
    void setWidth(double w);

    // Function to calculate area
    double area() const;

    // Function to calculate perimeter
    double perimeter() const;
};

