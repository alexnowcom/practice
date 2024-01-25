import json

# Read the JSON file
with open('transactions.json', 'r') as file:
    transactions = json.load(file)

# Create a dictionary to store the spendign per company
total_spending = {}

# Iterate through each transaction
for transaction in transactions:
    company_id = transaction['company_id'] # Extract the company_id for this transaction, save it to use later
    amount = float(transaction['amount'].replace('$','')) # Convert the amount to float, drop the $

    if company_id in total_spending:
        total_spending[company_id] += amount # add the amount to the ledger
    else:
        total_spending[company_id] = amount # start a new entry

# Print the total spending for each company_id
for company_id, spending in total_spending.items():
    print(f"Company {company_id}: ${spending:.2f}")
