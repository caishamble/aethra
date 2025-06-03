#include <iostream>
#include <string>

int main() {
    std::string str = "Hello, world!";
    
    // Trying to find a substring
    std::size_t found = str.find("world");
    
    if (found != std::string::npos) {
        std::cout << "'world' found at position: " << found << std::endl;
    } else {
        std::cout << "'world' not found" << std::endl;
    }

    // Trying to find a substring that doesn't exist
    found = str.find("planet");
    
    if (found != std::string::npos) {
        std::cout << "'planet' found at position: " << found << std::endl;
    } else {
        std::cout << "'planet' not found" << std::endl;
    }

    return 0;
}
