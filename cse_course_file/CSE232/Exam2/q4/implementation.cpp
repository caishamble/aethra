/**
 * Question 4 - Rectangle
 * 
 * Write a class named Rectangle that has the following member functions:
 * - A constructor that takes two integers, height and width, and initializes the height and width of the rectangle.
 * - A member function named can_hold that takes another Rectangle object as a parameter and returns a boolean value.
 * - - This function should return true only if the current rectangle can hold the other rectangle, and false otherwise.
 * - - A rectangle can hold another rectangle if the height and width of the other rectangle are strictly less than the height and width of the current rectangle.
 * - - Additionally, if, when rotated 90 degrees, the other rectangle can fit within the current rectangle, the function should also return true.
 * 
 * Do so by writing both a header file and an implementation file.
 */

// header.h - TO CREATE

// implementation.cpp - TO CREATE

#include "header.h"
#include <iostream>
#include <string>
#include <cmath>
#include <algorithm>

using namespace std;

Rectangle::Rectangle(int height, int width){
    height_ = height;
    width_ = width;
}

int Rectangle::geth() const{
    return height_;
}

int Rectangle::getw() const{
    return width_;
}

bool Rectangle::can_hold(const Rectangle & b)const{
    int h1 = (*this).geth();
    int w1 = (*this).getw();
    int h2 = b.geth();
    int w2 = b.getw();
    int min1 = min(h1, w1);
    int max1 = max(h1, w1);
    int min2 = min(h2, w2);
    int max2 = max(h2, w2);
    if(min1 > min2 && max1 > max2){
        return true;
    }
    return false;
}