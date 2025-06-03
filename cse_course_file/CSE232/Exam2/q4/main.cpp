// main.cpp - for testing
#include "header.h" 
#include <iostream> 

int main() {
    Rectangle const r1(10, 20);
    Rectangle const r2(5, 10);
    Rectangle const r3(20, 10);
    Rectangle const r4(10, 5);
    std::cout << r1.can_hold(r2) << std::endl; // Should return true
    std::cout << r1.can_hold(r3) << std::endl; // Should return false
    std::cout << r1.can_hold(r4) << std::endl; // Should return true
    return 0;
}