products = {}

# Create
products[1] = {"name": "Laptop", "price": 50000}
products[2] = {"name": "Mobile", "price": 20000}

# Read
print("Product Records:")
for product_id, details in products.items():
    print(product_id, details)

# Update
products[1]["price"] = 55000

print("\nAfter Update:")
print(products)

# Delete
del products[2]

print("\nAfter Delete:")
print(products)