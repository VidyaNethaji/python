# Step 1: Product list with prices
products = {
    "Sarees Under – ₹800": "https://www.kaitharinesavu.com/collections/saree-under-800",
    "Sarees Under – ₹1499": "https://www.kaitharinesavu.com/collections/saree-under-1500",
    "Sarees Under – ₹3000": "https://www.kaitharinesavu.com/collections/saree-under-3000",
    "Sarees Under – ₹5000": "https://www.kaitharinesavu.com/collections/saree-under-5000",
}

# Step 2: Convert product keys into a sorted list of (price, name, link)
product_list = []
for name, link in products.items():
    price = int(name.split("₹")[1])
    product_list.append((price, name, link))

# Sort products by price ascending
product_list.sort()

# Step 3: Ask for user budget
budget = int(input("Enter your saree budget in ₹: "))

# Step 4: Show the lowest matching product range
found = False
for price, name, link in product_list:
    if budget <= price:
        print("\n🧺 Sarees within your budget:")
        print(f"- {name}: {link}")
        found = True
        break

if not found:
    print("❌ No products found in your budget range. Try increasing your budget.")
