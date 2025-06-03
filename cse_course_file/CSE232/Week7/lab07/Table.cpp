#include "Table.hpp"
#include <random>
#include <vector>
#include <string>
#include <iostream>

using namespace std;

Table::Table(size_t width, size_t height, int val)
// PLACE A ':' HERE FOLLOWED BY ANY MEMBER VARIABLE INITIALIZIONS
{
  width_ = width;
  height_ = height;
  row_t row_vec (width_ , val);
  vector<row_t> two_d_vec (height_, row_vec);
  table_ = two_d_vec;
}

// WRITE THE DEFINITION FOR Table::PrintTable
void Table::PrintTable(std::ostream & out) const{
  // vector<vector<int>> two_d_vec;
  // two_d_vec = Table(width_, height_, val);
  for(size_t i = 0; i < table_.size(); ++i){
    for(size_t j = 0; j < table_.at(i).size(); ++j){
      out << table_.at(i).at(j) << ", ";
    }
    out << endl;
  }
}

// // WRITE THE DEFINITION FOR Table::FillRandom
void Table::FillRandom(int low, int high, int seed){
  // std::random_device device;
  std::mt19937 generator(seed);
  std::uniform_int_distribution<int> distribution(low, high);

  // when we need the random value, we use distribution(generator)
  for(size_t i = 0; i < table_.size(); ++i){
    for(size_t j = 0; j < table_.at(i).size(); ++j){
      table_.at(i).at(j) = distribution(generator);
    }
  }
}


// // WRITE THE DEFINITION FOR Table::SetValue
bool Table::SetValue(size_t col, size_t row, int val){
  if(((col) < width_  && static_cast<int>(col) >= 0) && ((row) < height_ && static_cast<int>(row) >= 0 )){
    table_.at(row).at(col) = val;
    return true;
  }else{
    //throw std::out_of_range("Gone bro");
    return false;
  }
}


// // WRITE THE DEFINITION FOR Table::GetValue
int Table::GetValue(size_t col, size_t row) const{
  if(((col) < width_  && static_cast<int>(col) >= 0) && ((row) < height_ && static_cast<int>(row) >= 0 )){
    return table_.at(row).at(col);
  }else{
    throw std::out_of_range("This is not in my table!");
  }
}