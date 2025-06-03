#pragma once

#include <iostream>

class Rectangle {
private:
    int height_;
    int width_;

public:
    Rectangle(int height, int width);
    int get_height() const;
    int get_width() const;
    bool can_hold(const Rectangle& other) const;
};
