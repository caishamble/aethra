#include "secret.h"

#include <string>

std::string Secret::GetText(std::string const & password){
    if(password == creator.password){
        return text;
    }
    return "Access denied!";
}