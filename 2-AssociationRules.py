def generate_candidates(prev_candidates, k):
    candidates = set()
    for itemset1 in prev_candidates:
        for itemset2 in prev_candidates:
            union = itemset1.union(itemset2)
            if len(union) == k:
                candidates.add(union)
    return candidates


def support_count(transactions, itemset):
    count = 0
    for transaction in transactions:
        if itemset.issubset(transaction):
            count += 1
    return count


def apriori(transactions, min_support):
    itemsets = []
    k = 1
    unique_items = set(item for transaction in transactions for item in transaction)
    candidates = set(frozenset([item]) for item in unique_items)

    while candidates:
        frequent_itemsets = []
        for itemset in candidates:
            support = support_count(transactions, itemset)
            if support >= min_support:
                frequent_itemsets.append((itemset, support))
        itemsets.extend(frequent_itemsets)
        k += 1
        candidates = generate_candidates(set(itemset for itemset, _ in frequent_itemsets), k)

    return itemsets


def generate_rules(frequent_itemsets, transactions, min_confidence):
    rules = []
    for itemset, support in frequent_itemsets:
        if len(itemset) > 1:
            for item in itemset:
                antecedent = frozenset([item])
                consequent = itemset - antecedent
                confidence = support_count(transactions, itemset) / support_count(transactions, antecedent)
                if confidence >= min_confidence:
                    rules.append((antecedent, consequent, confidence))
    return rules


# Take user input for transactions
transactions = []
num_transactions = int(input("Enter the number of transactions: "))
for i in range(num_transactions):
    items = input(f"Enter items for transaction {i + 1} (comma-separated): ").split(',')
    transactions.append(set([item.strip() for item in items]))

# Take user input for minimum support and confidence
min_support = int(input("Enter the minimum support count: "))
min_confidence = float(input("Enter the minimum confidence (between 0 and 1): "))

# Find frequent itemsets
frequent_itemsets = apriori(transactions, min_support)

# Generate association rules
association_rules = generate_rules(frequent_itemsets, transactions, min_confidence)

# Print frequent itemsets
print("\nFrequent Itemsets:")
for itemset, support in frequent_itemsets:
    print(f"{set(itemset)} : {support}")

# Print association rules
print("\nAssociation Rules:")
for antecedent, consequent, confidence in association_rules:
    print(f"{set(antecedent)} => {set(consequent)} : {confidence}")
