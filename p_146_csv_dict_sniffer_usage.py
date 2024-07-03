# csv.Sniffer
# csv.Snifferクラスは、CSVファイルのデータ形式を推測するためのクラスです。
# CSVファイルとTSVファイルを自動的に判別して読み込む場合に使用されます。

# csv.Sniffer is a class for deducing the format of CSV files.
# It is used when you need to automatically distinguish and read CSV and TSV files.

import csv

# Define the file path as a variable
csv_file_path = "books.csv"

# Sample data as a list of dictionaries for a library management system
book_data = [
    {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "year": "1951"},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": "1960"},
    {"title": "1984", "author": "George Orwell", "year": "1949"},
]

# Write the sample data to a CSV file
with open(csv_file_path, "w", newline="") as csvfile:
    fieldnames = ["title", "author", "year"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for book in book_data:
        writer.writerow(book)

# Read the data back from the CSV file using Sniffer to deduce the format
with open(csv_file_path, "r") as csvfile:
    # Sniff the dialect
    dialect = csv.Sniffer().sniff(csvfile.read(1024))
    csvfile.seek(0)
    reader = csv.DictReader(csvfile, dialect=dialect)
    for row in reader:
        print(f"Title: {row['title']}, Author: {row['author']}, Year: {row['year']}")
