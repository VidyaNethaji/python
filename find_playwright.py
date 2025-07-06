import csv
from urllib.parse import urlparse
import os
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # 1) Open homepage
    page.goto("https://www.kaitharinesavu.com")
    page.wait_for_load_state("networkidle")

    # 2) Click the menu item at your given XPath
    menu_xpath = '//*[@id="section-sections--24558422655258__header"]/div[2]/div/div/div/div[2]/nav/div/ul/li[5]/a'
    page.wait_for_selector(menu_xpath)
    page.locator(menu_xpath).click()
    page.wait_for_load_state("networkidle")
    print("✅ Navigated to collection page.")

    # 3) Grab all product links
    product_links = page.locator("a.grid-product__link").all()
    print(f"🔎 Found {len(product_links)} products on the collection page.")

    # 4) Open files
    csv_file = open("all_products_detailed.csv", mode="w", newline="", encoding="utf-8")
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow([
        "Product URL",
        "Product Title",
        "Meta Title",
        "Description",
        "Meta Description",
        "Image Alt",
        "Image Name"
    ])
    text_file = open("all_products_detailed.txt", mode="w", encoding="utf-8")

    # 5) Loop over each product without limit
    for idx, link in enumerate(product_links, start=1):
        relative_url = link.get_attribute("href")
        if not relative_url:
            continue  # skip broken links

        # Build full URL if needed
        product_url = relative_url if relative_url.startswith("http") else "https://www.kaitharinesavu.com" + relative_url

        print(f"\n➡️ [{idx}] Visiting: {product_url}")
        product_page = browser.new_page()
        product_page.goto(product_url)
        product_page.wait_for_load_state("networkidle")

        # Collect data
        product_data = {}
        product_data["product_url"] = product_url

        # Product title (H1 on page)
        product_data["product_title"] = (
            product_page.locator("h1").inner_text()
            if product_page.locator("h1").is_visible()
            else None
        )

        # Meta title
        product_data["meta_title"] = product_page.title()

        # Description text
        product_data["description"] = (
            product_page.locator(".product-single__description").inner_text()
            if product_page.locator(".product-single__description").is_visible()
            else None
        )

        # Meta description
        product_data["meta_description"] = product_page.locator(
            "head > meta[name='description']"
        ).get_attribute("content")

        # Alt text & image file name from first product image
        if product_page.locator(".product-single__photo img").is_visible():
            img_locator = product_page.locator(".product-single__photo img")
            img_alt = img_locator.get_attribute("alt")
            img_src = img_locator.get_attribute("src")

            # Extract image file name from URL
            if img_src:
                parsed_url = urlparse(img_src)
                img_name = os.path.basename(parsed_url.path)
            else:
                img_name = None
        else:
            img_alt, img_name = None, None

        product_data["image_alt"] = img_alt
        product_data["image_name"] = img_name

        # Write to CSV
        csv_writer.writerow([
            product_data["product_url"],
            product_data["product_title"],
            product_data["meta_title"],
            product_data["description"],
            product_data["meta_description"],
            product_data["image_alt"],
            product_data["image_name"]
        ])

        # Write to text file
        text_file.write(f"\n--- Product {idx} ---\n")
        for key, value in product_data.items():
            text_file.write(f"{key}: {value}\n")

        print(f"✅ Product {idx} data saved.")
        product_page.close()

    print("\n🎉 Done scraping ALL products in the collection!")
    csv_file.close()
    text_file.close()
    browser.close()
