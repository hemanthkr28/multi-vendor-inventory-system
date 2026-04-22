# services.py

def normalize():
    data = []

    from .vendor_data import vendor_a, vendor_b, vendor_c

    for item in vendor_a():
        data.append({
            "product_id": item["id"],
            "vendor_name": "Vendor A",
            "product_name": item["title"],
            "price": item["price"],
            "stock": item["inventory"]
        })

    for item in vendor_b():
        data.append({
            "product_id": item["product_id"],
            "vendor_name": "Vendor B",
            "product_name": item["name"],
            "price": item["cost"],
            "stock": item["stock"]
        })

    for item in vendor_c():
        data.append({
            "product_id": item["sku"],
            "vendor_name": "Vendor C",
            "product_name": item["product_name"],
            "price": item["price"],
            "stock": item["qty"]
        })

    return data