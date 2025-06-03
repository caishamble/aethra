#include <iostream>
#include <string>

#include "login.h"

int main(){
    Login l1("Calestis", "1234");
    Login l2("Shambles", "5678");
    Login l3("Peter", "1245");
    Login l4("John", "1234");

    std::cout << (l1 == l2) << (l1 == l4) << (l1 == l3) << std::endl;
    return 0;
}