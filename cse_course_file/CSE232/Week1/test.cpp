#include <iostream>
using namespace std;
int main() {
  int x = 10;
  for (int i = 0; i < 10; i++) {
    if (i % 2 == 0) {
      cout << "Even: " << i << endl;
    } else {
      cout << "Odd: " << i << endl;
    }
  }
  return 0;
}
