#include "utility.hpp"
#include <iostream>

std::ostream &operator<<(std::ostream &os, const Order &order) {
    os << order.side << " " << order.amount << " " << order.asset
       << " at " << order.price << " USD by " << order.username;
    return os;
}

std::ostream &operator<<(std::ostream &os, const Trade &trade) {
    os << trade.amount << " " << trade.asset << " at " << trade.price
       << " USD between " << trade.buyer_username << " and " << trade.seller_username;
    return os;
}

// Implement the comparison operators
bool operator==(const Order &lhs, const Order &rhs) {
    return lhs.username == rhs.username &&
           lhs.side == rhs.side &&
           lhs.asset == rhs.asset &&
           lhs.amount == rhs.amount &&
           lhs.price == rhs.price;
}

bool operator==(const Trade &lhs, const Trade &rhs) {
    return lhs.buyer_username == rhs.buyer_username &&
           lhs.seller_username == rhs.seller_username &&
           lhs.asset == rhs.asset &&
           lhs.amount == rhs.amount &&
           lhs.price == rhs.price;
}
