#include <iostream>
#include <string>
#include <algorithm> // For std::sort, std::reverse

int main() {
    // 1. Declaring and initializing strings
    std::string str1;                         // Empty string
    std::string str2 = "Hello";               // String with initial value
    std::string str3("World");                // Another way to initialize a string
    std::string str4(5, 'A');                 // String with 5 'A' characters: "AAAAA"
    std::string str5 = str2 + " " + str3;     // Concatenating strings

    // 2. Accessing individual characters in a string
    std::cout << "First character of str2: " << str2[0] << std::endl;
    std::cout << "Last character of str3: " << str3[str3.size() - 1] << std::endl;

    // 3. Modifying individual characters
    str2[0] = 'h'; // Changes 'Hello' to 'hello'
    std::cout << "Modified str2: " << str2 << std::endl;

    // 4. Getting the length of a string
    std::cout << "Length of str5: " << str5.length() << std::endl;

    // 5. Iterating through a string (traditional for loop)
    std::cout << "Characters in str5: ";
    for (size_t i = 0; i < str5.size(); ++i) {
        std::cout << str5[i] << " ";
    }
    std::cout << std::endl;

    // 6. Iterating through a string (range-based for loop)
    std::cout << "Range-based loop through str5: ";
    for (char ch : str5) {
        std::cout << ch << " ";
    }
    std::cout << std::endl;

    // 7. Concatenating strings using '+'
    std::string str6 = str2 + " and " + str3;
    std::cout << "Concatenated string (str2 + str3): " << str6 << std::endl;

    // 8. Finding a substring
    size_t pos = str6.find("World");
    if (pos != std::string::npos) {
        std::cout << "'World' found at position: " << pos << std::endl;
    }

    // 9. Replacing a substring
    str6.replace(0, 5, "HELLO");  // Replace "hello" with "HELLO"
    std::cout << "After replacing, str6: " << str6 << std::endl;

    // 10. Inserting into a string
    str6.insert(5, " beautiful"); // Inserts " beautiful" at position 5
    std::cout << "After insertion, str6: " << str6 << std::endl;

    // 11. Erasing part of a string
    str6.erase(5, 10);  // Erase 10 characters starting from index 5
    std::cout << "After erasing, str6: " << str6 << std::endl;

    // 12. Substring extraction
    std::string sub = str6.substr(0, 5);  // Extracts a substring from index 0, length 5
    std::cout << "Substring of str6: " << sub << std::endl;

    // 13. Comparing strings
    std::string str7 = "apple";
    std::string str8 = "orange";
    if (str7 < str8) {
        std::cout << str7 << " is lexicographically smaller than " << str8 << std::endl;
    }

    // 14. Converting C-style strings to std::string
    const char* c_str = "This is a C-string";
    std::string str9 = std::string(c_str);
    std::cout << "Converted C-string to std::string: " << str9 << std::endl;

    // 15. Converting std::string to C-style string
    const char* c_str2 = str9.c_str();  // Returns a pointer to a C-style string
    std::cout << "Converted std::string to C-string: " << c_str2 << std::endl;

    // 16. Appending to a string
    std::string str10 = "Hello";
    str10.append(" world!");
    std::cout << "After appending, str10: " << str10 << std::endl;

    // 17. Reversing a string (using std::reverse)
    std::reverse(str10.begin(), str10.end());
    std::cout << "Reversed str10: " << str10 << std::endl;

    // 18. convert a int to string
    int num = 12345;
    std::string str_num = std::to_string(num);
    std::cout << "Converted int to string: " << str_num << std::endl;

    // 19. convert a string to int
    std::string str_num2 = "54321";
    int num2 = std::stoi(str_num2);
    std::cout << "Converted string to int: " << num2 << std::endl;
    
    // 20. iss usage
    /*
    #include <iostream>
    #include <sstream>  // Include for std::istringstream
    #include <string>

    int main() {
        // Example string
        std::string input = "42 3.14 Hello";

        // Create an istringstream object
        std::istringstream iss(input);

        int intValue;
        double doubleValue;
        std::string stringValue;

        // Use iss to extract formatted data from the string
        iss >> intValue >> doubleValue >> stringValue;

        // Output the extracted values
        std::cout << "Integer value: " << intValue << std::endl;
        std::cout << "Double value: " << doubleValue << std::endl;
        std::cout << "String value: " << stringValue << std::endl;

        return 0;
    }
    */

    return 0;
}
