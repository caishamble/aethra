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

