#include <iostream>
#include "complex.h"

using namespace std;

int main(){

    complex a = {1, 2};
    complex b = {3, 4};

    cout << (a < b) << endl;

    return 0;
}