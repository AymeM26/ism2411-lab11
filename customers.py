# Exercise 1: One customer
customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 1250.50,
}
print("Exercise 1")
print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)

# Exercise 2: Update and add
print("\nExercise 2")
customer["phone"] = "555-123-4567"
print(customer)

customer["tier"] = "platinum"
print(customer)

del customer["email"]
print(customer)

# Exercise 3: Safe lookup
print("\nExercise 3")
print(customer.get("email", "no email on file"))

try:
    print(customer["email"])
except KeyError:
    print("KeyError: 'email' is not in the dictionary")

# Exercise 4: Iterate
print("\nExercise 4")
for key, value in customer.items():
    print(f"{key}: {value}")

# Looping over the dict without .items() gives only the keys, not the
# values. .items() gives (key, value) pairs, so we can unpack both.
for key in customer:
    print(key)

# Exercise 5: Lookup table
print("\nExercise 5")
tier_discounts = {"bronze": 0, "silver": 0.05, "gold": 0.10, "platinum": 0.15}

tier = customer["tier"]
discount = tier_discounts.get(tier, 0)
price = 200
final_price = price * (1 - discount)
print(f"Tier: {tier}")
print(f"Discount: {discount * 100:.0f}%")
print(f"Final price: ${final_price:.2f}")

# Exercise 6: List of dicts
print("\nExercise 6")
customers = [
    {"name": "Alice", "email": "alice@example.com", "tier": "platinum", "ytd_spend": 3200.00},
    {"name": "Bob", "email": "bob@example.com", "tier": "silver", "ytd_spend": 640.25},
    {"name": "Cara", "email": "cara@example.com", "tier": "bronze", "ytd_spend": 120.00},
]

purchase = 300
for c in customers:
    rate = tier_discounts.get(c["tier"], 0)
    discount_amount = purchase * rate
    print(f"{c['name']} | {c['tier']} | discount: ${discount_amount:.2f}")

# Exercise 7: Nested catalog
print("\nExercise 7")
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8},
}

for product, info in catalog.items():
    if info["stock"] < 20:
        print(f"LOW STOCK: {product} ({info['stock']} left)")

# Exercise 8: Sales by region
print("\nExercise 8")
transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200},
]

summary = {}
for t in transactions:
    summary[t["region"]] = summary.get(t["region"], 0) + t["amount"]

for region in sorted(summary):
     print(f"{region}: {summary[region]}")