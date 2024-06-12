class WeChatMessage:
    def __init__(self, sender, content):
        self.sender = sender
        self.content = content

    def __repr__(self):
        # Providing a detailed string representation of the object
        return f"WeChatMessage(sender={self.sender!r}, content={self.content!r})"


# Create an instance of WeChatMessage
message = WeChatMessage("Alice", "Hello, Bob!")

# Use repr to get the detailed string representation
print(repr(message))  # Output: WeChatMessage(sender='Alice', content='Hello, Bob!')

# Another example with different content
message2 = WeChatMessage("Bob", "Hi, Alice!")

# Use repr to get the detailed string representation
print(repr(message2))  # Output: WeChatMessage(sender='Bob', content='Hi, Alice!')

