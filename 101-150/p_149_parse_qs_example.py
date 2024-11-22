# parse_qs関数は、URLクエリストリングを解析し、辞書形式で結果を返します。
# The parse_qs function parses a URL query string and returns the result as a dictionary.

from urllib.parse import parse_qs

# Example URL query string
query_string = (
    "title=The+Great+Gatsby&author=F.+Scott+Fitzgerald&year=1925&title=The+Great+Gatsby"
)

# Parse the query string into a dictionary
parsed_query = parse_qs(query_string)

# Adjust the output format for better readability
for key, value in parsed_query.items():
    print(f"{key}: {', '.join(value)}")

# The expected output will be:
# title: The Great Gatsby, The Great Gatsby
# author: F. Scott Fitzgerald
# year: 1925
