import csv
import os
from urllib.parse import urlparse
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # 1) Open the specific product page
    product_url = "https://www.kaitharinesavu.com/collections/raaga-kaithari-nesavu/products/raaga-copper-zaree-cotton-saree"
    page.goto(product_url)
    page.wait_for_load_state("networkidle")
    print(f"✅ Opened: {product_url}")

    # 2) Collect details
    product_data = {}
    product_data["Product URL"] = product_url

    # Product title (H1 on page)
    product_data["Product Title"] = (
        page.locator("h1").inner_text()
        if page.locator("h1").is_visible()
        else None
    )

    # Meta title
    product_data["Meta Title"] = page.title()

    # Meta description
    product_data["Meta Description"] = page.locator(
        "head > meta[name='description']"
    ).get_attribute("content")

    # Product description
    product_data["Product Description"] = (
        page.locator(".product-single__description").inner_text()
        if page.locator(".product-single__description").is_visible()
        else None
    )

    # Collect all image alt texts & file names
    img_alts = []
    img_names = []

    img_locators = page.locator(".product-single__photo img")
    img_count = img_locators.count()
    for i in range(img_count):
        img = img_locators.nth(i)
        img_alt = img.get_attribute("alt")
        img_src = img.get_attribute("src")
        img_name = os.path.basename(urlparse(img_src).path) if img_src else None
        if img_alt:
            img_alts.append(img_alt)
        if img_name:
            img_names.append(img_name)

    product_data["All Image Alts"] = "; ".join(img_alts)
    product_data["All Image Names"] = "; ".join(img_names)

    # 3) Print to console
    print("\n🔎 Product Details:")
    for key, value in product_data.items():
        print(f"{key}: {value}")

    # 4) Save to CSV
    with open("product_output.csv", mode="w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        for key, value in product_data.items():
            writer.writerow([key, value])

    # 5) Save to text file
    with open("product_output.txt", mode="w", encoding="utf-8") as txtfile:
        txtfile.write(f"Product Details from: {product_url}\n\n")
        for key, value in product_data.items():
            txtfile.write(f"{key}: {value}\n")

    print("\n🎉 Done! Saved product details to product_output.csv and product_output.txt.")
    browser.close()
