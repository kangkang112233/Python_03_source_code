# Example of Unpacking Dictionary Items
# In this example, we demonstrate how to unpack both keys and values from a dictionary using a for loop.

# Dictionary containing country codes and their corresponding names in Japanese
country_code = {"GBR": "英国", "TWN": "台湾", "JPN": "日本"}

# Unpacking key-value pairs from the dictionary
for key, value in country_code.items():
    print(f"{key}:{value}")

# Expected output:
# GBR:英国
# TWN:台湾
# JPN:日本
