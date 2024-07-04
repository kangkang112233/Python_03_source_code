# parse_qsl関数は、URLクエリ文字列を解析して、キーと値のペアのリストを返します。この関数はPythonのurllib.parseモジュールに含まれています。
# The parse_qsl function parses a URL query string and returns a list of key-value pairs. This function is included in Python's urllib.parse module.

from urllib.parse import parse_qsl, urlparse

# Example URL with query string for a library management system
url = "http://example.com/library?title=Python+Programming&author=John+Doe&year=2021&genre=Technology"

# Parse the URL and extract the query string
query_string = urlparse(url).query

# Parse the query string into a list of key-value pairs
params = parse_qsl(query_string)

# Display the key-value pairs in a readable format
for key, value in params:
    print(f"{key}: {value}")
