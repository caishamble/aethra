// create two function

// function one: return_each_digit_add, input 1234, you can return 10
// algorithm: 1234 % 10 = 4, 1234 / 10 = 123, 123 % 10 = 3, 123 / 10 = 12, 12 % 10 = 2, 12 / 10 = 1, 1 % 10 = 1, 1 / 10 = 0, 4 + 3 + 2 + 1 = 10
// write a while loop, each_digit = x % 10, new_value += each_digit, x /= 10, if x < 10, new_value += x, break

// function two: divide_count, input 1234, you can return 2 1
// algorithm: 1234 -> 1 + 2 + 3 + 4 = 10 -> 1 + 0 = 1
// write a while loop, use the first function to returen digit of sum, and if the sum is bigger than 10, you should keep working
// until the sum is smaller than 10, also you have to mark down how many times you have done

// main function
// read a number, and use the second function to get the result, and print out the result
// if the number is 0, you should stop the program
// you can use while loop to keep reading the number until the number is 0

#include <iostream>
#include <vector>

int return_each_digit_add(int x){
  int new_value = 0;
  while(true){
    int each_digit = x % 10;
    new_value += each_digit;
    x /= 10;
    if(x < 10){
      new_value += x;
      break;
    }
  }
  return new_value;
}

void divide_count(int a){
  int cnt = 0;
  int return_a = 0;
  while(true){
    if(a<10){
      return_a = a;
      break;
    }else{
      a = return_each_digit_add(a);
      cnt += 1;
    }
  }
  std::cout << cnt << " " << return_a << std::endl;
}

int main() {
  int a;
  while(std::cin>>a && a > 0){
    divide_count(a);
  }
  return 0;
}


