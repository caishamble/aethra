#include <iostream>
#include "temperature.cpp"

using namespace std;

int main() {
    Temperature temp1(32.0, 'F');
    
    // Output the temperature in Fahrenheit
    cout << temp1 << endl; // Output: 32F
    
    // Output the temperature converted to Kelvin
    cout << temp1.AsKelvin() << endl; // Output: 273.15

    return 0;
}
