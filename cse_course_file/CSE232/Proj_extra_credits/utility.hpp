#pragma once
#include <iostream>
#include <string>

struct Order {
    std::string username;
    std::string side;  // "Buy" or "Sell"
    std::string asset;
    int amount;
    int price;

    friend std::ostream &operator<<(std::ostream &os, const Order &order);
    friend bool operator==(const Order &lhs, const Order &rhs); // Add this
};

struct Trade {
    std::string buyer_username;
    std::string seller_username;
    std::string asset;
    int amount;
    int price;

    friend std::ostream &operator<<(std::ostream &os, const Trade &trade);
    friend bool operator==(const Trade &lhs, const Trade &rhs); // Add this
};