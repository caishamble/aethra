#include <iostream>
#include <cctype>   // For character handling functions (toupper, tolower, etc.)
#include <cstring>  // For C-string manipulation functions (strlen, strcpy, etc.)

int main() {
    // 1. Declaring and initializing char variables
    char ch1 = 'A';  // A single character
    char ch2 = 65;   // ASCII value for 'A'
    char ch3 = '\n'; // Special character (newline)

    std::cout << "ch1: " << ch1 << std::endl;
    std::cout << "ch2 (ASCII 65): " << ch2 << std::endl;

    // 2. Declaring and initializing C-style strings (arrays of char)
    char str1[] = "Hello";  // String literal stored as a char array
    char str2[6];           // Array to hold a string (size 6, including null terminator)

    // 3. Copying one C-string to another
    std::strcpy(str2, str1);  // Copy str1 into str2
    std::cout << "Copied string: " << str2 << std::endl;

    // 4. Getting the length of a C-string
    size_t length = std::strlen(str1);
    std::cout << "Length of str1: " << length << std::endl;

    // 5. Concatenating C-strings
    char str3[20] = "Hello";
    std::strcat(str3, " World!");  // Concatenate " World!" to str3
    std::cout << "Concatenated string: " << str3 << std::endl;

    // 6. Comparing C-strings
    if (std::strcmp(str1, str2) == 0) {
        std::cout << "str1 and str2 are equal" << std::endl;
    }

    // 7. Accessing individual characters in a C-string
    std::cout << "First character of str1: " << str1[0] << std::endl;

    // 8. Modifying characters in a C-string
    str1[0] = 'h';  // Changing 'H' to 'h'
    std::cout << "Modified str1: " << str1 << std::endl;

    // 9. Character handling functions from <cctype>
    char ch4 = 'a';
    std::cout << "Uppercase of 'a': " << static_cast<char>(std::toupper(ch4)) << std::endl;
    std::cout << "Lowercase of 'A': " << static_cast<char>(std::tolower(ch1)) << std::endl;

    // 10. Checking if a character is a digit
    char ch5 = '5';
    if (std::isdigit(ch5)) {
        std::cout << ch5 << " is a digit" << std::endl;
    }

    // 11. Checking if a character is a letter
    if (std::isalpha(ch4)) {
        std::cout << ch4 << " is a letter" << std::endl;
    }

    // 12. Checking if a character is alphanumeric
    char ch6 = 'Z';
    if (std::isalnum(ch6)) {
        std::cout << ch6 << " is alphanumeric" << std::endl;
    }

    // 13. Checking if a character is a whitespace character
    char ch7 = ' ';
    if (std::isspace(ch7)) {
        std::cout << "ch7 is a whitespace character" << std::endl;
    }

    // 14. Iterating through a C-string
    std::cout << "Characters in str1: ";
    for (size_t i = 0; i < std::strlen(str1); ++i) {
        std::cout << str1[i] << " ";
    }
    std::cout << std::endl;

    return 0;
}
