# 日语
# `urlparse`は、URLを解析するためのPythonのモジュールです。URLをスキーム、ネットロケーション、パス、パラメータ、クエリ、フラグメントに分割します。
# ウェブスクレイピングやAPI呼び出しの際に、URLを操作する必要があるときによく使われます。
# URLのスキームを取得したり、クエリパラメータを抽出するために使われます。

# 英文
# `urlparse` is a Python module for parsing URLs. It breaks down a URL into scheme, netloc, path, params, query, and fragment.
# It is commonly used when handling URLs during web scraping and API calls.
# Used to obtain the scheme of a URL or extract query parameters.

from urllib.parse import urlparse

# URL to be parsed
url = "http://www.example.com/library/books?title=python&author=guido#section1"

# Parse the URL
parsed_url = urlparse(url)

# Accessing different parts of the URL
print(f"Scheme: {parsed_url.scheme}")
print(f"Netloc: {parsed_url.netloc}")
print(f"Path: {parsed_url.path}")
print(f"Params: {parsed_url.params}")
print(f"Query: {parsed_url.query}")
print(f"Fragment: {parsed_url.fragment}")

# Example output:
# Scheme: http
# Netloc: www.example.com
# Path: /library/books
# Params:
# Query: title=python&author=guido
# Fragment: section1
