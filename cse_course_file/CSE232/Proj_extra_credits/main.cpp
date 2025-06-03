#include <iostream>
#include <map>
#include <string>
#include <vector>
#include <sstream>

#include "exchange.hpp"
#include "useraccount.hpp"
#include "utility.hpp"

// we need to write a CHECK function that accepts a boolean value and returns it
int check_number = 1;
bool CHECK(bool condition) {
  if (!condition) {
    std::cout << std::endl << check_number << " CHECK has failed." << std::endl << std::endl;
    check_number++;
    return false;
  }
  std::cout << std::endl << check_number << " CHECK has succeeded." << std::endl << std::endl;
  check_number++;
  return condition;
}

int main(){
  Exchange e;
  std::ostringstream oss;
  e.MakeDeposit("Nahum", "BTC", 10);
  e.MakeDeposit("Dolson", "USD", 5555);
  CHECK(e.AddOrder({"Nahum", "Sell", "BTC", 5, 100}));
  e.PrintUserPortfolios(std::cout);
  oss.str("");
  e.PrintUserPortfolios(oss);
  CHECK(oss.str() == "User Portfolios (in alphabetical order):\nDolson's Portfolio: 5555 USD, \nNahum's Portfolio: 5 BTC, \n");
  e.PrintUsersOrders(std::cout);
  oss.str("");
  e.PrintUsersOrders(oss);
  CHECK(oss.str() == "Users Orders (in alphabetical order):\nDolson's Open Orders (in chronological order):\nDolson's Filled Orders (in chronological order):\nNahum's Open Orders (in chronological order):\nSell 5 BTC at 100 USD by Nahum\nNahum's Filled Orders (in chronological order):\n");
  std::cout << std::endl << std::endl;
  CHECK(e.AddOrder({"Dolson", "Buy", "BTC", 7, 100}));
  e.PrintUserPortfolios(std::cout);
  oss.str("");
  e.PrintUserPortfolios(oss);
  CHECK(oss.str() == "User Portfolios (in alphabetical order):\nDolson's Portfolio: 5 BTC, 4855 USD, \nNahum's Portfolio: 5 BTC, 500 USD, \n");
  e.PrintUsersOrders (std::cout);
  oss.str("");
  e.PrintUsersOrders (oss);
  CHECK(oss.str() == "Users Orders (in alphabetical order):\nDolson's Open Orders (in chronological order):\nBuy 2 BTC at 100 USD by Dolson\nDolson's Filled Orders (in chronological order):\nBuy 5 BTC at 100 USD by Dolson\nNahum's Open Orders (in chronological order):\nNahum's Filled Orders (in chronological order):\nSell 5 BTC at 100 USD by Nahum\n");
  std::cout << std::endl << std::endl;
  CHECK(e.AddOrder({"Nahum", "Sell", "BTC", 3, 100}));
  e.PrintUserPortfolios(std::cout);
  oss.str("");
  e.PrintUserPortfolios(oss);
  CHECK(oss.str() == "User Portfolios (in alphabetical order):\nDolson's Portfolio: 7 BTC, 4855 USD, \nNahum's Portfolio: 2 BTC, 700 USD, \n");
  e.PrintUsersOrders (std::cout);
  oss.str("");
  e.PrintUsersOrders (oss);
  CHECK(oss.str() == "Users Orders (in alphabetical order):\nDolson's Open Orders (in chronological order):\nDolson's Filled Orders (in chronological order):\nBuy 5 BTC at 100 USD by Dolson\nBuy 2 BTC at 100 USD by Dolson\nNahum's Open Orders (in chronological order):\nSell 1 BTC at 100 USD by Nahum\nNahum's Filled Orders (in chronological order):\nSell 5 BTC at 100 USD by Nahum\nSell 2 BTC at 100 USD by Nahum\n");
}