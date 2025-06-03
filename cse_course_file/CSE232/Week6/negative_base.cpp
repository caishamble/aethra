#include <iostream>
#include <vector>
#include <string>
using namespace std;

// Function to convert a decimal number into a given negative base
string convertToNegativeBase(int n, int base) {
    if (n == 0) {
        return "0";
    }

    vector<int> digits;
    int remainder;
    
    while (n != 0) {
        remainder = n % base;
        n /= base;

        // Adjust remainder and quotient if the remainder is negative
        if (remainder < 0) {
            remainder += (-base);
            n += 1;
        }

        digits.push_back(remainder);
    }

    // Convert the digits into a string
    string result;
    for (int i = digits.size() - 1; i >= 0; i--) {
        if (digits[i] < 10) {
            result += to_string(digits[i]);
        } else {
            result += char('A' + (digits[i] - 10)); // For hexadecimal-like digits
        }
    }

    return result;
}

int main() {
    int n, base;
    
    // Input multiple test cases until the user terminates
    cin >> n >> base;
    string converted = convertToNegativeBase(n, base);
    cout << n << "=" << converted << "(base" << base << ")" << endl;


    return 0;
}
