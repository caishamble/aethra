#include <bits/stdc++.h>

using namespace std;

int main(){

    map<string, string> name_to_city = {
        {"Josh", "EL"},
        {"Emily", "CL"}
    };

    if (name_to_city["Mal"] == "DC")
        cout << "In DC ";
    cout << name_to_city.size();
    return 0;
}