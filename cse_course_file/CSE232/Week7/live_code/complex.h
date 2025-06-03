#pragma once
#include <iostream>

class complex{
private:
    double re, im;
public:
    complex(double r, double i) : re{r}, im{i} {}
    complex(double r) : re{r}, im{0} {}
    complex() : re{0}, im{0} {}
    complex(const complex& c) : re{c.re}, im{c.im} {}

    double real() const {
        return re;
    }
    void real(double r) {
        re = r;
    }
    double  imag() const {
        return im;
    }
    void imag(double i) {
        im = i;
    }
    bool operator<(complex const & b);
};

