#include "exchange.hpp"
#include <set>
#include <algorithm>

void Exchange::MakeDeposit(const std::string &username, const std::string &asset, int amount) {
    auto [it, inserted] = user_accounts_.emplace(std::piecewise_construct,
                                                 std::forward_as_tuple(username),
                                                 std::forward_as_tuple(username));
    it->second.Deposit(asset, amount);
}


std::ostream &Exchange::PrintUserPortfolios(std::ostream &os) const {
    os << "User Portfolios (in alphabetical order):\n";

    // Collect all unique assets across all user portfolios
    std::set<std::string> all_assets;
    for (const auto &[username, account] : user_accounts_) {
        for (const auto &[asset, _] : account.GetPortfolio()) {
            all_assets.insert(asset);
        }
    }

    // Collect usernames and sort them alphabetically
    std::vector<std::string> usernames;
    for (const auto &[username, _] : user_accounts_) {
        usernames.push_back(username);
    }
    std::sort(usernames.begin(), usernames.end());

    // Print sorted user portfolios
    for (const std::string &username : usernames) {
        const auto &account = user_accounts_.at(username);
        os << username << "'s Portfolio: ";

        // Create a complete portfolio with all assets
        const auto &portfolio = account.GetPortfolio();

        //bool first = true;

        for (const auto &asset : all_assets) {
            int amount = portfolio.count(asset) ? portfolio.at(asset) : 0;
            if (amount > 0) { // Only print non-zero balances
                os << amount << " " << asset << ", ";
            }
        }

        os << "\n"; // Add trailing comma and newline for each user
    }

    return os;
}





bool Exchange::MakeWithdrawal(const std::string &username, const std::string &asset, int amount) {
    auto it = user_accounts_.find(username);
    if (it == user_accounts_.end()) return false; // User not found

    return it->second.Withdraw(asset, amount);
}

// start changes
bool Exchange::AddOrder(const Order &order) {
    // Check if the user exists
    auto it = user_accounts_.find(order.username);
    if (it == user_accounts_.end()) return false; // User not found

    UserAccount &account = it->second;

    // Validate the order
    if (!ValidateOrder(order, account)) return false;

    // Try to match the order
    if (MatchOrder(order)) {
        return true; // Trade executed successfully
    }

    // Reserve funds for the order
    if (!ReserveFundsForOrder(order, account)) return false;

    // Add the order to the user's account if no match is found
    AddOrderToAccount(order, account);
    return true;
}

bool Exchange::ValidateOrder(const Order &order, const UserAccount &account) const {
    const auto &portfolio = account.GetPortfolio();
    if (order.side == "Buy") {
        int total_cost = order.amount * order.price;
        auto it = portfolio.find("USD");
        return it != portfolio.end() && it->second >= total_cost; // Check if user has enough USD
    } else if (order.side == "Sell") {
        auto it = portfolio.find(order.asset);
        return it != portfolio.end() && it->second >= order.amount; // Check if user has enough of the asset
    }
    return false; // Invalid side
}

bool Exchange::ReserveFundsForOrder(const Order &order, UserAccount &account) {
    if (order.side == "Buy") {
        int total_cost = order.amount * order.price;
        return account.Withdraw("USD", total_cost); // Deduct USD for a buy order
    } else if (order.side == "Sell") {
        return account.Withdraw(order.asset, order.amount); // Deduct asset for a sell order
    }
    return false; // Invalid side
}

void Exchange::AddOrderToAccount(const Order &order, UserAccount &account) {
    account.AddOrder(order);
}

bool Exchange::MatchOrder(const Order &new_order) {
    for (auto &[username, account] : user_accounts_) {
        auto &open_orders = account.GetOpenOrders();
        for (auto it = open_orders.begin(); it != open_orders.end(); ++it) {
            const Order &existing_order = *it;

            // Check if the new order matches the existing order
            if (new_order.asset == existing_order.asset &&
                new_order.side != existing_order.side &&
                new_order.price == existing_order.price &&
                new_order.amount == existing_order.amount) {
                
                // Execute the trade
                ExecuteTrade(new_order, existing_order);

                // Remove the matched order from the list
                open_orders.erase(it);
                return true;
            }
        }
    }
    return false; // No match found
}

void Exchange::ExecuteTrade(const Order &buy_order, const Order &sell_order) {
    auto &buyer = user_accounts_.at(buy_order.username);
    auto &seller = user_accounts_.at(sell_order.username);

    if(buy_order.amount <= sell_order.amount) {

        int total_cost = buy_order.amount * buy_order.price;

        // Update buyer's portfolio
        buyer.Withdraw("USD", total_cost);
        buyer.Deposit(buy_order.asset, buy_order.amount);

        //seller.Withdraw(sell_order.asset, sell_order.amount); -> since we already hold the amount of the asset, we don't need to withdraw it again
        seller.Deposit("USD", total_cost);

        // add the buy and sell trade to the filled orders
        buyer.GetFilledOrders().push_back(buy_order);
        seller.GetFilledOrders().push_back(sell_order);
    }
    if(buy_order.amount > sell_order.amount) {
        int total_seller = sell_order.amount * buy_order.price;
        int total_buyer = buy_order.amount * buy_order.price;

        // Update buyer's portfolio
        buyer.Withdraw("USD", total_buyer);
        buyer.Deposit(buy_order.asset, sell_order.amount);

        //seller.Withdraw(sell_order.asset, sell_order.amount); -> since we already hold the amount of the asset, we don't need to withdraw it again
        seller.Deposit("USD", total_seller);

        // add the buy and sell trade to the filled orders
        buyer.GetFilledOrders().push_back(buy_order);
        seller.GetFilledOrders().push_back(sell_order);
    }
}


// end changes

std::ostream& Exchange::PrintUsersOrders(std::ostream &os) const {
    //Users Orders (in alphabetical order):
    //should be this line
    os << "Users Orders (in alphabetical order):\n";
    for (const auto &[username, account] : user_accounts_) {
        account.PrintOrders(os);
    }
    return os;
}

std::ostream& Exchange::PrintTradeHistory(std::ostream &os) const {
    os << "Trade history not yet implemented.\n";
    return os;
}

std::ostream& Exchange::PrintBidAskSpread(std::ostream &os) const {
    os << "Bid/Ask spread not yet implemented.\n";
    return os;
}