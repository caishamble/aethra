#include <bits/stdc++.h>

using namespace std;

string Two_D_Vector_To_String(vector<vector<char>> vec){
  stringstream os;
  for(int i = 0; i < static_cast<int>(vec.size()); i++){
    for(int j = 0; j < static_cast<int>(vec.at(i).size()); j++){
      os << vec.at(i).at(j) << " ";
    }
    os << "\n";
  }
  return os.str();
}

bool is_prime(int n) {
    if (n < 2) {
        return false;
    }
    for (int i = 2; i <= sqrt(n); ++i) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}

vector<vector<char>> Counting_Spiral(int n) {
    vector<vector<char>> matrix(n, vector<char>(n, '0'));

    // Start from the center
    int x = n / 2;
    int y = n / 2;
    int value = 0;

    matrix[y][x] = '0'; // Set the center value
    value = (value + 1) % 10;

    int steps = 1;

    // Direction vectors: right, up, left, down
    vector<pair<int, int>> directions = {{1, 0}, {0, -1}, {-1, 0}, {0, 1}};
    int directionIndex = 0; // Start by moving right

    while (x != n - 1 || y != n - 1) {
        for (int i = 0; i < 2; ++i) {
            for (int j = 0; j < steps; ++j) {
                x += directions[directionIndex].first;
                y += directions[directionIndex].second;

                // Check if we are within bounds
                if (x >= 0 && x < n && y >= 0 && y < n) {
                    matrix[y][x] = static_cast<char>('0' + value); // Convert to char
                    value = (value + 1) % 10;
                }

                // Stop when reaching the bottom-right corner
                if (x == n - 1 && y == n - 1) {
                    return matrix;
                }
            }
            // Change direction (right -> up -> left -> down)
            directionIndex = (directionIndex + 1) % 4;
        }
        ++steps; // Increase steps after completing a full cycle
    }

    return matrix;
}

vector<vector<char>> Prime_Spiral(vector<vector<char>> vec){
  for(int i = 0; i < static_cast<int>(vec.size()); i++){
    for(int j = 0; j < static_cast<int>(vec.at(i).size()); j++){
      if(is_prime(vec.at(i).at(j) - '0')){
        vec.at(i).at(j) = '0';
      }else{
        vec.at(i).at(j) = ' ';
      }
    }
  }
  return vec;
}

int main() {
    int n = 85; // Example size
    vector<vector<char>> spiral = Counting_Spiral(n);
    vector<vector<char>> primeSpiral = Prime_Spiral(spiral);
    cout << Two_D_Vector_To_String(primeSpiral);

    return 0;
}
