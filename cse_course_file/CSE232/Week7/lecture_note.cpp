#include <bits/stdc++.h>

using namespace std;

// Inheritance

// Base class (superclass)
class Animal {
public:
    string name;
    void eat() {
        cout << name << " is eating." << endl;
    }
};

// Derived class (subclass)
class Dog : public Animal {
public:
    void bark() {
        cout << name << " is barking!" << endl;
    }
};

int main() {
    // Create an object of the derived class
    Dog myDog;
    myDog.name = "Buddy";

    // Call the inherited method from the base class
    myDog.eat();

    // Call the method from the derived class
    myDog.bark();

    return 0;
}


// const member function in class

double real() const {
    return re;
}

// note that the function is const, so it cannot change the value of re

// encapsulation

double get_re() const {
    return re;
}   // getter

void set_re(double r) {
    re = r;
}   // setter


// inheritance

class Complex {
    double re, im;
public:
    Complex(double r, double i) : re(r), im(i) {}
    double real() const {
        return re;
    }
    double imag() const {
        return im;
    }
    void real(double r) {
        re = r;
    }
    void imag(double i) {
        im = i;
    }
    Complex& operator+=(Complex z) {
        re += z.re;
        im += z.im;
        return *this;
    }
    Complex& operator-=(Complex z) {
        re -= z.re;
        im -= z.im;
        return *this;
    }
    Complex& operator*=(Complex);
    Complex& operator/=(Complex);
};


// constructor

Complex::Complex(double r, double i) : re{r}, im{i} {}
Complex::Complex(double r) : re(r), im(0) {}
Complex::Complex() : re(0), im(0) {}   // default constructor

// copy constructor

Complex::Complex(const Complex& c) : re(c.re), im(c.im) {}

// operator 

Complex operator+(Complex a, Complex b) {
    return a += b;
}

Complex operator-(Complex a, Complex b) {
    return a -= b;
}

Complex operator*(Complex a, Complex b) {
    return a *= b;
}

Complex operator/(Complex a, Complex b) {
    return a /= b;
}

// friend function

class Complex {
    double re, im;
public:

    friend Complex operator+(Complex a, Complex b);
    friend Complex operator-(Complex a, Complex b);
    friend Complex operator*(Complex a, Complex b);
    friend Complex operator/(Complex a, Complex b);
};

Complex operator+(Complex a, Complex b) {
    return {a.re + b.re, a.im + b.im};
}

Complex operator-(Complex a, Complex b) {
    return {a.re - b.re, a.im - b.im};
}

Complex operator*(Complex a, Complex b) {
    return {a.re * b.re - a.im * b.im, a.re * b.im + a.im * b.re};
}

Complex operator/(Complex a, Complex b) {
    double d = b.re * b.re + b.im * b.im;
    return {(a.re * b.re + a.im * b.im) / d, (a.im * b.re - a.re * b.im) / d};
}


// destructor

class DynamicArray {
private:
    int* data;
    int size;

public:
    // Constructor
    DynamicArray(int s) : size(s) {
        data = new int[size];  // Dynamically allocate memory
        cout << "Array of size " << size << " created." << endl;
    }

    // Destructor
    ~DynamicArray() {
        delete[] data;  // Free dynamically allocated memory
        cout << "Array of size " << size << " destroyed." << endl;
    }

    // Method to set a value
    void setValue(int index, int value) {
        if (index >= 0 && index < size) {
            data[index] = value;
        }
    }

    // Method to get a value
    int getValue(int index) const {
        if (index >= 0 && index < size) {
            return data[index];
        }
        return -1;  // Return -1 for invalid index
    }
};

int main() {
    DynamicArray arr(5);  // Constructor is called

    arr.setValue(0, 10);
    arr.setValue(1, 20);

    cout << "Value at index 0: " << arr.getValue(0) << endl;
    cout << "Value at index 1: " << arr.getValue(1) << endl;

    // Destructor will be called automatically when 'arr' goes out of scope
    return 0;
}

// for more conversation, the linke is below
// https://chatgpt.com/share/6717cdb2-ac7c-800d-b490-7b85e2d8a01f



// Stream I/O


// input function
Vector read(istream& is) {
    Vector v;
    for (double d; is >> d;) {
        v.push_back(d);
    }
    return v;
}

// output function
void write(ostream& os, const Vector& v) {
    for (int i = 0; i != v.size(); ++i) {
        os << v[i] << '\n';
    }
}