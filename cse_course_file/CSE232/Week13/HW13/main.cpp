#include <iostream>
#include <iterator>
#include <sstream>
#include <string>
#include <vector>

#include "sort.h"


int main() {
  // read a line from std::cin
  std::string line;
  getline(std::cin, line);

  // get whitespace-separated integers from line into an int vector
  std::istringstream iss(line);
  std::vector<int> values(std::istream_iterator<int>(iss), {});

  std::cout << "Bubble Sort" << std::endl;
  bubble_sort(values);

  std::cout << "Insertion Sort" << std::endl;
  insertion_sort(values);

  std::cout << "Quicksort Sort" << std::endl;
  quicksort_sort(values);

  return 0;
}
