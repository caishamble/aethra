#include <iostream>
#include <cmath>

using namespace std;

int factorial(int n){
  int product = 1;
  for (int i = 1; i <= n; ++i){
    product *= i;
  }
  return product;
}

int combination(int n, int k){
  return factorial(n) / (factorial(k) * factorial(n - k));
}

int main(){
  int mark = 0;
  for(int n = 0;; ++n){
    double sum = 0;
    for(int k = 0; k <= 9; ++k){
      sum += combination(n,k) * pow(0.95, k) * pow(0.05, n-k);
    }
    if(sum < 0.05){
      mark = n;
      break;
    }
  }
  cout << mark;
  return 0;
}