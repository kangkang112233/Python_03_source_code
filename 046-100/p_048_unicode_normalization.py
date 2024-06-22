import unicodedata

# Define a string with combined characters
original_string = "café"

# Normalize to NFC form
nfc_normalized = unicodedata.normalize("NFC", original_string)
print(f"NFC Normalized: {nfc_normalized}")

# Normalize to NFD form
nfd_normalized = unicodedata.normalize("NFD", original_string)
print(f"NFD Normalized: {nfd_normalized}")

# Demonstration for a book management system
# Assume we are comparing user input in various forms
user_input = "cafe\u0301"  # 'e' and the accent as separate characters
if unicodedata.normalize("NFC", user_input) == nfc_normalized:
    print("User input matches the NFC normalized form in our database.")
