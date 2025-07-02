# Step 1: Product list with prices
products = {
    "Sarees Under – ₹800": "https://www.kaitharinesavu.com/collections/saree-under-800",
    "Sarees Under – ₹1499": "https://www.kaitharinesavu.com/collections/saree-under-1500",
    "SSarees Under– ₹3000": "https://www.kaitharinesavu.com/collections/saree-under-3000",
    "Sarees Under – ₹5000": "https://www.kaitharinesavu.com/collections/saree-under-5000",
}

# Step 2: Ask for user input
budget = int(input("Enter your saree budget in ₹: "))

# Step 3: Filter and show matching products
print("\n🧺 Sarees within your budget:")

found = False
for name, link in products.items():
    price = int(name.split("₹")[1])
    if price <= budget:
        print(f"- {name}: {link}")
        found = True

if not found:
    print("❌ No products found in your budget range. Try increasing your budget.")
