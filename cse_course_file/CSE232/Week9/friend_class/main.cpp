#include <iostream>
#include <string>

#include "login.h"
#include "secret.h"

int main(){

    Login me("Twilight", "everypony");
    Secret message("I love you all!", me);
    std::cout << message.GetText("everypony") << std::endl;
    std::cout << message.GetText("everybody") << std::endl; 
}