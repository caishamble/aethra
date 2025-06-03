# FREEZE CODE BEGIN
###########################################
# FUNCTIONS SECTION TOP                   #
# (Place functions below)                 #
#-----------------------------------------#
# FREEZE CODE END
from SS24_P3Library import f_GetNextCustomerNumber
from SS24_P3Library import f_GetNextTransactionID
from SS24_P3Library import f_GetMenuSelection
import csv




# FREEZE CODE BEGIN
#-----------------------------------------#
# FUNCTIONS SECTION BOTTOM                #
###########################################
if __name__ == '__main__':
# FREEZE CODE END
  pass


def read_customer_file(file_name):
    customers = []
    with open(f".guides/datafiles/{file_name}", "r") as file:
        lines = file.readlines()
        for line in lines[1:]:
            customer = {
                'customer_number': int(line[0:5]),
                'customer_name': line[5:35].strip(),
                'customer_email': line[35:65].strip(),
                'customer_pin': int(line[65:69]),
                'customer_balance': float(line[69:77]),
                'customer_credit_limit': float(line[77:85])
            }
            customers.append(customer)
    return customers

def read_transaction_file(file_name):
    transactions = []
    with open(f".guides/datafiles/{file_name}", "r") as file:
        lines = file.readlines()
        for line in lines[1:]:
            transaction_id, customer_number, transaction_type, transaction_date, vendor, amount = line.strip().split(",")
            transaction = {
                'transaction_id': int(transaction_id),
                'customer_number': int(customer_number),
                'transaction_type': transaction_type,
                'transaction_date': transaction_date,
                'vendor': vendor,
                'amount': float(amount)
            }
            transactions.append(transaction)
    return transactions

def add_customer(customers, customer_name, customer_email, customer_pin, customer_credit_limit):
    if any(customer['customer_email'] == customer_email for customer in customers):
        print("*** Customer already on file, transaction canceled ***")
        return
    customer_number = next_customer_number(customers)
    customer = {
        'customer_number': customer_number,
        'customer_name': customer_name,
        'customer_email': customer_email,
        'customer_pin': customer_pin,
        'customer_balance': 0.0,
        'customer_credit_limit': customer_credit_limit
    }
    customers.append(customer)

def update_transactions(transactions, customers, transaction_type, customer_number, transaction_date, amount, vendor, transaction_pin, next_transaction_id):
    if not any(customer['customer_number'] == customer_number for customer in customers):
        print("*** Customer not on file, transaction canceled ***")
        return
    if transaction_type == "Charge":
        if not any(customer['customer_number'] == customer_number and customer['customer_pin'] == transaction_pin for customer in customers):
            transactions.append({
                'transaction_id': next_transaction_id(),
                'customer_number': customer_number,
                'transaction_type': "Rejected",
                'transaction_date': transaction_date,
                'vendor': vendor,
                'amount': amount
            })
            return
        customer = next(customer for customer in customers if customer['customer_number'] == customer_number)
        if customer['customer_balance'] + amount > customer['customer_credit_limit']:
            transactions.append({
                'transaction_id': next_transaction_id(),
                'customer_number': customer_number,
                'transaction_type': "Rejected",
                'transaction_date': transaction_date,
                'vendor': vendor,
                'amount': amount
            })
            return
        transactions.append({
            'transaction_id': next_transaction_id(),
            'customer_number': customer_number,
            'transaction_type': "Charge",
            'transaction_date': transaction_date,
            'vendor': vendor,
            'amount': amount
        })
        customer['customer_balance'] += amount
    elif transaction_type == "Payment":
        transactions.append({
            'transaction_id': next_transaction_id(),
            'customer_number': customer_number,
            'transaction_type': "Payment",
            'transaction_date': transaction_date,
            'vendor': "",
            'amount': amount
        })
        customer = next(customer for customer in customers if customer['customer_number'] == customer_number)
        customer['customer_balance'] -= amount

def print_customer_statements(customers, transactions):
    for customer in customers:
        print(f"{customer['customer_number']} {customer['customer_name']} {customer['customer_email']} {customer['customer_pin']} {customer['customer_balance']:.2f} {customer['customer_credit_limit']}")
        purchases = sum(transaction['amount'] for transaction in transactions if transaction['customer_number'] == customer['customer_number'] and transaction['transaction_type'] == "Charge")
        payments = sum(transaction['amount'] for transaction in transactions if transaction['customer_number'] == customer['customer_number'] and transaction['transaction_type'] == "Payment")
        rejects = sum(transaction['amount'] for transaction in transactions if transaction['customer_number'] == customer['customer_number'] and transaction['transaction_type'] == "Rejected")
        print(f"Purchases: {purchases:.2f}")
        print(f"Payments: {payments:.2f}")
        print(f"Rejects: {rejects:.2f}")
        print()

def display_customer_list_information(customers):
    for customer in customers:
        print(f"{customer['customer_number']} {customer['customer_name']} {customer['customer_email']} {customer['customer_pin']} {customer['customer_balance']:.2f} {customer['customer_credit_limit']}")

def display_transaction_list_information(transactions):
    for transaction in transactions:
        print(f"{transaction['transaction_id']} {transaction['customer_number']} {transaction['transaction_type']} {transaction['transaction_date']} {transaction['vendor']} {transaction['amount']}")

def next_customer_number(customers):
    return f_GetNextCustomerNumber(customers)

def next_transaction_id():
    return f_GetNextTransactionID()




def f_bumpcounter(counter, increment):
    return counter + increment

def f_sum_amounts(customer_number, transaction_type, transaction_customer_numbers, transaction_types, transaction_amounts):
    return sum(transaction_amount for transaction_customer_number, transaction_type, transaction_amount in zip(transaction_customer_numbers, transaction_types, transaction_amounts) if transaction_customer_number == customer_number and transaction_type == transaction_type)

def main():
    customer_file_name = input("Enter customer file name: ")
    transaction_file_name = input("Enter transaction file name: ")
    customers = read_customer_file(customer_file_name)
    transactions = read_transaction_file(transaction_file_name)

    next_transaction_id = lambda: f_bumpcounter(max(transaction['transaction_id'] for transaction in transactions), 1)

    while True:
        print("------------------------")
        print("1. Add Customer")
        print("2. Update Transactions")
        print("3. Print Customer Statement")
        print("4. Display Customer List Information")
        print("5. Display Transaction List Information")
        print("X. Exit Program")
        print("------------------------")
        option = input("Enter menu option: ")
        if option == "1":
            customer_name, customer_email, customer_pin, customer_credit_limit = input("Enter new customer information (LN, FN; Email; PIN; credit limit): ").split(";")
            add_customer(customers, customer_name, customer_email, int(customer_pin), float(customer_credit_limit))
        elif option == "2":
            transaction_type, customer_number, transaction_date, amount = input("Charge |Customer #|Transaction Date|$ Amount|Vendor|Transaction PIN\nPayment|Customer #|Transaction Date|$ Amount\nEnter transaction: ").split("|")
            if transaction_type == "Charge":
                vendor, transaction_pin = amount, transaction_date
                amount = float(vendor)
                update_transactions(transactions, customers, transaction_type, int(customer_number), transaction_date, amount, vendor, int(transaction_pin), lambda: next_transaction_id)
            elif transaction_type == "Payment":
                update_transactions(transactions, customers, transaction_type, int(customer_number), transaction_date, float(amount), "", 0, lambda: next_transaction_id)
        elif option == "3":
            print_customer_statements(customers, transactions)
        elif option == "4":
            display_customer_list_information(customers)
        elif option == "5":
            display_transaction_list_information(transactions)
        elif option.lower() == "x":
            break

if __name__ == '__main__':
    main()
