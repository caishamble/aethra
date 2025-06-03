#pragma once
#include <iostream>
#include <string>
#include <map>
#include <vector>
#include "useraccount.hpp"
#include "utility.hpp"

class Exchange {
 public:
  // Public member functions
  void MakeDeposit(const std::string &username, const std::string &asset, int amount);
  bool MakeWithdrawal(const std::string &username, const std::string &asset, int amount);
  bool AddOrder(const Order &order);
  
  // Output functions
  std::ostream &PrintUserPortfolios(std::ostream &os) const;
  std::ostream &PrintUsersOrders(std::ostream &os) const;
  std::ostream &PrintOpenOrders(std::ostream &os) const;
  std::ostream &PrintFilledOrders(std::ostream &os) const;
  std::ostream &PrintTradeHistory(std::ostream &os) const;
  std::ostream &PrintBidAskSpread(std::ostream &os) const;

 private:
  // Private member variables
  std::map<std::string, UserAccount> user_accounts_; // Holds user account information
  std::vector<Order> trade_history_; // Tracks the history of executed trades

  // Private helper functions
  bool ValidateOrder(const Order &order, const UserAccount &account) const; // Validates if the order can be placed
  bool ReserveFundsForOrder(const Order &order, UserAccount &account);      // Reserves funds or assets for the order
  void AddOrderToAccount(const Order &order, UserAccount &account);         // Adds an order to the user's open orders
  bool MatchOrder(const Order &new_order);                                  // Attempts to match a new order with existing open orders
  void ExecuteTrade(const Order &buy_order, const Order &sell_order);       // Executes a trade and updates portfolios
};
