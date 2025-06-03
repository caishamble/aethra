#include <iostream>

//function declaration
double square(double x);

double square(double x){
    return x * x;
}

int main(){
    std::cout << "The square of 1.234 is " << square(1.234) << '\n';
    return 0;
}