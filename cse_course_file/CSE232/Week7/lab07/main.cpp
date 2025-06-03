#include <exception>
#include <iostream>
#include "Table.hpp"

using namespace std;

int main() {
    cout << std::boolalpha;

    Table my_table(5, 5);
    cout << "Initial Table:\n";
    my_table.PrintTable(cout);
    cout << endl;

    my_table.FillRandom(1, 10);
    cout << "Random Table:\n";
    my_table.PrintTable(cout);
    cout << endl;

    bool result_bool = my_table.SetValue(100, 100, 100);
    cout << "Set illegal value (should return false). Result: " << result_bool << std::endl;
    cout << endl;

    int result_int = my_table.GetValue(3, 2);
    cout << "Value at 3,2: " << result_int << endl;
    try {
        result_int = my_table.GetValue(100, 100);
    } catch (out_of_range& e) {
        cout << "Correct - threw out-of-range exception!" << endl;
    }
    cout << endl;

    for (int i = 0; i < 5; i++) {
        result_bool = my_table.SetValue(i, i + 1, i * i);
        cout << "Set " << i << "," << (i+1) << " to " << (i*i);
        if (!result_bool) cout << " (failed)";
        cout << "\n";
    }

    cout << "\nFinal Table:\n";
    my_table.PrintTable(cout);
    cout << endl;
}
