// Week5 lecture note

#include <bits/stdc++.h>

using namespace std;

int main(){
    // Seperate compilation

    // In C++, the function and class can only has one definition. If you need multiple definition for same function or class, 
    // you need to use seperate compilation and re-direction.

    // method 1: C Macros
    // #define MAX(a, b) ((a) > (b) ? (a) : (b))
    // header.h
    // #ifndef HEADER_H
    // #define HEADER_H
    // file contents
    // #endif

    // method 2: pragma once
    // header.h
    // #pragma once
    // file contents
    return 0;
}