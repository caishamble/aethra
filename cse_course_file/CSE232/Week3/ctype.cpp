#include <iostream>
#include <cctype>  // For character handling functions
#include <string>

int main() {
    std::string testStr = "Hello, World! 123 \t\n";

    std::cout << "Testing string: \"" << testStr << "\"\n\n";

    // Loop through each character in the string and check various properties
    for (char ch : testStr) {
        std::cout << "Character: '" << ch << "'\n";

        // Check if alphabetic
        if (isalpha(ch)) {
            std::cout << "  isalpha: true (Alphabetic character)\n";
        }

        // Check if digit
        if (isdigit(ch)) {
            std::cout << "  isdigit: true (Digit)\n";
        }

        // Check if alphanumeric
        if (isalnum(ch)) {
            std::cout << "  isalnum: true (Alphanumeric character)\n";
        }

        // Check if space or other whitespace character
        if (isspace(ch)) {
            std::cout << "  isspace: true (Whitespace character)\n";
        }

        // Check if lowercase
        if (islower(ch)) {
            std::cout << "  islower: true (Lowercase letter)\n";
        }

        // Check if uppercase
        if (isupper(ch)) {
            std::cout << "  isupper: true (Uppercase letter)\n";
        }

        // Check if punctuation
        if (ispunct(ch)) {
            std::cout << "  ispunct: true (Punctuation mark)\n";
        }

        // Check if hexadecimal digit
        if (isxdigit(ch)) {
            std::cout << "  isxdigit: true (Hexadecimal digit)\n";
        }

        // Check if control character
        if (iscntrl(ch)) {
            std::cout << "  iscntrl: true (Control character)\n";
        }

        // Check if printable character
        if (isprint(ch)) {
            std::cout << "  isprint: true (Printable character)\n";
        }

        // Check if graphic character (printable but not space)
        if (isgraph(ch)) {
            std::cout << "  isgraph: true (Graphic character)\n";
        }

        // Convert to lowercase
        if (isupper(ch)) {
            std::cout << "  tolower: '" << static_cast<char>(tolower(ch)) << "' (Lowercase conversion)\n";
        }

        // Convert to uppercase
        if (islower(ch)) {
            std::cout << "  toupper: '" << static_cast<char>(toupper(ch)) << "' (Uppercase conversion)\n";
        }

        std::cout << "\n";
    }

    return 0;
}
