#pragma once
#include "utility.hpp"
#include <map>
#include <string>
#include <vector>
#include <ostream>

class UserAccount {
 public:
  UserAccount() : username_("") {};
  UserAccount(const std::string &username);
  
  // Deposits the specified amount of the given asset into the portfolio.
  void Deposit(const std::string &asset, int amount);
  
  // Withdraws the specified amount of the given asset if available.
  bool Withdraw(const std::string &asset, int amount);
  
  // Adds an order to the open orders list.
  void AddOrder(const Order &order);
  
  // Prints the user's portfolio in alphabetical order of assets.
  void PrintPortfolio(std::ostream &os) const;
  
  // Prints the user's open and filled orders in chronological order.
  void PrintOrders(std::ostream &os) const;
  
  // Provides read-only access to the user's portfolio.
  const std::map<std::string, int> &GetPortfolio() const { return portfolio_; }

  // Provides read-only access to the user's open orders.
  const std::vector<Order> &GetOpenOrders() const { return open_orders_; }

  // Provides writable access to the user's open orders.
  std::vector<Order> &GetOpenOrders() { return open_orders_; }

  // Provides read-only access to the user's filled orders.
  const std::vector<Order> &GetFilledOrders() const { return filled_orders_; }

  // Provides writable access to the user's filled orders.
  std::vector<Order> &GetFilledOrders() { return filled_orders_; }

 private:
  std::string username_; // The username of the account holder.
  std::map<std::string, int> portfolio_; // Asset to amount mapping.
  std::vector<Order> open_orders_; // List of open orders.
  std::vector<Order> filled_orders_; // List of filled orders.
};
 