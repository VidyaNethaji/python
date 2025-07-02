# Product list: (Display Name, Link)
products = {
    "Sarees Under – ₹800": "https://www.kaitharinesavu.com/collections/saree-under-800",
    "Sarees Under – ₹1499": "https://www.kaitharinesavu.com/collections/saree-under-1500",
    "Sarees Under – ₹3000": "https://www.kaitharinesavu.com/collections/saree-under-3000",
    "Sarees Under – ₹5000": "https://www.kaitharinesavu.com/collections/saree-under-5000",
}

# Tier logic based on budget
def get_collections(budget):
    if budget <= 800:
        return ["Sarees Under – ₹800"]
    elif budget <= 1499:
        return ["Sarees Under – ₹800", "Sarees Under – ₹1499"]
    elif budget <= 3000:
        return ["Sarees Under – ₹800", "Sarees Under – ₹1499", "Sarees Under – ₹3000"]
    else:
        return list(products.keys())  # all collections

# Input
budget = int(input("Enter your saree budget in ₹: "))

# Fetch matching collections
matching_collections = get_collections(budget)

# Output
print("\n🧺 Saree Collections Based on Your Budget:")
for name in matching_collections:
    print(f"- {name}: {products[name]}")
