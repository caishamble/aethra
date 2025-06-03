#include "sort.h"
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void bubble_sort(vector<int> vec) {
  size_t n = vec.size();
  for (size_t i = 0; i < n - 1; i++) {
    for (size_t j = 0; j < n - i - 1; j++) {
      if (vec[j] > vec[j + 1]) {
        swap(vec[j], vec[j + 1]);
      }
    }
  }
  for (size_t i = 0; i < n; i++) {
    cout << vec[i] << " ";
  }
  cout << endl;
}

void quicksort_sort(vector<int> vec) {
  sort(vec.begin(), vec.end());
  for (size_t i = 0; i < vec.size(); i++) {
    cout << vec[i] << " ";
  }
  cout << endl;
}

void insertion_sort(vector<int> vec) {
  size_t n = vec.size();
  for (size_t i = 1; i < n; i++) {
    int key = vec[i];
    size_t j = i - 1;
    while (size_t j >= 0 && vec[j] > key) {
      vec[j + 1] = vec[j];
      j = j - 1;
    }
    vec[j + 1] = key;
  }
  for (size_t i = 0; i < n; i++) {
    cout << vec[i] << " ";
  }
  cout << endl;
}

