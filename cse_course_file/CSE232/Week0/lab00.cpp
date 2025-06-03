#include <iostream>
#include <vector>
#include <string>

using namespace std;



int main() {
    vector<string> names;
    string name;
    cout << "Enter names: ";
    while (cin >> name) {
        names.push_back(name);
    }
    cout << "Names: ";
    for (int i = 0; i < names.size(); i++) {
        cout << names[i] << " ";
    }
    cout << endl;
    return 0;
}