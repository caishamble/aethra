#include "complex.h"
#include <cmath>

using namespace std;

double absolute_value(complex const & c) {
    return sqrt(c.real() * c.real() + c.imag() * c.imag());
}

bool complex::operator<(complex const & b) {
    double abs_a = absolute_value(*this);
    double abs_b = absolute_value(b);
    return abs_a < abs_b;
}