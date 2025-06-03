#include "useraccount.hpp"
#include <algorithm>

UserAccount::UserAccount(const std::string &username) : username_(username) {}

void UserAccount::Deposit(const std::string &asset, int amount) {
    portfolio_[asset] += amount;
}

bool UserAccount::Withdraw(const std::string &asset, int amount) {
    //std::cout << "Test starting amount: " << portfolio_[asset] << std::endl;
    if (portfolio_[asset] < amount) {
        return false;
    }
    portfolio_[asset] -= amount;
    return true;
}

void UserAccount::AddOrder(const Order &order) {
    open_orders_.push_back(order);
}

// updated version of PrintPortfolio
void UserAccount::PrintPortfolio(std::ostream &os) const {
    os << username_ << "'s Portfolio:";

    // Sort the portfolio by asset name.
    std::vector<std::pair<std::string, int>> sorted_assets(portfolio_.begin(), portfolio_.end());
    std::sort(sorted_assets.begin(), sorted_assets.end());

    for (const auto &[asset, amount] : sorted_assets) {
        os << " " << amount << " " << asset << ",";
    }

    if (!sorted_assets.empty()) {
        os.seekp(-1, std::ios_base::cur); // Remove the trailing comma.
    }
    os << "\n";
}


void UserAccount::PrintOrders(std::ostream &os) const {
    os << username_ << "'s Open Orders (in chronological order):\n";
    for (const auto &order : open_orders_) {
        os << order << "\n";
    }
    os << username_ << "'s Filled Orders (in chronological order):\n";
    for (const auto &order : filled_orders_) {
        os << order << "\n";
    }

}