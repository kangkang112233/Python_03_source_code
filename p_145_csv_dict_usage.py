# csv.DictReader
# csv.DictReaderはCSVファイルを辞書として読み込むためのPythonクラスです。
# 主にCSVデータをキーと値のペアとして扱いたい場合に使用されます。

# csv.DictReader is a Python class for reading CSV files as dictionaries.
# It is mainly used when you need to handle CSV data as key-value pairs.

# csv.DictWriter
# csv.DictWriterは辞書をCSVファイルとして書き出すためのPythonクラスです。
# 主に辞書形式のデータをCSV形式で保存する場合に使用されます。

# csv.DictWriter is a Python class for writing dictionaries to CSV files.
# It is mainly used when you need to save dictionary-formatted data in CSV format.

import csv

# Define the file path as a variable
csv_file_path = "D:\\2024-01-29-0008_sort_by_creation_date\\2024-05-16-2335_Python 3 Certified Practical Engineer\\新建 Microsoft Excel 工作表.csv"

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

# Read the data back from the CSV file
with open(csv_file_path, "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(f"Title: {row['title']}, Author: {row['author']}, Year: {row['year']}")
