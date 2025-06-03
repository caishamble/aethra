#include<bits/stdc++.h>

using namespace std;

// class    

// reference study back up
using std::string;

char & FirstDigit(string &s) {
    for (char & c : s) {
        if (std::isdigit(c)) {
            return c;
        }
    }
    return s.at(0);
}

int main() {
    string text{"My dog is 5 years old"};
    char & digit = FirstDigit(text);
    std::cout << "Digit: " << digit << std::endl;
    std::cout << "Text: " << text << std::endl;
    digit = '1';
    std::cout << "Digit: " << digit << std::endl;
    std::cout << "Text: " << text << std::endl;
}


// constructor
// A constructor is a member function with the same name as class
// constructor never has a return type
// the body of the constructor can to other initialization work(if any)
// member initializer list is used to initialize the member variables of the class

// only class
class MyClass {
public:
    int value;  // Attribute
    void display() {  // Behavior (Method)
        std::cout << value;
    }
};

// constructor inside the class
class MyClass {
public:
    int value;
    MyClass() {  // Constructor
        value = 10;  // Initializing the member variable
    }
};
// class
#include <iostream>
#include <string>

class Car {
public:
    // Public members
    std::string model;
    
    void startEngine() {
        std::cout << "Engine started for " << model << std::endl;
    }

private:
    // Private members
    int year;  // This can only be accessed from inside the class

    void setYear(int y) {
        year = y;  // This function can access the private member year
    }
};

int main() {
    Car myCar;

    // Accessing the public member 'model'
    myCar.model = "Tesla";
    //myCar.startEngine();  // Calling the public method

    // Trying to access the private member 'year'
    // myCar.year = 2021;  // This will give a compile-time error

    return 0;
}

// basic constructor
#include <iostream>
#include <string>

class Car {
public:
    // Public members
    std::string model;
    int year;

    // Constructor
    Car(std::string m, int y) {
        model = m;
        year = y;
        std::cout << "Car constructor called!" << std::endl;
    }

    void displayInfo() {
        std::cout << "Model: " << model << ", Year: " << year << std::endl;
    }
};
int main() {
    Car myCar("Toyota", 2021);  // Constructor is called automatically
    myCar.displayInfo();        // Calling the member function
}

// default constructor
#include <iostream>
#include <string>

class Car {
public:
    std::string model;
    int year;

    // Constructor with parameters
    Car(std::string m, int y) {
        model = m;
        year = y;
    }

    // Default constructor (no parameters)
    Car() {
        model = "Unknown";
        year = 0;
    }

    void displayInfo() {
        std::cout << "Model: " << model << ", Year: " << year << std::endl;
    }
};

int main() {
    Car myCar1("Tesla", 2020);  // Calls constructor with parameters
    Car myCar2;                 // Calls default constructor

    myCar1.displayInfo();       // Output: Model: Tesla, Year: 2020
    myCar2.displayInfo();       // Output: Model: Unknown, Year: 0
}



// sort
sort(a+1,a+n+1,cmp);
// sort the array from a+1 to a+n+1
// cmp is a function that is used to compare the elements of the array