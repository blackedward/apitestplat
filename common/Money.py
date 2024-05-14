def calculate_balances(payments):
    # Calculate the total amount and the average amount
    total_amount = sum(amount for name, amount in payments)
    average_amount = total_amount / len(payments)

    # Calculate the differences from the average
    balances = [(name, amount - average_amount) for name, amount in payments]

    # Split into those who owe money and those who should receive money
    debtors = [(name, -balance) for name, balance in balances if balance < 0]
    creditors = [(name, balance) for name, balance in balances if balance > 0]

    return total_amount, average_amount, balances, debtors, creditors

def settle_debts(debtors, creditors):
    settlements = []
    i, j = 0, 0

    while i < len(debtors) and j < len(creditors):
        debtor_name, debt = debtors[i]
        creditor_name, credit = creditors[j]

        amount = min(debt, credit)
        settlements.append((debtor_name, creditor_name, amount))

        debtors[i] = (debtor_name, debt - amount)
        creditors[j] = (creditor_name, credit - amount)

        if debtors[i][1] == 0:
            i += 1
        if creditors[j][1] == 0:
            j += 1

    return settlements

def main():
    # Define the list of payments. Each element is a tuple (name, amount_paid)
    payments = [
        ("jebe", 3059.8),
        ("dan", 1745.95),
        ("yue", 249.4),
        ("chance", 1316)
    ]

    total_amount, average_amount, balances, debtors, creditors = calculate_balances(payments)
    settlements = settle_debts(debtors, creditors)

    # Print the results
    print(f"Total amount: {total_amount}")
    print(f"Average amount: {average_amount:.2f}")
    print("\nBalances:")
    for name, balance in balances:
        status = "owes" if balance < 0 else "should receive"
        print(f"{name} {status} {abs(balance):.2f}")

    print("\nSettlements:")
    for debtor, creditor, amount in settlements:
        print(f"{debtor} should pay {creditor} {amount:.2f}")

if __name__ == "__main__":
    main()
