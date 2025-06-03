#pragma once
#include <string>

#include "login.h"

class Secret{

private:
    std::string text;
    Login creator;

public:
    Secret(std::string const & text, Login const & creator)
        : text(text), creator(creator) {}
    std::string GetText(std::string const &);
};