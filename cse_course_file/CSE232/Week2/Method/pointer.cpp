#include <iostream>


// example 1
int main(){

    int a = 5;

    int * p;

    *p = a;

    *p = 10;

    std:: cout << a << std:: endl;  // Output: 10

    return 0;
}

// example 2

int main(){

    int a = 5;

    int *p;

    p = &a;

    std:: cout << *p << std:: endl; // Output: 10
    std:: cout << p << std:: endl;  // Output: Memory address of a
    std:: cout << &a << std:: endl; // Output: Memory address of a


}


// example 3

void swap(int *x, int *y){
    int temp = *x;
    *x = *y;
    *y = temp;
}

int main(){

    int a = 5, b = 10;

    swap(&a, &b);

    std:: cout << a << std:: endl;  // Output: 10
    std:: cout << b << std:: endl;  // Output: 5

    return 0;
}

// example 4

void swap2(int x, int y){
    int temp = x;
    x = y;
    y = temp;
}

int main(){

    int a = 5, b = 10;

    swap2(a, b);

    std:: cout << a << std:: endl;  // Output: 5
    std:: cout << b << std:: endl;  // Output: 10

    return 0;
}