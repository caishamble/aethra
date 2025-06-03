#include "login.h"

#include <string>

bool operator==(const Login& l1, const Login& l2){
    return l1.password == l2.password;
}